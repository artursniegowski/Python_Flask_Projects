from custom_decorators import admin_only
from datetime import date
from env_variables import FLASK_SECRET_KEY, GMAIL_APP_PASSWORD, HOST_EMAIL_FOR_CONTACT_FORM, MY_EMAIL, POSTGRESQL_DATABASE_URL 
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from forms import CommentForm, CreatePostForm, LogInForm, RegisterForm
from notification_manager import NotificationManager
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

################################################################################
# DONT ADJUST THESE VARIABLES HERE !!
# email adress where we want to send the notification to, - 
# you need to specify where to which address to send it !!
EMAIL_RECIVER = HOST_EMAIL_FOR_CONTACT_FORM 
################################################################################


# creating an email sender manager object for sending emails
email_sender_manager = NotificationManager(email_app_password=GMAIL_APP_PASSWORD
                                            ,email_from=MY_EMAIL)


# creating flask object and its variables
app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_SECRET_KEY
ckeditor = CKEditor(app)
Bootstrap(app)


# Initialize flask_gravatar for avatars in comments
# Gravatar uses your email address to provide your image to other sites
# If you own a WordPress or GitHub account, you probably also have a Gravatar 
# account, and your data was scraped in the leak
gravatar = Gravatar(app,
                    size=100,
                    rating='g',
                    default='retro',
                    force_default=False,
                    force_lower=False,
                    use_ssl=False,
                    base_url=None)



## Connect to Database
# create the extension
db = SQLAlchemy()
# configure the SQLite database, relative to the app instance folder
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
# Upgrade SQLite Database to PostgreSQL - Heroku - resources tab PostgreSQL added
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRESQL_DATABASE_URL
# initialize the app with the extension
db.init_app(app)


# creating Flaks-Login manager
login_manager = LoginManager()
# config it for login
login_manager.init_app(app)


# Table configuration
# for comments
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    
    # Many to one  RELATIONSHIP - parent relationship
    # Create reference to the User object, the "posts" refers to the posts 
    # protperty in the User class.
    comment_author = relationship('User', back_populates='comments')
    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    # Create reference to the BlogPost object, the "comments" refers to the comments 
    # protperty in the BlogPost class.
    parent_post = relationship('BlogPost', back_populates = 'comments')
    # Create Foreign Key, "blog_posts.id" the blog_posts refers to the tablename of BlogPost.
    parent_post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))

#  for blog post
class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    # Many to one  RELATIONSHIP - parent relationship
    # Create reference to the User object, the "posts" refers to the posts 
    # protperty in the User class.
    author = relationship('User', back_populates='posts')
    # Create Foreign Key, "users.id" the users refers to the tablename of User.
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))


    # ONE TO MANY RELATIONSHIP - child relationship
    # FOR one BlogPost - many comments
    # This will act like a List of Comment objects attached to each BlogPost. 
    # The "parent_post" refers to the parent_post property in the Comment class.
    comments = relationship('Comment', back_populates = 'parent_post')
  

    # represenation when printed
    def __repr__(self):
        return f'<BlogPost {self.title}>'

# for user
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(250))
    name = db.Column(db.String(100))

    # ONE TO MANY RELATIONSHIP - child relationship
    # FOR POSTS one user - many posts
    # This will act like a List of BlogPost objects attached to each User. 
    # The "author" refers to the author property in the BlogPost class.
    posts = relationship('BlogPost', back_populates = 'author')

    # FOR Comments one user - many comments
    # This will act like a List of Comment objects attached to each User. 
    # The "author" refers to the author property in the BlogPost class.
    comments = relationship('Comment', back_populates = 'comment_author')
  

    # represenation when printed
    def __repr__(self):
        return f'<User {self.name}>'



# create table schema in the database
with app.app_context():
    # create_all does not update tables if they are already in the database!
    db.create_all()

# This callback is used to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

################## ROUTES ############

# GET ALL posts
@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route('/register', methods = ["GET","POST"])
def register():
    register_form = RegisterForm()

    # if form is validated then it has to be the post request !
    if register_form.validate_on_submit():

        check_if_user_exists = User.query.filter_by(email=register_form.email.data).first()

        # if a user with the given email adress already exists, redirect to login page
        # give feed back to the current user !
        if not check_if_user_exists:

            # create a new user
            new_user = User(
                email = register_form.email.data,
                name = register_form.name.data,
                # saving the password as a hash with salt 
                password = generate_password_hash(
                    password=register_form.password.data, 
                    method="pbkdf2:sha256", 
                    salt_length=8),
            )

            # saving data to database
            db.session.add(new_user)
            db.session.commit()

            # Login and validate the user.
            login_user(new_user)

            return redirect(url_for('get_all_posts'))

        else:

            # flask flash message
            flash("This email address is already being used. Please sign in!")
            # redirect to login page
            return redirect(url_for('login'))


    return render_template("register.html", form = register_form)


@app.route('/login', methods = ["GET","POST"])
def login():
    login_form = LogInForm()
    # if form is validated then it has to be the post request !
    if login_form.validate_on_submit():
        
        # getting data from the data base
        user_trying_to_login = User.query.filter_by(email=login_form.email.data).first()

        # if the user exists with the given email address check the password
        if user_trying_to_login:

            # checking the hashed password - true if matches
            if check_password_hash(user_trying_to_login.password, login_form.password.data):
                
                # Login and validate the user.
                login_user(user_trying_to_login)

                return redirect(url_for('get_all_posts'))
            else:
                # flask flash message
                flash("Password incorrect!")
                return redirect(url_for("login"))

        else:
            # flask flash message
            flash("This email address dosent exists!")
            return redirect(url_for("login"))

    return render_template("login.html", form = login_form)


@app.route('/logout')
def logout():
    # loggin out the current user
    logout_user()
    return redirect(url_for('get_all_posts'))



# GET ONE post
@app.route("/post/<int:post_id>", methods = ["GET","POST"])
def show_post(post_id):
    requested_post = BlogPost.query.get_or_404(post_id)
    comment_form = CommentForm()

    # getting all the comment for the requested post
    all_comments = requested_post.comments
    # print(all_comments)

    # if form is validated then it has to be the post request !
    if comment_form.validate_on_submit():
        
        # if the curretn user is not authenticated / logged in 
        # redirect to login page !
        if not current_user.is_authenticated:
            flash("You need to login or register to comment.")
            return redirect(url_for("login"))

        # otherwise save the comment to the database
        new_comment = Comment(
            text = comment_form.comment.data,
            comment_author = current_user,
            parent_post = requested_post,
        )

        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for("show_post",post_id=post_id))


    return render_template("post.html", post=requested_post, form = comment_form, all_comments = all_comments)
    
# POST new post
@app.route("/new_post", methods = ["GET","POST"])
@admin_only
def new_post():

    add_post_form = CreatePostForm()

    # if form is validated then it has to be the post request !
    if add_post_form.validate_on_submit():
       
        # add post to the database

        current_time = date.today()

        # create a new post
        new_post = BlogPost(
            title = add_post_form.title.data,
            subtitle = add_post_form.subtitle.data,
            date = current_time.strftime("%B %d, %Y"),
            body = add_post_form.body.data,
            author = current_user,
            img_url = add_post_form.img_url.data,
        )

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('get_all_posts'))

    return render_template("make-post.html", form = add_post_form, new_post = True)



# Update a post
@app.route("/post-edit/<int:post_id>", methods = ["GET","POST"])
@admin_only
def edit_post(post_id):
    requested_post = BlogPost.query.get_or_404(post_id)
    
    update_post_form = CreatePostForm(
        obj = requested_post
        # or you can pass any of the properties from the form
        # title = requested_post.title 
        )
    
    # if form is validated then it has to be the post request !
    if update_post_form.validate_on_submit():

        # update the database with the values from the form post request
        requested_post.title = update_post_form.title.data
        requested_post.subtitle = update_post_form.subtitle.data
        requested_post.body = update_post_form.body.data
        requested_post.img_url = update_post_form.img_url.data

        db.session.commit()

        # redirecting to detail view
        return redirect(url_for('show_post',post_id=requested_post.id))

    return render_template("make-post.html", form = update_post_form, new_post = False)


# DELETE post
@app.route("/delete/<int:post_id>")
@admin_only
def delete_post(post_id):
    requested_post = BlogPost.query.get_or_404(post_id)
    
    db.session.delete(requested_post)
    db.session.commit()
    
    # redirecting to home / all posts view
    return redirect(url_for('get_all_posts'))


# about
@app.route("/about")
def about():
    return render_template("about.html")


# creating contacts route
@app.route("/contact", methods = ["GET", "POST"])
def contact():
    successfully_sent = False
    # contact form - reciving data
    if request.method == "POST":
        try:
            data = request.form
            # request.form['username'] - if the key dosent exists we will get KeyError - 404 bad request
            # user_name = request.args.get('username', 'NoName') - for get requests
            name = data['name'] 
            email = data['email'] 
            phone_number = data['phone_number'] 
            message = data['message'] 
            
        except KeyError:
            # handle the exception of not existing key element like password or username in the form
            print("Key error")
            return render_template("404.html")
        else:

            # creating message for the email
            message_content = f"Name: {name}\nEmail: {email}\nPhone: {phone_number}\nMessage: {message}"
            # sending an email
            email_sender_manager.send_gmail_mail(email_title="New Message", 
                                            message_to_send=message_content, 
                                            email_to=EMAIL_RECIVER)
            successfully_sent = True
        
        return render_template('contact.html', successfully_sent = successfully_sent)
    else: # GET
        return render_template('contact.html', successfully_sent = successfully_sent)



# 404 error handler - page not found
@app.errorhandler(404)
def page_not_found(errors):
# note that we set the 404 status explicitly
  return render_template("404.html"), 404


# 403 error handler - Forbidden
@app.errorhandler(403)
def page_forbidden(errors):
# note that we set the 403 status explicitly
  return render_template("403.html"), 403


# running the app and setting the required env variable
if __name__ == "__main__":
    # only run if it's not imported
    # so only if the file main.py is run directly and not imported
    # by another file

    # adding the env variable for Flask to work
    # > $env:FLASK_APP = "main"
    import os
    # print(os.environ.get("FLASK_APP"))
    os.environ["FLASK_APP"] = "main"

    # > flask run
    # start server
    # in a debug mode not suitable for production !!
    app.run(host="0.0.0.0", port=5000, debug=False)
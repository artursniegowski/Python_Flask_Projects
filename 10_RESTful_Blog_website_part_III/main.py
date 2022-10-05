from datetime import date
from env_variables import FLASK_SECRET_KEY, GMAIL_APP_PASSWORD, MY_EMAIL 
from notification_manager import NotificationManager
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor, CKEditorField
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL


################################################################################
# ADJUST THESE VARIABLES !!
# email adress where we want to send the notification to, - 
# you need to specify where to which address to send it !!
EMAIL_RECIVER = "your_email_@domain.me" 
################################################################################


# creating an email sender manager object for sending emails
email_sender_manager = NotificationManager(email_app_password=GMAIL_APP_PASSWORD
                                            ,email_from=MY_EMAIL)



# creating flask object and its variables
app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_SECRET_KEY
ckeditor = CKEditor(app)
Bootstrap(app)


## Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# creating pointer to the database
db = SQLAlchemy(app)



# Table configuration
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")




################## ROUTES ############

# GET ALL posts
@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)

# GET ONE post
@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = BlogPost.query.get_or_404(post_id)

    return render_template("post.html", post=requested_post)
    
# POST new post
@app.route("/new_post", methods = ["GET","POST"])
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
            author = add_post_form.author.data,
            img_url = add_post_form.img_url.data,
        )

        db.session.add(new_post)
        db.session.commit()

        return redirect(url_for('get_all_posts'))

    return render_template("make-post.html", form = add_post_form, new_post = True)



# Update a post
@app.route("/post-edit/<int:post_id>", methods = ["GET","POST"])
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
        requested_post.author = update_post_form.author.data
        requested_post.img_url = update_post_form.img_url.data

        db.session.commit()

        # redirecting to detail view
        return redirect(url_for('show_post',post_id=requested_post.id))

    return render_template("make-post.html", form = update_post_form, new_post = False)


# DELETE post
@app.route("/delete/<int:post_id>")
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

# contact
# @app.route("/contact")
# def contact():
#     return render_template("contact.html")

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
  return render_template("404.html")


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
    app.run(host="0.0.0.0", port=5000, debug=True)
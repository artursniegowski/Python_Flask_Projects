from env_variables import FLASK_SECRET_KEY
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


UPLOAD_FOLDER = 'static'
SECRET_FILE_NAME = 'files/cheat_sheet.pdf'


# # create the app and its variables
app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

## Connect to Database
# create the extension
db = SQLAlchemy()
# configure the SQLite database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# initialize the app with the extension
db.init_app(app)

# creating Flaks-Login manager
login_manager = LoginManager()
# config it for login
login_manager.init_app(app)

## CREATE TABLE IN DB - define the models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# Line below only required once, when creating DB. 

# create table schema in the database
with app.app_context():
    # create_all does not update tables if they are already in the database!
    db.create_all()

# This callback is used to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# routes
# home
@app.route('/')
def home():
    return render_template("index.html")

# register
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        
        data = request.form
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        # hashing and salting the password
        password = generate_password_hash(password=password, method="pbkdf2:sha256", salt_length=8)

        # checking if the email dosent exist in the database
        if not User.query.filter_by(email=email).first():

            new_user = User(
                email = email,
                password = password,
                name = name,
            )

            db.session.add(new_user)
            db.session.commit()

            #Log in and authenticate user after adding details to database.
            login_user(new_user)

            return redirect(url_for('secrets'))

        # otherwise redirect to the login page
        else:
            flash("This email already exists. Sign In!")
            return redirect(url_for('login'))

    else:
        return render_template("register.html")

# login
@app.route('/login', methods=["GET","POST"])
def login():
    if request.method == "POST":
        
        data = request.form
        email = data.get('email')
        password = data.get('password')

        # getting data from the data base
        user_trying_to_login = User.query.filter_by(email=email).first()

        # if the user exists with the given email address check the password
        if user_trying_to_login:

            # checking the hashed password - true if matches
            if check_password_hash(user_trying_to_login.password, password):
                # Login and validate the user.
                # user should be an instance of your `User` class
                login_user(user_trying_to_login)

                return redirect(url_for('secrets'))

            else:
                flash('Wrong password. Try again.')
        else:
            flash('The email does not exist. Try again.')

    return render_template("login.html")

# secrets
@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name = current_user.name)

# logout
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))

# download
@app.route('/download')
@login_required
def download():
    return send_from_directory(directory=app.config["UPLOAD_FOLDER"], path=SECRET_FILE_NAME)




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
    app.run(debug=True)
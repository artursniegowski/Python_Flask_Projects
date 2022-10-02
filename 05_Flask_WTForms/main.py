from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, Length


# env variables !
from dotenv import load_dotenv
load_dotenv()
import os

################################################################################
## sensitive data ###
#####################
# user defined WTF_CSRF_SECRET_KEY !
# In order to generate the csrf token, you must have a secret key, this is 
# usually the same as your Flask app secret key. If you want to use another 
# secret key, config it.
# env variables ! - dont change here !
FLASK_SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
################################################################################


app = Flask(__name__)
# setting secret key 
# in order to generate the csrf token, you must have a secret key
app.secret_key = FLASK_SECRET_KEY
# adding bootstrap
Bootstrap(app)



### Forms ###
# login Form
class LoginForm(FlaskForm):
    """creating a form for the login page"""
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)] )
    submit_form = SubmitField(label='Log In')


# Flask routs
# / 
@app.route("/")
def home():
    return render_template('index.html')

# /login
@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    # validation will be successful after the user submited the form (POST)
    # or False if failed
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and \
            login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form = login_form)



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
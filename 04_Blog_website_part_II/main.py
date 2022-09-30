from notification_manager import NotificationManager
from flask import Flask, render_template, request
import requests

# env variables !
from dotenv import load_dotenv
load_dotenv()
import os


################################################################################
# ADJUST THESE VARIABLE !!
# npoint - create json data for posts - your own endpoint !!!
API_NPOINT_ENDPPOINT = "https://api.npoint.io/dadsfsdfsadfasdfasf"
# email adress where we want to send the notification to, - 
# you need to specify where to send it !!
EMAIL_RECIVER = "example@proton.me" 
################################################################################


################################################################################
## sensitive data ###
#####################
# user defined email and app password - has to be GMAIL !
# env variables ! - dont change here !
MY_EMAIL = os.environ.get('MY_EMAIL')
GMAIL_APP_PASSWORD = os.environ.get('GMAIL_APP_PASSWORD')
################################################################################


# creating an email sender manager object for sending emails
email_sender_manager = NotificationManager(email_app_password=GMAIL_APP_PASSWORD
                                            ,email_from=MY_EMAIL)


# creating Flask object
app = Flask(__name__)

# function for retriving the posts data
def get_posts_data(url_endpoint: str) -> list[dict]:
    """
    retriving the data from an API and storing in a list
    """
    response = requests.get(url_endpoint)
    response.raise_for_status()

    all_posts = response.json()

    if all_posts:
        return all_posts
    else:
        return None


# FLASK ROUTING
# creating index route / home
@app.route("/")
def home():
    return render_template('index.html', all_posts = get_posts_data(API_NPOINT_ENDPPOINT))

# creating about route
@app.route("/about")
def about():
    return render_template('about.html')


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
        else:
            
            # print(name)
            # print(email)
            # print(phone_number)
            # print(message)

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


# creating detail post view
@app.route("/post/<int:num>")
def detail_post(num):
    all_posts = get_posts_data(API_NPOINT_ENDPPOINT)
    org_post = None
    for post in all_posts:
        if post['id'] == num:
            org_post = post 
            break

    return render_template('post.html', post = org_post)




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
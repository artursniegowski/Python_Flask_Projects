from flask import Flask
from markupsafe import escape
from flask_custom_decorators import add_html_img, add_html_tag
from random import randint

app = Flask(__name__)


# generating a random number that the user has to quess
random_number = randint(0,9)
print(f"number to guess: {random_number}")

# creating index route
@app.route("/")
@add_html_img(src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif")
@add_html_tag(tag='h1', inline_style="color: blue; text-transform: uppercase;")
def index():
    website_title = "Guess a number between 0 and 9"
    return website_title

# creating guessed number page
@app.route("/<int:number>")
@add_html_img(src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif")
def guessed_number(number):
    
    if 0 <= number <= 9:
        if number < random_number:
            return "<h1 style='color: red;'>Too low, try again!</h1>"
        elif number > random_number:
            return "<h1 style='color: orange;'>Too high, try again</h1>"
        else:
            return f"<h1 style='color: green;'>You guessed the number! {escape(number)} was the random number !</h1>"
    else:
        return f"<h1 style='color: yellow;'>The number: {escape(number)} is not in range!</h1>"


# running the app and setting the required env variable
if __name__ == "__main__":
    # only run if it's not imported
    # so only if the file main_flask.py is run directly and not imported
    # by another file

    # adding the env variable for Flask to work
    # > $env:FLASK_APP = "main_flask"
    import os
    # print(os.environ.get("FLASK_APP"))
    os.environ["FLASK_APP"] = "main_flask"

    # > flask run
    # start server
    # in a debug mode not suitable for production !!
    app.run(debug=True)
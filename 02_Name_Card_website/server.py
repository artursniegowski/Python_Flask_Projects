from flask import Flask
from flask import render_template


app = Flask(__name__)

# creating index route
@app.route("/")
def home():
    return render_template('index.html')


# running the app and setting the required env variable
if __name__ == "__main__":
    # only run if it's not imported
    # so only if the file server.py is run directly and not imported
    # by another file

    # adding the env variable for Flask to work
    # > $env:FLASK_APP = "server"
    import os
    # print(os.environ.get("FLASK_APP"))
    os.environ["FLASK_APP"] = "server"

    # > flask run
    # start server
    # in a debug mode not suitable for production !!
    app.run(debug=True)
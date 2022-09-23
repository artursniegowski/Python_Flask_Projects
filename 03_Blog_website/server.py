from flask import Flask
from flask import render_template
from post import Post
import requests


API_NPOINT_ENDPPOINT = "https://api.npoint.io/8cf1faf4e455dcc4755e"


app = Flask(__name__)


def get_posts_data(url_endpoint: str) -> list[Post]:
    """
    retriving the data from an API and storing in a list of Post
    """
    response = requests.get(url_endpoint)
    response.raise_for_status()

    data = response.json()
    list_of_posts = []

    for post in data:
        new_post = Post(
            id = post['id'],
            title = post['title'],
            subtitle = post['subtitle'],
            body = post['body'],
        )
        list_of_posts.append(new_post)

    return list_of_posts

# making it globally accesible 
lists_of_posts = get_posts_data(API_NPOINT_ENDPPOINT)


# creating index route / home
@app.route("/")
def home():
    return render_template('index.html', posts = lists_of_posts)


# creating detail post view
@app.route("/post/<int:num>")
def detail_post(num):
    org_post = None
    for post in lists_of_posts:
        if post.id == num:
            org_post = post 
            break

    return render_template('post.html', post = org_post)




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
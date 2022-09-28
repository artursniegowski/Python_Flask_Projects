from flask import Flask, url_for, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

# env variables !
from dotenv import load_dotenv
load_dotenv()
import os

################################################################################
## sensitive data ###
#####################
# In order to generate the csrf token, you must have a secret key, this is 
# usually the same as your Flask app secret key. If you want to use another 
# secret key, config it.
# env variables ! - dont change here !
FLASK_SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
################################################################################


# creating flask object and its variables
app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_SECRET_KEY
# database uri
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books-collection.db'
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# creating the book model for database
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<User {self.title}>'

# create the initial database
# should only run once to create your database
db.create_all()



# all Flask routes below
# main route - home - /
@app.route('/')
def home():
    # gettin all the books from the data base
    all_books = db.session.query(Book).all()
    return render_template("index.html", books = all_books)



# /add route
@app.route("/add", methods = ["GET", "POST"])
def add():
    if request.method == "POST":
        try: 
            data = request.form
            book_name = data['book-name']
            book_author = data['book-author']
            book_rating = data['book-rating']
        except KeyError:
            # handle the exception of not existing key element in the form
            print("Key error in books form")
        else:

            # CREATE new entry in the database
            new_book = Book(title=book_name, author=book_author, rating=book_rating)
            db.session.add(new_book)
            db.session.commit()

            # redirect after submiting data
            return redirect(url_for("home"))
        
    return render_template("add.html")


# /edit_book/1 route
@app.route("/edit_book/<int:id>", methods = ["GET", "POST"])
def edit_book(id):
    book = Book.query.get(id)

    if request.method == "POST":
        try: 
            data = request.form
            new_book_rating = data['new-book-rating']
        except KeyError:
            # handle the exception of not existing key element in the form
            print("Key error in books form")
        else:
            # updating the new value in the database
            book.rating = new_book_rating
            db.session.commit()

            # redirect after submiting data
            return redirect(url_for("home"))
        
    return render_template("edit_book.html",book=book)


# /delete route
# http://127.0.0.1:5000/delete?id=1
@app.route("/delete")
def delete_book():

    # getting the id
    book_id = request.args.get('id')
    # getting the book
    book = Book.query.get(book_id)
    # deleting the book
    db.session.delete(book)
    db.session.commit()

       
    # redirect to home
    return redirect(url_for("home"))


#### running the website ####

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

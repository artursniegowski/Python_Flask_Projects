# 07_Virtual_Bookshelf

This is a website that keeps track of the books we have read and was created using the Python framework Flask.
The data is stored in a database and managed by using SQLAlchemy from Flask to serve it whenever it is needed.
The main page will display a list of all the books in the database, and the user will have the option of:</br>
- adding a new book to the database (title, author, rating), </br>
- updating the rating of an existing book,</br>
- deleting an existing book.</br>
This is a project to get more familiar with the CRUD operations with Flask SQLAlchemy.
Jinja2, Jinja2-Templates, Flask-SQLAlchemy, and Forms are some of the main features.

---

Flask</br>
https://flask.palletsprojects.com/en/2.1.x/</br>

Flask-SQLAlchemy</br>
https://flask-sqlalchemy.palletsprojects.com/en/2.x/</br>

Jinja templates</br>
https://jinja.palletsprojects.com/en/3.1.x/</br>

---

The necessary steps to make the program work:</br>
1. Install the required libraries from the requirements.txt using the following command: </br>
*pip install -r requirements.txt*</br>
2. Change the name of .env.example to .env and define the environmental variable (https://flask.palletsprojects.com/en/2.2.x/config/#SECRET_KEY):</br>
FLASK_SECRET_KEY = "your_secret_key_keep_it_secret"</br>


---

**Example views from the website:**</br>


***The home page - book list.***</br>
![Screenshot](docs/img/01_home.png)</br>

---

***Adding a new book view.***</br>
![Screenshot](docs/img/02_adding_new_book.png)</br>

---

***Editing an existing book rating view.***</br>
![Screenshot](docs/img/03_edit_rating.png)</br>

---

***Home page after deleting the first book - user gets redirected.***</br>
![Screenshot](docs/img/04_after_deleting_first_book.png)</br>


---

**The program was developed using python 3.10.6, Flask 2.2, Flask-SQLAlchemy, Jinja2**


In order to run the program, you have to execute main.py.
And your website will be accessible under localhost:5000 (http://127:0:0:1:5000).
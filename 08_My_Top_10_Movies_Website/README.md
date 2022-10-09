# 08_My_Top_10_Movies_Website

This is a website that compiles a list of your top favourite movies of all time.
It was developed using Python / Flask / WTForms /SQLite / SQLAlchemy / Flask-Bootstrap.
The movie data is stored in a SQLite database and managed with the help of SQLAlchemy.
The user can add movies and search for them according to titles with the help of the API 
https://www.themoviedb.org/ which will find the available movies that can be added to the list. The movies will be ordered and ranked on the main page as neatly formatted flip cards based on the user ratings.
The user also has the option to delete any of the movies from the list, as well as update the rating and review at any time. Changing ratings of the movies will result in an updated order/rank list. 


This is a project to get more familiar with the CRUD operations with Flask SQLAlchemy and get a more in-depth understanding of the powerful Flask framework.
Some of the main features are Jinja2, Jinja2-Templates, Flask-SQLAlchemy, SQLAlchemy, SQLite, WTForms, Flask-Bootstrap, consuming APIs, and many more.
The forms are handled using the quick_form from Flask bootstrap (https://pythonhosted.org/Flask-Bootstrap/forms.html). 

---

Flask</br>
https://flask.palletsprojects.com/en/2.1.x/</br>

Flask-SQLAlchemy</br>
https://flask-sqlalchemy.palletsprojects.com/en/2.x/</br>

SQLAlchemy</br>
https://docs.sqlalchemy.org/en/14/orm/query.html </br>

WTForms</br>
https://wtforms.readthedocs.io/en/2.3.x/</br>

Flask-WTF</br>
https://flask-wtf.readthedocs.io/en/1.0.x/</br>

Flask-Bootstrap</br>
https://pythonhosted.org/Flask-Bootstrap/index.html#</br>

Jinja templates</br>
https://jinja.palletsprojects.com/en/3.1.x/</br>

---

The necessary steps to make the program work:</br>
1. Install the required libraries from the requirements.txt using the following command: </br>
*pip install -r requirements.txt*</br>
2. In order to make the website work you will need an API KEY which you can obtain for
free from https://developers.themoviedb.org/3/getting-started/introduction. </br>
3. Change the name of .env.example to .env and define the environmental variables (https://flask.palletsprojects.com/en/2.2.x/config/#SECRET_KEY):</br>
**FLASK_SECRET_KEY** = "your_secret_key_keep_it_secret"</br>
**THEMOVIEDB_API_KEY**='your_api_the_moviedb_key'</br>


---

**Example views from the website:**</br>



***The home page - flipping cards.***</br>
![flip-card-home-page](docs/img/08_flip_card_gif.gif)


---


***The home page - movie list.***</br>
![Screenshot](docs/img/01_Home_page.png)</br>


---

***Home page - flipped selected card.***</br>
![Screenshot](docs/img/02_Home_Page_card_flipped.png)</br>


---

***Update movie rating and review - view.***</br>
![Screenshot](docs/img/03_Updating_movie_Rating_review_page.png)</br>

---

***Home page after deleting a movie.***</br>
![Screenshot](docs/img/04_Home_page_after_deleting_movie.png)</br>


---

***Adding a movie page - view.***</br>
![Screenshot](docs/img/05_adding_movie_page.png)</br>


---

***Adding a movie page - list view with the results from the API themoviedb. The User has to select which movie to add.***</br>
![Screenshot](docs/img/06_list_of_movies_from_API.png)</br> 


---

***Home page after adding a movie.***</br>
![Screenshot](docs/img/07_Home_view_after_adding_a_movie.png)</br>



---

**The program was developed using python 3.10.6, Flask 2.2, Flask-SQLAlchemy, SQLite, Flask-WTF, Flask-Bootstrap, Jinja2, CSS**


In order to run the program, you have to execute main.py.
And your website will be accessible under localhost:5000 (http://127:0:0:1:5000).

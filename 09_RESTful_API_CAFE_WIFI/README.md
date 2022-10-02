# 09_RESTful_API_CAFE_WIFI

This is a RESTful API created with Python / Flask / SQLite / SQLAlchemy.
It has a home page with a link to the documentation for the API created with the help
of Postman (https://www.postman.com/).
This RESTful API uses the data from its cafe database to respond to the users' requests.
The database consists of a list of cafes and some information about them to help the user 
to decide whether a particular cafe is a suitable place to work in.
The user can make different HTTP requests like: </br>
-GET (the user can request data for all the cafes, a random cafe, or a cafe by location), </br>
-POST (the user can add a new cafe to the database), </br>
-PATCH (the user can update the price of coffee for a given cafe), </br>
-DELETE (the user can delete a given cafe from the database, but only with a valid api_key). </br>

In the documentation you can find how to make all the requests with the necessary key words.


---

Flask</br>
https://flask.palletsprojects.com/en/2.1.x/</br>

Flask-SQLAlchemy</br>
https://flask-sqlalchemy.palletsprojects.com/en/2.x/</br>

SQLAlchemy</br>
https://docs.sqlalchemy.org/en/14/orm/query.html </br>

Testing and documentation APIs - Postman </br>
https://www.postman.com/ </br>

Viewing database - SQLite browser </br>
https://sqlitebrowser.org/dl/ </br>

---

The necessary steps to make the program work:</br>
1. Install the required libraries from the requirements.txt using the following command: </br>
*pip install -r requirements.txt*</br>
2. Change the name of .env.example to .env and define the environmental variables (https://flask.palletsprojects.com/en/2.2.x/config/#SECRET_KEY):</br>
**FLASK_SECRET_KEY** = "your_secret_key_keep_it_secret"</br>



---

**Example views from the website:**</br>



***The home page with a link to the documentation.***</br>
![Screenshot](docs/img/01_home.png)


---


***documentation - overview.***</br>
***https://documenter.getpostman.com/view/23653195/2s83tFGWqi***</br>
***docs/Cafe & Wifi - documentation.pdf***</br>
![Screenshot](docs/img/02_API_docs.png)</br>


---

**The program was developed using python 3.10.6, Flask 2.2, Flask-SQLAlchemy, SQLite**


In order to run the program, you have to execute main.py.
And your website will be accessible under localhost:5000 (http://127:0:0:1:5000).
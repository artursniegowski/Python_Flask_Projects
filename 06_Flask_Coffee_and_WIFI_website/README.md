# 06_Flask_Coffee_and_WIFI_website

It is a website where the user can use it to scan for a nearby cafe and check what time they are open and if they have good coffee and easy access to wifi and power sockets in case they want to work in one of them.
The main page consists of two buttons, each of which will redirect the user either to the whole list of cafes stored, or to a site where the user can fill out the given form and add a new cafe to the list.
The cafes are stored in a csv file and handled with Python and Flask.
In order to submit the form for adding a new coffee, the user's data has to pass validation.
The form is handled using the quick_form from Flask bootstrap (https://pythonhosted.org/Flask-Bootstrap/forms.html).
Inheriting Templates Using Jinja2, Jinja2-Templates, Flask-Bootstrap, Flask-WTF, WTForms, and Forms Validation are some of the main features.

---

Flask</br>
https://flask.palletsprojects.com/en/2.1.x/</br>


Jinja templates</br>
https://jinja.palletsprojects.com/en/3.1.x/</br>


WTForms</br>
https://wtforms.readthedocs.io/en/2.3.x/</br>


Flask-WTF</br>
https://flask-wtf.readthedocs.io/en/1.0.x/</br>


Flask-Bootstrap</br>
https://pythonhosted.org/Flask-Bootstrap/index.html#</br>


CSV File Reading and Writing</br>
https://docs.python.org/3/library/csv.html</br>

---

The necessary steps to make the program work:</br>
1. Install the required libraries from the requirements.txt using the following command: </br>
*pip install -r requirements.txt*</br>
2. Change the name of .env.example to .env and define the environmental variable (https://flask.palletsprojects.com/en/2.2.x/config/#SECRET_KEY):</br>
FLASK_SECRET_KEY = "your_secret_key_keep_it_secret"</br>


---

**Example views from the website:**</br>


***The home page.***</br>
![Screenshot](docs/img/home.png)</br>

---

***The cafes list pag.***</br>
![Screenshot](docs/img/list_cafes.png)</br>

---

***The adding cafe page.***</br>
![Screenshot](docs/img/adding_cafe.png)</br>

---

***The adding cafe page - with validation.***</br>
![Screenshot](docs/img/adding_cafe_2.png)</br>


---

**The program was developed using python 3.10.6, Flask 2.2, Flask-WTF, Jinja2, Flask-Bootstrap, csv-python**


In order to run the program, you have to execute main.py.
And your website will be accessible under localhost:5000 (http://127:0:0:1:5000).
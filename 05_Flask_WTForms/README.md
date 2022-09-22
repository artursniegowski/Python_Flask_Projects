# 05_Flask_WTForms

This is an example project in Flask showing how to start using the Flask-WTF, which gives a number of benefits over the simple HTML form.
With easy form validation, it makes sure that the user is entering the data in the required format and fields, with less code, and build in CSRF Protection (CSRF stands for Cross Site Request Forgery).
This website consists of the main page with a login button. After pressing it, the user gets transferred to the login page,
where an email and password are required. The "secret" is revealed to the user after entering the correct email address and password; otherwise, the user is presented with an access denied website.
Main Features include: Inheriting Templates Using Jinja2, Jinja2 - templates, Flask-Bootstrap, Flask-WTF, WTForms, Forms validation. 

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

---

The necessary steps to make the program work:</br>
1. Install the required libraries from the requirements.txt using the following command: </br>
*pip install -r requirements.txt*</br>
2. Change the name of .env.example to .env and define the environmental variable (https://flask.palletsprojects.com/en/2.2.x/config/#SECRET_KEY):</br>
FLASK_SECRET_KEY = "your_secret_key_keep_it_secret"</br>

</br>
</br>

The correct user data to reveal the secret:</br>
email: admin@email.com</br>
password: 12345678</br>

---

**Example views from the website:**</br>


***The home page.***</br>
![Screenshot](docs/img/home.png)</br>

---

***The Log in page.***</br>
![Screenshot](docs/img/login_page.png)</br>

---

***The Log in - success page.***</br>
![Screenshot](docs/img/login_success.png)</br>

---

***The Log in - deny page.***</br>
![Screenshot](docs/img/login_denied.png)</br>


---

**The program was developed using python 3.10.6, Flask 2.2, Flask-WTF, Jinja2, Flask-Bootstrap**


In order to run the program, you have to execute main.py.
And your website will be accessible under localhost:5000 (http://127:0:0:1:5000).

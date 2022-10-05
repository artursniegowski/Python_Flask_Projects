# 10_RESTful_Blog_website_part_III

This is a blog website that is basically an upgraded version of the 04_Blog_website_II, which was built using the Python framework Flask. The styling was done with the help of additional Bootstrap templates (https://startbootstrap.com/previews/clean-blog), Flask-Bootstrap, Bootstrap, CSS. The main features are:</br>
- RESTful Blog - with the blog you will be able to create new posts, edit and delete existing posts from the database (Flask HTTP requests and forms WTF),</br>
- CKEditorField - The CK Editor field renders the CK editor control that allows users to visually work with HTML and save the results back into a text property.</br>
- all the posts will be stored in a SQLite database and managed with Flask-SQLAlchemy,</br>
- dynamically generated blogpost pages with full screen titles,</br>
- multi-page website with an interactive navigation bar,</br>
- fully mobile responsive with an adaptive navigation bar,</br> 
- fully functional contact form (POST request - Flask) that will send an email form to the specified email receiver,</br>
- error handling - 404 - page not found.</br>


The data for each post is stored using an SQLite database and managed with the help of Flask-SQLAlchemy.
The blog can perform POST, GET, DELETE HTTP request in order to create, edit or delete a post in the database.


The main page consists of a list of posts (titles and subtitles), with the option to open each post, which will redirect the user into a detailed view of the given post. The user can also add a post from the main page with the help of the button: Create new Post. On top of that, from the detail view of each post can be edited.
The adaptive navabr has the options of about, contact, and home page. The contact view has a form where the user can fill up the required data and send it to the server as a POST request, which will be processed and sent to the given email address in the form with a short message.


---

Flask</br>
https://flask.palletsprojects.com/en/2.1.x/</br>

Flask-SQLAlchemy</br>
https://flask-sqlalchemy.palletsprojects.com/en/2.x/</br>

SQLAlchemy</br>
https://docs.sqlalchemy.org/en/14/orm/query.html </br>

Viewing database - SQLite browser </br>
https://sqlitebrowser.org/dl/ </br>

Jinja templates</br>
https://jinja.palletsprojects.com/en/3.1.x/</br>

WTForms</br>
https://wtforms.readthedocs.io/en/2.3.x/</br>

Flask-WTF</br>
https://flask-wtf.readthedocs.io/en/1.0.x/</br>

Flask-CKEditor</br>
https://flask-ckeditor.readthedocs.io/en/latest/basic.html</br>

Flask-Bootstrap</br>
https://pythonhosted.org/Flask-Bootstrap/index.html#</br>

Bootstrap </br>
https://getbootstrap.com/ </br>

Email SMTP </br>
https://docs.python.org/3/library/smtplib.html </br>


---

The necessary steps to make the program work:</br>
1. Install the required libraries from the requirements.txt using the following command: </br>
*pip install -r requirements.txt*</br>
2. Before using the program, we need to create a Gmail account that the program can use and generate an app_pssword for our account (https://help.prowly.com/how-to-create-use-gmail-app-passwords). After creating the Gmail account, we have to change the name of .env.example to .env and define the environmental variables according to our account:</br>
MY_EMAIL = "EXAMPLE.USER@gmail.com"</br>
GMAIL_APP_PASSWORD = "GMAIL_APP_PASSWORD"</br>
3. Define the Flask environmental variables in .env (https://flask.palletsprojects.com/en/2.2.x/config/#SECRET_KEY):</br>
**FLASK_SECRET_KEY** = "your_secret_key_keep_it_secret"</br>
4. Adjust the variable **EMAIL_RECIVER** in the file main.py. This the the host email, where all the emails from contact form will be sent to.



---

**Example views from the website:**</br>


***The home page - desktop view.***</br>
![Screenshot](docs/img/01-Home_page_desktop.png)</br>

---

***The home page - mobile view.***</br>
![Screenshot](docs/img/02-Home_page_mobile.png)</br>

---

***Detailed post view.***</br>
![Screenshot](docs/img/03_detailed_post_view.png)</br>

---

***The About page.***</br>
![Screenshot](docs/img/04_about_view.png)</br>

---

***The Contact page with the contact form filled in.***</br>
![Screenshot](docs/img/05_contact_view_and_filled_form.png)</br>

---

***After successfully submitting the contact form, the contact page appears with a message***</br>
![Screenshot](docs/img/06_contact_view_after_data_sent.png)</br>

---

***Example email received from the website.***</br>
![Screenshot](docs/img/07_email_recived.png)</br>

---

***Create a new post view.***</br>
![Screenshot](docs/img/08_Create_New_Post_View.png)</br>

---

***Detail Post view - after adding a post.***</br>
![Screenshot](docs/img/09_Detail_Post_View_after_adding.png)</br>

---

***Edit a post view.***</br>
![Screenshot](docs/img/10_Edit_Post_view.png)</br>

---

**The program was developed using python 3.10.6, Flask 2.2, Flask-Bootstrap, Flask-CKEditor, Flask-SQLAlchemy, Flask-WTF, SQLite, Email SMTP**


In order to run the program, you have to execute main.py.
And your website will be accessible under localhost:5000 (http://127:0:0:1:5000).

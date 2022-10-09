# 12_Blog_website_with_Users_part_IV
This is a fully-fledged blog website that is ready to be published and launched. It's an upgraded version of the previous blog website (10_RESTful_Blog_website_part_III). The blog was developed using the Python framework Flask. The styling was done with the help of additional Bootstrap templates (https://startbootstrap.com/previews/clean-blog), Flask-Bootstrap, Bootstrap, and CSS. Some extra functionality like registering and authenticating users was added, as well as the ability for authenticated users to comment on blog posts. </br>
The main features are:</br>
- RESTful Blog: with the blog you will be able to create new posts, edit and delete existing posts from the database (Flask HTTP requests and forms WTF). Only the admin user (id = 1), the first user to register on the blog, will have these rights. </br>
- Authentication-users for the website and giving different permissions. There will be 3 groups that are distinguished: admin, logged users, and anonymous users (not logged in). </br>
- all the posts will be stored in a SQLite database and managed with Flask-SQLAlchemy.</br>
- use of Gravatar images to provide an avatar image for blog commenters.</br>
- Making use of Relational Databases (one-to-many relationship).</br>
- Message Flashing using Flask Flash to give feedback to the user. They will be visible only for one session. </br>
- CKEditorField-The CK Editor field renders the CK editor control that allows users to visually work with HTML and save the results back into a text property. </br>
- blog post pages with full-screen titles that are generated dynamically. </br>
- multi-page website with an interactive navigation bar.</br>
- fully mobile responsive with an adaptive navigation bar.</br>
- a fully functional contact form (POST request-Flask) that will send an email form to the specified email receiver. </br>
- customised error handling-403-page Forbidden.</br>
- customised error handling-404-page not found.</br> 




The data for each post, user, and comment is stored respecively in three different tables using an SQLite database and managed with the help of Flask-SQLAlchemy. Between these tables, there exists a database relationship "A one to many", which makes it easy to locate all the comments belonging to each post or all the blog posts belonging to a specific user.
The blog can perform POST, GET, and DELETE HTTP requests in order to create, edit, or delete a post in the database.
As mentioned earlier, there will be three groups of users:</br> 
- admin (id = 1, the first user that registers on the blog),</br> 
- logged users (any user that has registered after the admin),</br> 
- anonymous users (not logged in).</br> 


Depending on the group the user belongs to, they will be able to perform different tasks on the blog.</br> 
Admin users will have all rights over the blog website. They will be able to read, create, update, and delete posts, as well as comment on the blog posts.</br> 
Regular logged-in users will be allowed only to read posts and comment on them.</br> 
The anonymous users/not logged in users will be allowed only to read the posts.</br>  



The main page consists of a list of posts (titles and subtitles), with the option to open each post, which will redirect the user into a detailed view of the given post. The admin user can add a post from the main page with the help of the button: Create New Post. On top of that, from the detail view, each post can be edited but only by an admin user.
The adaptive navigation has different options depending on whether a user is authenticated or not.</br>  
Authenticated users will have the options: HOME, LOGOUT, ABOUT, CONTACT.</br>  
Not-Authenticated users (not logged in) will have the options: HOME, LOGIN, REGISTER, ABOUT, CONTACT.</br>  


The contact view has a form where the user can fill up the required data and send it to the server as a POST request, which will be processed and sent to the given email address in the form with a short message.



Each user that wants to be authenticated needs to register. After registering, the users' data will be stored securely in the database. Afterwards, the user can simply log in to the blog.
When the user gets registered, the email address, user name , and hashed password with salt are stored in the database in the users table. 
This website shows how authentication is done with the use of Flask and Flask-login while maintaining the highest security by hashing the user passwords and adding salt to them and then storing the hash in the database instead of the password itself.


If the user is not logged in or does not have permission to access a specific website, the server will respond with a customised error message either:</br> 
- HTTP 403: Forbidden</br> 
- HTTP 404: page not found</br> 



In order to give a better user experience, Flask flash messaging was implemented to give feedback to the user if the email address is incorrect, like if it already exists in the database, or if the email address does not exist and the user tries to login, or if the password was wrong. The flash messages will be visible only for one session.

---

Database Schema:</br>

![Screenshot](docs/img/14_databse_schema.png)</br>


---

Flask</br>
https://flask.palletsprojects.com/en/2.1.x/</br>

Flask-Login</br>
https://flask-login.readthedocs.io/en/latest/</br>

Hashing + Salting a password</br>
https://werkzeug.palletsprojects.com/en/2.2.x/utils/#werkzeug.security.generate_password_hash</br>

Flask - Message Flashing</br>
https://flask.palletsprojects.com/en/2.2.x/patterns/flashing/#message-flashing</br>

Flask-SQLAlchemy</br>
https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/</br>

SQLAlchemy</br>
https://docs.sqlalchemy.org/en/14/orm/query.html </br>

ONE-TO-MANY Database relationships</br>
https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html?highlight=one+many </br>

Custom Error Pages</br>
https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/</br>

Flask-Gravatar</br>
https://pythonhosted.org/Flask-Gravatar/</br>

Flask decorators</br>
https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/#login-required-decorator</br>

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
5. You have the option of using the existing database with defined users or creating a new one.</br>
user id = 1 </br>
email: admin@gmail.com</br>
password: admin</br>
</br>
user id = 2 </br>
email: tester@gmail.com</br>
password: tester</br>
</br>
Alternatively, you can simply delete the database instance/blog.db and then run main.py.
A new empty database will be created, and you will have to register the users create new posts (The first registered user will become the admin!).
I recommend using the SQLite browser to explore the data currently saved in the database.



---

**Example views from the website:**</br>



***The home page - mobile view.***</br>
![Screenshot](docs/img/01_Home_view_mobile.png)</br>

---

***The home page - desktop view - user is not logged in.***</br>
![Screenshot](docs/img/02_Home_View_desktop_annonymous_user.png)</br>

---

***The home page - desktop view - admin user is logged in.***</br>
![Screenshot](docs/img/03_Home_View_desktop_loggedn_admin_user.png)</br>

---

***The About page.***</br>
![Screenshot](docs/img/04_About_View.png)</br>

---

***The Contact page with the contact form filled in.***</br>
![Screenshot](docs/img/05_contact_View_filled_form.png)</br>

---

***After successfully submitting the contact form, the contact page appears with a message***</br>
![Screenshot](docs/img/06_Contact_View_after_successful_message.png)</br>

---

***Example email received from the website.***</br>
![Screenshot](docs/img/07_email_recived.png)</br>

---

***Login View after unsuccessful login before - red flash message indicating the problem.***</br>
![Screenshot](docs/img/08_Login_View_unsuccessful.png)</br>

---

***Register a user view.***</br>
![Screenshot](docs/img/09_Register_View.png)</br>

---

***New/Add post view - only accessible with an admin user logged in.***</br>
![Screenshot](docs/img/10_New_Post_View_only_admin_user.png)</br>

---

***Detailed post view - admin user logged in - permission to edit and comment.***</br>
![Screenshot](docs/img/11_Detail_View_post_admin_user.png)</br>

---

***Detailed post view - regular user logged in - only permission to comment.***</br>
![Screenshot](docs/img/12_Detail_View_post_regular_user.png)</br>

---

***Edit a post view - possible only with an admin user logged in.***</br>
![Screenshot](docs/img/13_Edit_Post_View_only_admin_user.png)</br>


---

**The program was developed using python 3.10.6, Flask 2.2, Flask-Login, Flask - Message Flashing, Flask-Bootstrap, Flask-CKEditor, Flask-SQLAlchemy, Flask-WTF, SQLite, Email SMTP, Hashing passwords with Wergzeug, Flask-Gravatar, Customized Flask decorators**

In order to run the program, you have to execute main.py.
And your website will be accessible under localhost:5000 (http://127:0:0:1:5000).
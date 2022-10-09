# Python_Flask_Projects
This is a repository of unique Flask projects that you can either use as ideas for your next Flask project or as a source to learn from. Each project contains the full source code and is listed in order of difficulty level. It starts with the easiest project, and with every new project, you will be building more challenging flask web applications. Have a peek and enjoy codding!


## 01_Guess_The_Number_game
This is the  starting project where we create a simple web app developed using Python's web framework, Flask. The user will play a guess the number game, where on the main page the user will be prompted with a question of selecting a number between 0 and 9 and a changing number animation.
The user is supposed to type the guessed number into the path. The web app will then tell us whether we chose the right number or if our guess was too low or high.

## 02_Name_Card_website
This is a web-based name card using one of the templates on HTML 5 Up (https://html5up.net/).
It is exactly like the old school paper name cards, just better.
It was developed using Python's web framework, Flask.

## 03_Blog_website
This is a blog website developed using Python's web framework, Flask.
The main page consists of a list of posts, with the option "Read", which will redirect the user into a detailed view of the given post.
The data for each post is stored using an API (https://www.npoint.io/), which converts our data into an easily accessible API endpoint. The blog website makes a request to this endpoint and retrieves a JSON data representation for each post, which is later rendered into HTML.

## 04_Blog_website_part_II
This is a blog website that is basically an upgraded version of the 03_Blog_website, which was built using the Python framework Flask. The styling was done with the help of additional Bootstrap templates (https://startbootstrap.com/previews/clean-blog), Bootstrap 5, CSS, and JS. The main features are:</br>
- multi-page website with an interactive navigation bar,</br>
- dynamically generated blogpost pages with full screen titles,</br>
- fully mobile responsive with an adaptive navigation bar,</br>
- fully functional contact form (POST request - Flask) that will send an email form to the specified email receiver.</br>

The data for each post is stored using an API (https://www.npoint.io/), which converts our data into an easily accessible API endpoint. The blog website makes a request to this endpoint and retrieves a JSON data representation for each post, which is later rendered into HTML.

## 05_Flask_WTForms
This is an example project in Flask showing how to start using the Flask-WTF, which gives a number of benefits over the simple HTML form.
With easy form validation, it makes sure that the user is entering the data in the required format and fields, with less code, and build in CSRF Protection (CSRF stands for Cross Site Request Forgery).
This website consists of the main page with a login button. After pressing it, the user gets transferred to the login page,
where an email and password are required. The "secret" is revealed to the user after entering the correct email address and password; otherwise, the user is presented with an access denied website.
Main Features include: Inheriting Templates Using Jinja2, Jinja2 - templates, Flask-Bootstrap, Flask-WTF, WTForms, Forms validation.

## 06_Flask_Coffee_and_WIFI_website
It is a website where the user can use it to scan for a nearby cafe and check what time they are open and if they have good coffee and easy access to wifi and power sockets in case they want to work in one of them.
The main page consists of two buttons, each of which will redirect the user either to the whole list of cafes stored, or to a site where the user can fill out the given form and add a new cafe to the list.
The cafes are stored in a csv file and handled with Python and Flask.
In order to submit the form for adding a new coffee, the user's data has to pass validation.
The form is handled using the quick_form from Flask bootstrap (https://pythonhosted.org/Flask-Bootstrap/forms.html).
Inheriting Templates Using Jinja2, Jinja2-Templates, Flask-Bootstrap, Flask-WTF, WTForms, and Forms Validation are some of the main features.

## 07_Virtual_Bookshelf
This is a website that keeps track of the books we have read and was created using the Python framework Flask.
The data is stored in a database and managed by using SQLAlchemy from Flask to serve it whenever it is needed.
The main page will display a list of all the books in the database, and the user will have the option of:</br>
- adding a new book to the database (title, author, rating), </br>
- updating the rating of an existing book,</br>
- deleting an existing book.</br>

This is a project to get more familiar with the CRUD operations with Flask SQLAlchemy.
Jinja2, Jinja2-Templates, Flask-SQLAlchemy, and Forms are some of the main features.

## 08_My_Top_10_Movies_Website
This is a website that compiles a list of your top favourite movies of all time.
It was developed using Python / Flask / WTForms /SQLite / SQLAlchemy / Flask-Bootstrap.
The movie data is stored in a SQLite database and managed with the help of SQLAlchemy.
The user can add movies and search for them according to titles with the help of the API 
https://www.themoviedb.org/ which will find the available movies that can be added to the list. The movies will be ordered and ranked on the main page as neatly formatted flip cards based on the user ratings.
The user also has the option to delete any of the movies from the list, as well as update the rating and review at any time. Changing ratings of the movies will result in an updated order/rank list.

## 09_RESTful_API_CAFE_WIFI
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

## 10_RESTful_Blog_website_part_III
This is a blog website that is basically an upgraded version of the 04_Blog_website_II, which was built using the Python framework Flask. The styling was done with the help of additional Bootstrap templates (https://startbootstrap.com/previews/clean-blog), Flask-Bootstrap, Bootstrap, CSS. The main features are:</br>
- RESTful Blog - with the blog you will be able to create new posts, edit and delete existing posts from the database (Flask HTTP requests and forms WTF),</br>
- CKEditorField - The CK Editor field renders the CK editor control that allows users to visually work with HTML and save the results back into a text property.</br>
- all the posts will be stored in a SQLite database and managed with Flask-SQLAlchemy,</br>
- dynamically generated blogpost pages with full screen titles,</br>
- multi-page website with an interactive navigation bar,</br>
- fully mobile responsive with an adaptive navigation bar,</br>
- fully functional contact form (POST request - Flask) that will send an email form to the specified email receiver,</br>
- error handling - 404 - page not found.</br>


## 11_Flask_Authentication
This is a website where the user has to register in order to be allowed to download the secret file cheat_sheet.pdf.
After registration, the users' data will be stored securely in the database and the next time the user will be able to login.
When the user gets registered, the email address, user name , and hashed password with salt are stored in the database instance/users.db.
This website shows how authetication is done with the use of Flask and Flask-login while maintaining the highest security by hashing the user passwords and adding salt to them and then storing the hash in the database instead of the password itself.
If the user is not logged in and tries to access the routes /download or/secrets, the server will respond with 401 HTTP-Unauthorized. Only logged in / authenticated users will have access to these routes.
In order to give a better user experience, Flask flash messaging was implemented to give feedback to the user if the email address is incorrect, like it exists in the database, or if the email address does not exist and the user tries to login, or if the password was wrong, like it does not match to the email. 
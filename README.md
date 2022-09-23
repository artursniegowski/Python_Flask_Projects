# Python_Flask_Projects
This is a repository of unique Flask projects that you can either use as ideas for your next Flask project or as a source to learn from. Each project contains the full source code and is listed in order of difficulty level. It starts with the easiest project, and with every new project, you will be building more challenging flask web applications. Have a peek and enjoy codding!


## 01_Guess_The_Number_game
This is the  starting project where we create a simple web app developed using Python's web framework, Flask. The user will play a guess the number game, where on the main page the user will be prompted with a question of selecting a number between 0 and 9 and a changing number animation.
The user is supposed to type the guessed number into the path. The web app will then tell us whether we chose the right number or if our guess was too low or high.

## 02_Name_Card_website
This is a web-based name card using one of the templates on HTML 5 Up (https://html5up.net/).
It is exactly like the old school paper name cards, just better.
It was developed using Python's web framework, Flask.

# 03_Blog_website
This is a blog website developed using Python's web framework, Flask.
The main page consists of a list of posts, with the option "Read", which will redirect the user into a detailed view of the given post.
The data for each post is stored using an API (https://www.npoint.io/), which converts our data into an easily accessible API endpoint. The blog website makes a request to this endpoint and retrieves a JSON data representation for each post, which is later rendered into HTML.

# 04_Blog_website_part_II
This is a blog website that is basically an upgraded version of the 03_Blog_website, which was built using the Python framework Flask. The styling was done with the help of additional Bootstrap templates (https://startbootstrap.com/previews/clean-blog), Bootstrap 5, CSS, and JS. The main features are:</br>
- multi-page website with an interactive navigation bar,</br>
- dynamically generated blogpost pages with full screen titles,</br>
- fully mobile responsive with an adaptive navigation bar,</br>
- fully functional contact form (POST request - Flask) that will send an email form to the specified email receiver.</br>

The data for each post is stored using an API (https://www.npoint.io/), which converts our data into an easily accessible API endpoint. The blog website makes a request to this endpoint and retrieves a JSON data representation for each post, which is later rendered into HTML.

# 05_Flask_WTForms
This is an example project in Flask showing how to start using the Flask-WTF, which gives a number of benefits over the simple HTML form.
With easy form validation, it makes sure that the user is entering the data in the required format and fields, with less code, and build in CSRF Protection (CSRF stands for Cross Site Request Forgery).
This website consists of the main page with a login button. After pressing it, the user gets transferred to the login page,
where an email and password are required. The "secret" is revealed to the user after entering the correct email address and password; otherwise, the user is presented with an access denied website.
Main Features include: Inheriting Templates Using Jinja2, Jinja2 - templates, Flask-Bootstrap, Flask-WTF, WTForms, Forms validation.
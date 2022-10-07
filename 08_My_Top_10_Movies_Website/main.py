from flask import Flask, url_for, redirect, render_template, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from movie_manager import MovieSeeker
from env_variables import FLASK_SECRET_KEY, THEMOVIEDB_API_KEY
from forms import AddMovieForm, RateMovieForm

# creating a object for searching for the movies with the help of 
# https://developers.themoviedb.org/3/search/search-movies API
movie_seeker = MovieSeeker(the_moviedb_api_key=THEMOVIEDB_API_KEY)


# creating flask object and its variables
app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_SECRET_KEY
# adding flask-bootstrap
Bootstrap(app)

# database uri
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collection.db'
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# creating pointer to the database
db = SQLAlchemy(app)

# creating the book model for database
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)
    
    #Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<User {self.title}>'

# create the initial database from models.py
# should only run once to create your database
db.create_all()

# just and example how to inject data into the database
# addin an entry to the database
# just once - after it nedds to be commented
# to get some data into our database
# if you run this code more than once you will get the following error
# sqlalchemy.exc.IntegrityError: (sqlite3.IntegrityError)
#
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()

# generator helper for ranking
def generator(start: int):
    """
    generator helper for creating increamental numbers from start
    """
    num = start
    while True:
        yield num
        num += 1

# all Flask routes below
# main route - home - /
@app.route("/")
def home():
    # getting all the movies from the database
    # all_movies = db.session.query(Movie).all()
    # all_movies = Movie.query.all()
    # ordering by the movie rating
    all_movies = Movie.query.order_by(Movie.rating).all()

    # updating the database with the ranking 
    counter_ranking = generator(start=1)
    for movie in all_movies[::-1]:
        movie.ranking = next(counter_ranking)
    # save the changes to database
    db.session.commit()

    return render_template("index.html", movies=all_movies)

# update databse - update movie route
@app.route("/update", methods = ["GET", "POST"])
def update():
    # creating our form
    form = RateMovieForm()
    movie_id = request.args.get('id',None)

    # if the url containad the desired key word , id
    if movie_id:
        selected_movie = Movie.query.get(movie_id)

        # if a movie with the desired id exists
        if selected_movie:
            
            # if form is validated then it has to be the post request !
            if form.validate_on_submit():
                
                # updating the database
                selected_movie.rating = float(form.rating.data)
                selected_movie.review = form.review.data
                # saving the changes to the database
                db.session.commit()

                #  redirecting back to home
                return redirect(url_for("home"))
            
            return render_template("edit.html", form=form, movie=selected_movie)

    return render_template("edit.html", form=form)


# delete entry in databse - delete movie route
@app.route("/delete")
def delete_movie():

    # try to get the id of the movie
    movie_id = request.args.get('id',None)

    # if the url containad the desired key word , id
    if movie_id:
        selected_movie = Movie.query.get(movie_id)

        # if a movie with the desired id exists
        if selected_movie:
        
            # deleting the movie fromt he databse
            db.session.delete(selected_movie)
            db.session.commit() 

            #  redirecting back to home
            return redirect(url_for("home"))



# adding a movie - list of movies from the api
@app.route("/get_movies", methods = ["GET", "POST"])
def get_movies():
    # creating our form
    form = AddMovieForm()

    # if form is validated then it has to be the post request !
    if form.validate_on_submit():

        movie_title = form.title.data
        movies_dict = movie_seeker.get_data_movies(title=movie_title)
        
        if movies_dict:
            return render_template("select.html", movies=movies_dict)

    return render_template("add.html", form=form)


# update databse with the movie found from the api
@app.route("/add_movie")
def add_movie_database():

    # try to get the id of the movie
    movie_id = request.args.get('id',None)

    if movie_id:

        # getting detail data from the api
        detail_movie_data = movie_seeker.get_data_movie_detail(int(movie_id))

        # updating the databse
        new_movie = Movie(
            title=detail_movie_data['title'],
            year=detail_movie_data['release_date'].split('-')[0],
            description=detail_movie_data['overview'],
            # rating=7.3,
            # ranking=10,
            # review="My favourite character was the caller.",
            img_url=detail_movie_data['poster_path'],
        )
        db.session.add(new_movie)
        db.session.commit()

        # checking the id of the movie from the database
        selected_movie = Movie.query.filter_by(title=detail_movie_data['title']).first()

        #  redirecting to updating the review and rating
        return redirect(url_for("update", id = selected_movie.id))



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

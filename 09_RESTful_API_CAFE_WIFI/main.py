from xmlrpc.client import boolean
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from env_variables import FLASK_SECRET_KEY
import random

# creating flask object and its variables
app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_SECRET_KEY


##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# creating pointer to the database
db = SQLAlchemy(app)



##Cafe TABLE Configuration
# this is how our databse looks like represented with SQLAlchemy 
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


    # converting data to dictionary for serialization with jsonify
    def to_dict(self):
        # Dictionary Comprehension - for Loop through each column in the data record
        #     # Create a new dictionary entry;
        #     # where the key is the name of the column
        #     # and the value is the value of the column
        return {column.name: getattr(self,column.name) for column in self.__table__.columns}

# creates the table, but does not update existing tables
# db.create_all()


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
# GET is allowed by default on all routes
@app.route("/random")
def get_random_cafe():

    # return a random cafe from the database
    # db.session.query(Cafe).all()
    cafes = Cafe.query.all()
    random_cafe = random.choice(cafes)

    return jsonify(cafe=random_cafe.to_dict())
    # return jsonify(
    #     cafe = {
    #         # omiting the id from the response
    #         # "id" : random_cafe.id,     
    #         "name" : random_cafe.name, 
    #         "map_url" : random_cafe.map_url, 
    #         "img_url" : random_cafe.img_url, 
    #         "location" : random_cafe.location, 
            
    #         # Put some properties in a sub-category
    #         "amenities" : {
    #         "seats" : random_cafe.seats, 
    #         "has_toilet" : random_cafe.has_toilet, 
    #         "has_wifi" : random_cafe.has_wifi,
    #         "can_take_calls" : random_cafe.can_take_calls, 
    #         "coffee_price" : random_cafe.coffee_price, 
    #         "has_sockets" : random_cafe.has_sockets, 
    #         }
    #     },
    # )


# return all cafes
@app.route("/all")
def get_all_cafes():
    
    cafes = Cafe.query.all()
    list_cafes = [cafe.to_dict() for cafe in cafes]

    return jsonify(cafes=list_cafes)



# search fro a cafee in a specific location
# ex. /search?loc=Peckham
@app.route("/search")
def search_cafe_by_location():
    
    requested_loction = request.args.get('loc', None)
    if requested_loction:
        requested_cafe =  Cafe.query.filter_by(location = requested_loction).first()
        
        if requested_cafe:
            return jsonify(cafe=requested_cafe.to_dict())
                
    return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."})



## HTTP POST - Create Record
# search fro a cafee in a specific location
# ex. /search?loc=Peckham
@app.route("/add", methods=["POST"])
def add_cafe():
    
    new_cafe = Cafe(
        name = request.form.get('name'),
        map_url = request.form.get('map_url'),
        img_url = request.form.get('img_url'),
        location = request.form.get('location'),
        seats = request.form.get('seats'),
        has_toilet = bool(request.form.get('has_toilet')),
        has_wifi = bool(request.form.get('has_wifi')),
        has_sockets = bool(request.form.get('has_sockets')),
        can_take_calls = bool(request.form.get('can_take_calls')),
        coffee_price = request.form.get('coffee_price'),
    )

    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={"success": "Successfuly added the new cafe"})


## HTTP PUT/PATCH - Update Record
# /update-price/<cafe_id>
@app.route("/update/<int:cafe_id>", methods=["PATCH"])
def update_cafe_coffee_price(cafe_id):
    
    cafe_to_update = Cafe.query.get(cafe_id)

    if cafe_to_update:

        new_price = request.args.get('new_coffee_price', None)

        if new_price:
            cafe_to_update.coffee_price = new_price
            db.session.commit()

            ## Just add the code after the jsonify method. 200 = Ok
            return jsonify(success="Successfully updted the price.") , 200
        
        #404 = Resource not found
        return jsonify(error={"Not Found": "Sorry a new_coffee_price was not found in the given request."}) , 404

    #404 = Resource not found
    return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}) , 404


## HTTP DELETE - Delete Record
# /update-price/<cafe_id>
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    
    api_key = request.args.get("api-key",None)

    if api_key == "TopSecretAPIKey":

        cafe_to_delete = Cafe.query.get(cafe_id)

        if cafe_to_delete:

            db.session.delete(cafe_to_delete)
            db.session.commit()

            ## 200 = Ok - http status codes
            return jsonify(success="The cafe was successfully deleted.") , 200

        ## 404 = Resource not found - http status codes
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}) , 404

    ## 403 =  Forbidden - http status codes
    return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}) , 403






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

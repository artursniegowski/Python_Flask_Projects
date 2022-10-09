import csv
from flask import Flask, url_for, redirect, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SelectField ,StringField, SubmitField, URLField
from wtforms.validators import DataRequired, URL

# env variables !
from dotenv import load_dotenv
load_dotenv()
import os


################################################################################
## sensitive data ###
#####################
# user defined WTF_CSRF_SECRET_KEY !
# In order to generate the csrf token, you must have a secret key, this is 
# usually the same as your Flask app secret key. If you want to use another 
# secret key, config it.
# env variables ! - dont change here !
FLASK_SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
################################################################################

CAFE_DATA_FILE = 'cafe-data.csv'

app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_SECRET_KEY
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location_url = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    opening_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', 
                                choices=['✘','☕️'*1, '☕️'*2,'☕️'*3,'☕️'*4,'☕️'*5], 
                                validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Strength Rating', 
                                choices=['✘','💪'*1, '💪'*2,'💪'*3,'💪'*4,'💪'*5], 
                                validators=[DataRequired()])
    power_outlet_rating = SelectField('Power Socket Availability', 
                                        choices=['✘','🔌'*1, '🔌'*2,'🔌'*3,'🔌'*4,'🔌'*5],
                                        validators=[DataRequired()])
    submit = SubmitField('Submit')



# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',  methods=['GET', 'POST'])
def add_cafe():
    file_name = CAFE_DATA_FILE
    form = CafeForm()
    # if form is validated then it has to be the post request !
    if form.validate_on_submit():

        # data_to_write = f"\n{form.cafe.data},{form.location_url.data},{form.opening_time.data},{form.closing_time.data},{form.coffee_rating.data},{form.wifi_rating.data},{form.power_outlet_rating.data}"   
        data_to_write = [
            form.cafe.data,
            form.location_url.data,
            form.opening_time.data,
            form.closing_time.data,
            form.coffee_rating.data,
            form.wifi_rating.data,
            form.power_outlet_rating.data
        ]   

        try:
            # with open(file_name, mode='a', encoding="utf8") as csv_file:
                # csv_file.write(data_to_write)
            with open(file_name, mode='a', newline='', encoding="utf8") as csv_file:
                csv_data_writer = csv.writer(csv_file, delimiter=',')
                csv_data_writer.writerow(data_to_write)

        except FileNotFoundError:
            print(f"Error: '{file_name}' was not found!!")
            print(f"Is the {file_name} in the right directory?")

        return redirect(url_for('cafes'))

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    list_of_rows_cafes = []
    file_name = CAFE_DATA_FILE
    try:
        with open(file_name, newline='', encoding="utf8") as csv_file:
            csv_data = csv.reader(csv_file, delimiter=',')
            for row in csv_data:
                list_of_rows_cafes.append(row)
    except FileNotFoundError:
        print(f"Error: '{file_name}' was not found!!")
        print(f"Is the {file_name} in the right directory?")

    return render_template('cafes.html', cafes=list_of_rows_cafes)




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

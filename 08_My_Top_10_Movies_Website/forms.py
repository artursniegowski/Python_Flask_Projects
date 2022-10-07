# forms for submiting data
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange

# form for updating a movie
class RateMovieForm(FlaskForm):
    rating = FloatField('Your Rating Out of 10 e.g. 7.5', validators=[DataRequired(), NumberRange(min=0, max=10)])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')


# form for adding a movie
class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')
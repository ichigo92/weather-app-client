from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CityForm(FlaskForm):
    """
    Form for admin to add or edit a city
    """
    city = StringField('City Name', validators = [DataRequired()])
    submit = SubmitField('Add City')
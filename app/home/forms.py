from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired

class AddCityForm(FlaskForm):

	city = StringField('City Name', validators = [DataRequired()])
	submit = SubmitField('Submit')
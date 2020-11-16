from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField
from wtforms.validators import DataRequired



class Slider(FlaskForm)
picture = FileField('Slider Picture', validators=[FileAllowed(['jpg', 'png'])])
submit = SubmitField('Create')
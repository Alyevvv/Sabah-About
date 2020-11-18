from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import SubmitField
from wtforms.validators import DataRequired



class SliderForm(FlaskForm):
    picture = FileField(validators=[FileAllowed(['jpg', 'png'])])

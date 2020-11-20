from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField ,SubmitField, TextAreaField
from wtforms.validators import DataRequired



class SliderForm(FlaskForm):
    picture =  FileField(validators=[FileRequired()])



class NewsForm(FlaskForm):
    title = StringField('Xəbərin adı', validators=[DataRequired()])
    image = FileField('Şəkil', validators=[FileRequired()])
    text = TextAreaField('Məqalə', validators=[DataRequired()])
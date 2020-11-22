from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField ,SubmitField, TextAreaField, DateTimeField
from wtforms.validators import DataRequired



class SliderForm(FlaskForm):
    url = StringField('Link əlavə edin', validators=[DataRequired()])
    picture =  FileField('Şəkil əlavə edin',validators=[FileRequired()])



class NewsForm(FlaskForm):
    title = StringField('Xəbərin adı', validators=[DataRequired()])
    image = FileField('Şəkil', validators=[FileRequired()])
    text = TextAreaField('Məqalə', validators=[DataRequired()])




class EventForm(FlaskForm):
    title = StringField('Tədbirin adı', validators=[DataRequired()])
    image = FileField('Şəkil', validators=[FileRequired()])
    text = TextAreaField('Məqalə', validators=[DataRequired()])


class AnnouncementForm(FlaskForm):
    title = StringField('Elanın adı', validators=[DataRequired()])
    date = DateTimeField('Elanın bitmə tarixi', format= '%Y-%m-%d',  validators=[DataRequired()])
    image = FileField('Şəkil', validators=[FileRequired()])
    text = TextAreaField('Məqalə', validators=[DataRequired()])
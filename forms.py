from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms.validators import FileRequired
from flask_wtf.file import FileRequired, FileAllowed


class SearchForm(FlaskForm):
    searched = FileField('Select from your computer', validators=[FileRequired(), FileAllowed(['pdf'], "Only pdf format allowed")])
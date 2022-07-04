from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed



class UploadForm(FlaskForm):
    file = FileField(label = 'Select from your computer', validators=[FileRequired(), FileAllowed(['pdf'], "Only pdf format allowed")])
from wtforms import *
from flask_wtf import *
from flask_wtf.file import *

class UploadForm(FlaskForm):
    description = TextAreaField('description',[validators.InputRequired])
    photo = FileField('photo', [validators.DataRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images Only!')])
    csrf_token = csrf.CSRFProtect()

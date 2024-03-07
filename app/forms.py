from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField 
from wtforms.validators import InputRequired 
from flask_wtf.file import FileField, FileAllowed , FileRequired



class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


class UploadForm(FlaskForm):
    upload = FileField('Image Upload', validators=[
        FileRequired(message='Please select a file to upload.'),
        FileAllowed(['jpg', 'png'], message='Only JPG and PNG images are allowed.')
    ])

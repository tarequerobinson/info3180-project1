# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField , TextAreaField
# from wtforms.validators import InputRequired , DataRequired, Email
# from flask_wtf.file import FileField, FileAllowed , FileRequired
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, FloatField, PasswordField
from wtforms.validators import DataRequired, NumberRange , InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])


# class UploadForm(FlaskForm):
#     propertyTitle = StringField('Property Title', validators=[DataRequired()])
#     desc = StringField('Description', validators=[DataRequired()])
#     location = StringField('Location', validators=[DataRequired()])
#     propertyType = SelectField('Property Type', choices=[('residential', 'Residential'), ('commercial', 'Commercial')], validators=[DataRequired()])
#     bathrooms = IntegerField('Number of Bathrooms', validators=[NumberRange(min=0)])
#     price = FloatField('Price', validators=[NumberRange(min=0)])
#     upload = FileField('Image Upload', validators=[
#         FileRequired(message='Please select a file to upload.'),
#         FileAllowed(['jpg', 'png', 'jpeg'], message='Only JPG and PNG images are allowed.')
#     ])


class UploadForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    type = SelectField('Property Type', choices=[('home', 'Home'), ('apartment', 'Apartment')], validators=[DataRequired()])
    number_of_bedrooms= IntegerField('Number of Bedrooms', validators=[NumberRange(min=0)])
    number_of_bathrooms = IntegerField('Number of Bathrooms', validators=[NumberRange(min=0)])
    price = FloatField('Price', validators=[NumberRange(min=0)])
    photo = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png' , 'jpeg'], 'Images only!')
    ])




# class ContactForm(FlaskForm):
#     name = StringField('Name', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     subject = StringField('Subject', validators=[DataRequired()])
#     message = TextAreaField('Message', validators=[DataRequired()])

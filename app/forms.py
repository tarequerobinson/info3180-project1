from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, FloatField, PasswordField
from wtforms.validators import DataRequired, NumberRange , InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])




class UploadForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    type = SelectField('Property Type', choices=[('Home', 'Home'), ('Apartment', 'Apartment')], validators=[DataRequired()])
    number_of_bedrooms= IntegerField('Number of Bedrooms', validators=[NumberRange(min=0)])
    number_of_bathrooms = IntegerField('Number of Bathrooms', validators=[NumberRange(min=0)])
    price = FloatField('Price', validators=[NumberRange(min=0)])
    photo = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png' , 'jpeg'], 'Images only!')
    ])





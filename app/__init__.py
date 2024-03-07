from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  
from .config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

# Instantiate Flask-Migrate here
migrate = Migrate(app, db)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


def get_uploaded_images():
    upload_folder = app.config['UPLOAD_FOLDER']
    images = []
    for filename in os.listdir(upload_folder):
        if filename.endswith(('.jpg', '.png', '.jpeg')):
            images.append(filename)
    return images


from app import views

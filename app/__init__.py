from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate  
from .config import Config
from flask import url_for
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


# def get_uploaded_images():
#     upload_folder = app.config['UPLOAD_FOLDER']
#     images = []
#     for filename in os.listdir(upload_folder):
#         if filename.endswith(('.jpg', '.png', '.jpeg')):
#             images.append("uploads/" +filename)
#     print (images)
#     return images


def get_uploaded_images():
    rootdir = os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'])
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    images = []

    for subdir, _, files in os.walk(rootdir):
        for file in files:
            if any(file.lower().endswith(ext) for ext in valid_extensions):
                relative_path = os.path.relpath(os.path.join(subdir, file), rootdir)
                image_url = url_for('get_image', filename=relative_path)
                images.append(image_url)
    print(images)
    return images



from app import views

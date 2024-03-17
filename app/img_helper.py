import os
from models import Property

def get_uploaded_images():
    # upload_folder = app.config['UPLOAD_FOLDER']
    upload_folder = './uploads'
    # app.config['UPLOAD_FOLDER']

    images = []
    for filename in os.listdir(upload_folder):
        if filename.endswith(('.jpg', '.png')):
            images.append(filename)
    return images


def get_all_properties():
    # Assuming db is an instance of SQLAlchemy
    properties = Property.query.all()
    return properties

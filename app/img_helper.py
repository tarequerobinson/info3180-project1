import os

def get_uploaded_images():
    upload_folder = app.config['UPLOAD_FOLDER']
    images = []
    for filename in os.listdir(upload_folder):
        if filename.endswith(('.jpg', '.png')):
            images.append(filename)
    return images

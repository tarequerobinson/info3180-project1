import os
from app import app, db, login_manager , get_uploaded_images
from flask import render_template, request, redirect, url_for, flash, session, abort
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.utils import secure_filename
from app.models import UserProfile
from app.models import Property
# from app.img_helper import get_all_properties
 

from app.forms import LoginForm , UploadForm
# UploadForm
from werkzeug.security import check_password_hash
from flask import send_from_directory



###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/properties/create', methods=['GET', 'POST'])
# @login_required
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        # f.save(os.path.join(os.path.dirname(app.root_path),  'uploads', filename))

        uploads_folder = os.path.join(os.path.dirname(__file__), 'static', 'uploads')
        file_path = os.path.join(uploads_folder, filename)
        f.save(file_path)


        # Create a new Property instance using form data
        property_title = form.title.data
        description = form.description.data
        location = form.location.data
        property_type = form.type.data
        bathrooms = form.number_of_bathrooms.data
        bedrooms = form.number_of_bedrooms.data

        price = form.price.data
        image_path = filename  # Store just the filename, not the full path
        
        # Create a new Property instance and save it to the database
        property_instance = Property(property_title=property_title, description=description, location=location, property_type=property_type, bathrooms=bathrooms, price=price , image_path=image_path , bedrooms=bedrooms)
        db.session.add(property_instance)
        db.session.commit()
        
        # Flash success message and redirect
        flash('Property added successfully!', 'success')
        return redirect(url_for('home'))
    return render_template('upload.html', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Get the username and password values from the form.
        username = form.username.data
        password = form.password.data

        # Using your model, query database for a user based on the username
        # and password submitted. Remember you need to compare the password hash.
        # You will need to import the appropriate function to do so.
        user = UserProfile.query.filter_by(username=username).first()

        if user and check_password_hash(user.password , password):
            # Login the user
            login_user(user)

            # Remember to flash a message to the user
            flash('Login successful!', 'success')

            return redirect(url_for('upload'))  # Redirect to the home page
        else:
            # Invalid username or password
            flash('Invalid username or password', 'error')

    return render_template('login.html', form=form)

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(UserProfile).filter_by(id=id)).scalar()

###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404




@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/files')
# @login_required
def files():
    images = get_uploaded_images()
    return render_template('files.html', images=images)



@app.route('/logout')
def logout():
    # Check if the user is authenticated
    if current_user.is_authenticated:
        # Logout the user
        logout_user()
        # Flash a message to the user
        flash('You have been logged out successfully.', 'success')
    # Redirect the user to the home route
    return redirect(url_for('home'))


@app.route('/properties')
def display_properties():
    properties = Property.query.all()
    print (properties)
    return render_template('properties.html', properties=properties)


@app.route('/property/<int:id>')
def display_property(id):
    # Query the database to get the property by its ID
    property = Property.query.get(id)

    # If property doesn't exist, return 404 Not Found
    if property is None:
        abort(404)

    # Render the template and pass the property object to it
    return render_template('property.html', property=property)

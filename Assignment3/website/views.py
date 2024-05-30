from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/create_event')
def create_event():
    return render_template('eventCreate.html')

# Error handlers
@main_bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main_bp.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500



# from flask import Blueprint, render_template, url_for, redirect, flash, request
# from .forms import EventForm
# from .models import Event
# from . import db
# from werkzeug.utils import secure_filename
# import os

# main_bp = Blueprint('main', __name__)

# @main_bp.route('/')
# def index():
#     return render_template('index.html')

# #create event 
# @main.route('/create-event', methods=['GET', 'POST'])
# def create_event():
#     form = EventForm()
#     if form.validate_on_submit():
#         file = form.image.data
#         filename = secure_filename(file.filename)
#         file.save(os.path.join(current_app.config['UPLOAD_FOLDER'],filename))
        
#         event = Event(title=form.title.data, description=form.description.data, data=form.date.data, image_url=filename)
#         db.session.add(event)
#         db.session.commit()
#         flash('Your event has been created!', 'success')
#         return redirect(url_for('main.home'))
#     return render_template('eventCreate.html', form=form)
        
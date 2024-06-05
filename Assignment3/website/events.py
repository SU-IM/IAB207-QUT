from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Event
from .forms import EventsForm
from . import db
import os
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user

events_bp = Blueprint('events', __name__, url_prefix='/events')

@events_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    print('Method type: ', request.method)
    form = EventsForm()
    
    if request.method == 'POST':
        form.state.choices = [(state, state) for state in get_states(form.country.data)]
        form.city.choices = [(city, city) for city in get_cities(form.state.data)]
        
        if form.validate_on_submit():
            print('Form validated successfully')
            try:
                db_file_path = check_upload_file(form)
                print(f'File uploaded to {db_file_path}')
                event = Event(
                    title=form.title.data,
                    startdate=form.startdate.data,
                    enddate=form.enddate.data,
                    performancetime=form.performancetime.data,
                    ticketopendate=form.ticketopendate.data,
                    ticketclosedate=form.ticketclosedate.data,
                    ticketprice=form.ticketprice.data,
                    numberofticket=form.numberofticket.data,
                    description=form.description.data,
                    about=form.about.data,
                    country=form.country.data,
                    state=form.state.data,
                    city=form.city.data,
                    detailed_location=form.detailed_location.data,
                    image=db_file_path
                    user_id=current_user
                )
                db.session.add(event)
                db.session.commit()
                flash('Successfully created new event!', 'success')
                return redirect(url_for('events.create'))
            except Exception as e:
                print(f'Error creating event: {e}')
                flash('Error creating event', 'danger')
        else:
            print('Form validation failed')
            print(form.errors)
    else:
        # GET 요청의 경우 기본 선택지를 설정합니다.
        form.state.choices = [('','Choose region...')]
        form.city.choices = [('','Choose city/state...')]
        
    return render_template('events/create.html', form=form)

def get_states(country):
    regions = {
        "USA": ["California", "Texas"],
        "Canada": ["Ontario", "Quebec"],
        "UK": ["England", "Scotland", "Wales", "Northern Ireland"],
        "AU": ["New South Wales", "Victoria", "Queensland"],
        "SouthKorea": ["Seoul", "Busan", "Incheon", "Daegu"]
    }
    return regions.get(country, [])

def get_cities(state):
    cities = {
        "California": ["Los Angeles", "San Francisco"],
        "Texas": ["Houston", "Austin"],
        "New South Wales": ["Sydney"],
        "Victoria": ["Melbourne"],
        "Queensland": ["Brisbane"],
        "Seoul": ["Gangnam-gu", "Jongno-gu"],
        "Busan": ["Haeundae", "Seo-gu"],
        "Incheon": ["Yeonsu-gu", "Namdong-gu"],
        "Daegu": ["Jung-gu", "Suseong-gu"],
        "England": ["London", "Manchester"],
        "Scotland": ["Edinburgh", "Glasgow"],
        "Wales": ["Cardiff", "Swansea"],
        "Northern Ireland": ["Belfast", "Derry"]
    }
    return cities.get(state, [])

def check_upload_file(form):
    try:
        fp = form.image.data
        filename = secure_filename(fp.filename)
        BASE_PATH = os.path.dirname(__file__)
        upload_path = os.path.join(BASE_PATH, 'static/img', filename)
        db_upload_path = f'/static/img/{filename}'
        fp.save(upload_path)
        return db_upload_path
    except Exception as e:
        print(f'Error uploading file: {e}')
        return None

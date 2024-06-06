# user.py
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Event, Booking
from . import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/userhistory')
@login_required
def userhistory():
    created_events = Event.query.filter_by(user_id=current_user.id).all()
    booked_events = db.session.query(Event).join(Booking).filter(Booking.user_id == current_user.id).all()
    return render_template('userhistory.html', created_events=created_events, booked_events=booked_events)

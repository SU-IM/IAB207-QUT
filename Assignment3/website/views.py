from flask import Blueprint, render_template, url_for, redirect, flash, request, jsonify
from .models import Event
from datetime import datetime
from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    events = Event.query.all()
    return render_template('index.html', events=events, Event=Event)

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

@main_bp.route('/api/events', methods=['GET'])
def get_events():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 6, type=int)
    events = Event.query.order_by(Event.startdate.asc()).paginate(page=page, per_page=per_page, error_out=False)
    event_data = [{'id': event.id, 'title': event.title, 'startdate': event.startdate.strftime('%B %d, %Y'), 'city': event.city, 'state': event.state, 'country': event.country, 'description': event.description, 'image': event.image} for event in events.items]
    return jsonify({'events': event_data, 'has_next': events.has_next})

@main_bp.route('/search', methods=['GET'])
def search():
    query = request.args.get('search')
    place = request.args.get('place')
    date = request.args.get('date')

    filters = []
    if query:
        filters.append((Event.title.ilike(f'%{query}%')) | (Event.description.ilike(f'%{query}%')))
    if place:
        filters.append((Event.city.ilike(f'%{place}%')) | (Event.state.ilike(f'%{place}%')) | (Event.country.ilike(f'%{place}%')))
    if date:
        try:
            date_obj = datetime.strptime(date, '%Y-%m-%d').date()
            filters.append(db.func.date(Event.startdate) == date_obj)
        except ValueError:
            print(f"Invalid date format: {date}")

    if filters:
        events = Event.query.filter(*filters).all()
    else:
        events = Event.query.all()

    event_data = [{'id': event.id, 'title': event.title, 'startdate': event.startdate.strftime('%B %d, %Y'), 'city': event.city, 'state': event.state, 'country': event.country, 'description': event.description, 'image': event.image} for event in events]

    return jsonify({'events': event_data})
        
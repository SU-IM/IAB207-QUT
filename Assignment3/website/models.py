from . import db
from flask_login import UserMixin
import string
import random

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True, nullable=False)
    email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)    
    
    events = db.relationship('Event', backref='user')
    booking = db.relationship('Booking', backref='user')
    
    def __repr__(self):
        return f"Name: {self.username}"

# create event
class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(400))
    title = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    detailed_location = db.Column(db.String(100), nullable=False)
    startdate = db.Column(db.DateTime, nullable=False)
    enddate = db.Column(db.DateTime, nullable=False)
    performancetime = db.Column(db.Integer, nullable=False)
    ticketopendate = db.Column(db.DateTime, nullable=False)
    ticketclosedate = db.Column(db.DateTime, nullable=False)
    ticketprice = db.Column(db.Integer, nullable=False)
    numberofticket = db.Column(db.Integer, nullable=False)
    ticketlimit = db.Column(db.Integer)
    description = db.Column(db.Text(400), nullable=False)
    about = db.Column(db.Text(1200), nullable=False)    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) # author of events
    
    bookings = db.relationship('Booking', backref='event', lazy=True)
    
    def __repr__(self):
        return f"Title: {self.title}"

def generate_random_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(8))
    
#Booking
class Booking(db.Model):
    __tablename__ = 'booking'
    id = db.Column(db.String(8), primary_key=True, default=generate_random_id)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    contactemail = db.Column(db.String(100), nullable=False)
    contactnumber = db.Column(db.String(100), nullable=False)
    numberoftickets = db.Column(db.Integer, nullable=False)
    bookingdate = db.Column(db.DateTime, nullable=False)
    paymentmethod = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return f"<Booking: {self.id}>"
    
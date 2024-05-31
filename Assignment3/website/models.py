from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True, nullable=False)
    email = db.Column(db.String(100), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Name: {self.username}"

class Event(db.Model, UserMixin):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(400))
    title = db.Column(db.String(100), nullable=False)
    #location = db.Column(db.String(100), nullable=False)
    startdate = db.Column(db.DateTime, nullable=False)
    enddate = db.Column(db.DateTime, nullable=False)
    performancetime = db.Column(db.Integer, nullable=False)
    ticketopendate = db.Column(db.DateTime, nullable=False)
    ticketclosedate = db.Column(db.DateTime, nullable=False)
    ticketprice = db.Column(db.Integer, nullable=False)
    numberofticket = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    about = db.Column(db.Text, nullable=False)    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) # author of events
    
    def __repr__(self):
        return f"Title: {self.title}"
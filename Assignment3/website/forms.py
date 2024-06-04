from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, SelectField, IntegerField,
from wtforms.validators import InputRequired, Email, EqualTo, DataRequired
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG', 'JPG', 'JPEG', 'png', 'jpg', 'jpeg'}

# creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
    password=PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

#User register
class RegisterForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    
    #linking two fields - password should be equal to data entered in confirm
    password = PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    #submit button
    submit = SubmitField("Register")

#event create    
class EventsForm(FlaskForm):
    image = FileField('Thumbnail image', validators=[
        FileRequired(message='Image cannot be empty'),
        FileAllowed(ALLOWED_FILE, message='Only supports PNG, JPG, JPEG, png, jpg, jpeg')])
    title = StringField('Event Name', validators=[InputRequired()])
    #location = StringField('Location', validators=[InputRequired()])
    startdate = StringField('Start Date', validators=[InputRequired()])
    enddate = StringField('End Date', validators=[InputRequired()])
    performancetime = StringField('Performance Time', validators=[InputRequired()])
    ticketopendate = StringField('Ticket Opening Date', validators=[InputRequired()])
    ticketclosedate = StringField('Ticket Closing Date', validators=[InputRequired()])
    ticketprice = StringField('Ticket Price', validators=[InputRequired()])
    numberoftickets = StringField('Total Number of Tickets', validators=[InputRequired()])
    description = TextAreaField('Short Description',
            validators=[InputRequired()])
    about = TextAreaField('About this event', validators=[InputRequired()])
    
    submit = SubmitField("Create")
    
#booking page
# class BookingForm(FlaskForm):
#     event_id = SelectField('Event', coerce=int, validators={DataRequired()})
#     ticket_number = IntegerField('Number of Tickets', validators=[DataRequired()])
#     name = StringField('Your Name', validators=[DataRequired()])
#     contact = StringField('Contact Number', validators=[DataRequired()])
#     booking_date = SelectField('Booking Date', validators=[DataRequired()])
#     payment_method = SelectField('Payment Method', choices=['PayPal', 'Credit Card'], validators=[DataRequired()]) #still have to fix
    
#     submit = SubmitField("Book Now")
    
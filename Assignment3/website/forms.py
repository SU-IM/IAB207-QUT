from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, SelectField, IntegerField, DateTimeLocalField
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
    startdate = DateTimeLocalField('Start Date', validators=[InputRequired()])
    enddate = DateTimeLocalField('End Date', validators=[InputRequired()])
    performancetime = StringField('Performance Time', validators=[InputRequired()])
    ticketopendate = DateTimeLocalField('Ticket Opening Date', validators=[InputRequired()])
    ticketclosedate = DateTimeLocalField('Ticket Closing Date', validators=[InputRequired()]) 
    ticketprice = StringField('Ticket Price', validators=[InputRequired()])
    numberofticket = IntegerField('Total Number of Tickets', validators=[InputRequired()])
    ticketlimit = IntegerField('Set a limit on the number of tickets reserved at one time')
    description = TextAreaField('Short Description',
            validators=[InputRequired()])
    about = TextAreaField('About this event', validators=[InputRequired()])
    country = SelectField('Country', choices=[('USA', 'USA'), ('Canada', 'Canada'), ('UK', 'United Kingdom'), ('AU', 'Australia'), ('SouthKorea', 'South Korea')], validators=[DataRequired()])
    state = SelectField('State', choices=[], validators=[DataRequired()])
    city = SelectField('City', choices=[], validators=[DataRequired()])
    detailed_location = StringField('Detailed Location', validators=[DataRequired()])
    submit = SubmitField("Create")
    
#booking page

class BookingForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    numberoftickets = IntegerField('Number of Tickets', validators=[DataRequired()])
    contactemail = StringField('Contact Email', validators=[DataRequired()])
    contactnumber = StringField('Contact Number', validators=[DataRequired()])
    paymentmethod = SelectField('Payment Method', choices=[('PayPal', 'PayPal'), ('Credit Card', 'Credit Card')], validators=[DataRequired()])
    
    submit = SubmitField("Book Now")
    
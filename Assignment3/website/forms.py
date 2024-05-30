from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

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
    
    
    
# from flask_wtf import FlaskForm
# from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
# from wtforms.validators import InputRequired, Length, Email, EqualTo, DataRequired
# from flask_wtf.file import FileField, FileAllowed
# from wtforms import StringField, TextAreaField, SubmitField, DateTimeField

# # creates the login information
# class LoginForm(FlaskForm):
#     user_name=StringField("User Name", validators=[InputRequired('Enter user name')])
#     password=PasswordField("Password", validators=[InputRequired('Enter user password')])
#     submit = SubmitField("Login")

#  # this is the registration form
# class RegisterForm(FlaskForm):
#     user_name=StringField("User Name", validators=[InputRequired()])
#     email = StringField("Email Address", validators=[Email("Please enter a valid email")])
#     # linking two fields - password should be equal to data entered in confirm
#     password=PasswordField("Password", validators=[InputRequired(),
#                   EqualTo('confirm', message="Passwords should match")])
#     confirm = PasswordField("Confirm Password")

#     # submit button
#     submit = SubmitField("Register")
    
# # create the event form
# class EventForm(FlaskForm):
#     title = StringField('Title', validators=[DataRequired()])
#     description = TextAreaField('Description', validators=[DataRequired()])
#     date = DateTimeField('Date', format='%Y-%m-%d %H:%M:%S', validators=[DataRequired()])
#     image = FileField('Image', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])
#     sumbmit = SubmitField('Create Event')
    
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import datetime

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    Bootstrap5(app)
    bcrypt = Bcrypt(app)

    app.secret_key = 'somesecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///website.sqlite'
    db.init_app(app)
    
    UPLOAD_FOLDER = '/static/img'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
       return db.session.scalar(db.select(User).where(User.id == user_id))

    from . import views
    app.register_blueprint(views.main_bp)
    from . import events
    app.register_blueprint(events.destbp)
    from . import auth
    app.register_blueprint(auth.auth_bp)
    
    # this creates a dictionary of variables that are available
    # to all html templates
    @app.context_processor
    def get_context():
      year = datetime.datetime.today().year
      return dict(year=year)

    return app


# # import flask - from 'package' import 'Class'
# from flask import Flask 
# from flask_bootstrap import Bootstrap5
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager
# from .views import main as main_blueprint

# db = SQLAlchemy()

# # create a function that creates a web application
# # a web server will run this web application
# def create_app():
  
#     app = Flask(__name__)  # this is the name of the module/package that is calling this app
#     # Should be set to false in a production environment
#     app.debug = True
#     app.secret_key = 'somesecretkey'
#     # set the app configuration data 
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sitedata.sqlite'
#     app.config['UPLOAD_PATH'] = 'path/to/upload/directory' # Add the uplaod path
    
   
#     # initialise db with flask app
#     db.init_app(app)

#     Bootstrap5(app)
    
#     # initialise the login manager
#     login_manager = LoginManager()
    
#     # set the name of the login function that lets user login
#     # in our case it is auth.login (blueprintname.viewfunction name)
#     login_manager.login_view = 'auth.login'
#     login_manager.init_app(app)

#     # create a user loader function takes userid and returns User
#     # Importing inside the create_app function avoids circular references
#     from .models import User
#     @login_manager.user_loader
#     def load_user(user_id):
#        return db.session.scalar(db.select(User).where(User.id==user_id))

#     from . import views
#     app.register_blueprint(main_blueprint)

#     from .auth import auth as auth_blueprint
#     app.register_blueprint(auth_blueprint)
    
#     return app
 
 
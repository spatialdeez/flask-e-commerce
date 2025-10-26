# This project experiments with Flask blueprints

from flask import Flask
import os
from dotenv import load_dotenv

def create_app():
    load_dotenv()
    app = Flask(__name__) # initalize flask
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') # get secret key from enviroment variable

    # get the routes
    from .auth import auth
    from .admin import admin
    from .views import views

    # register the blueprints
    app.register_blueprint(auth, url_prefix='/auth') 
    app.register_blueprint(admin, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')

    return app # start website
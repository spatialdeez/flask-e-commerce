from flask import Flask
import os
from dotenv import load_dotenv

def create_app():
    load_dotenv()
    app = Flask(__name__) # initalize flask
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') # get secret key from enviroment variable

    return app # start website
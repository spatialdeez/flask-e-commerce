# authentication
from flask import Blueprint

auth = Blueprint('auth', __name__) 

# Log in page
@auth.route('/login') # route to the paage
def login():
    return 'login test page'

# Sign up page
@auth.route('/sign_up') # route to the page
def sign_up():
    return 'signup test page'
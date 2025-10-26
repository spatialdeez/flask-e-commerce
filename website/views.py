from flask import Blueprint

views = Blueprint('views', __name__) # create the file as a file containing multiple endpoints or URLs


# Create homepage
@views.route('/') # decorator that states the route and directory of the webpage
def homepage():
    return 'Homepage test'
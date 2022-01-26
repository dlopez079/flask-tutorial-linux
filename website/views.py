from flask import Blueprint

# We are going to define that this is a blueprint
views = Blueprint('views', __name__) 

# Define the root view or index
# Decorator along with address then you define the function.
@views.route('/')
def home():
    return "<h1>TEST</h1>"
from flask import Blueprint

# We are going to define that this is a blueprint
auth = Blueprint('auth', __name__) 

# Define the login route
# Decorator along with address then you define the function.
@auth.route('/login')
def login():
    return "<p>Login</p>"

# Define the login route
# Decorator along with address then you define the function.
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

# Define the login route
# Decorator along with address then you define the function.
@auth.route('/sign-up')
def signup():
    return "<p>Sign Up!</p>"
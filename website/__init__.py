from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'al;dkfhjka;dfja;dlfkja;dfj'

    # Let's tell the app that I inserted a blueprint for views.
    from .views import views

    return app
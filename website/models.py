from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# Created two tables.  One table is going to hold the notes and the to the other table is going to hold the user information. 
# The child table will be the notes table and that is where the foreign key will go as this is a one to many relationship. 

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

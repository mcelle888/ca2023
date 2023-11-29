
from setup import db, ma
from marshmallow import fields
# AUTHENTICATION

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable = False, unique = True)
    password = db.Column(db.String, nullable = False)
    is_admin = db.Column(db.Boolean, default = False)
# list of cards owned by the user
    cards = db.relationship('Card', back_populates = 'user')
    # user is from card.py in Card.Model, we're connecting the two 

# USER SCHEMA

class UserSchema(ma.Schema):
    cards = fields.List(fields.Nested('CardSchema', exclude = ['user'])) 
# wrap in fields.list above because we have multiple cards (a list of cards) linked to a user
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin', 'cards')
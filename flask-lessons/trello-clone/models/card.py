from setup import db, ma
from datetime import datetime
from marshmallow import fields

class Card(db.Model):
    # last step: we need to rename the table name to cards (plural)
    __tablename__ = 'cards'
# subclass db.model (inheritance)
# this is an object that represents a table in database

# first column is the primary key : serial id will automatically be made if primary key is declared
    id = db.Column(db.Integer, primary_key = True)

    # next column is the title:
    title = db.Column(db.String(100), nullable = False)
    # desciption
    description = db.Column(db.Text())
    # tracking status of a card
    status = db.Column(db.String(30), default = 'To do')
    # date created in date type
    date_created = db.Column(db.Date(), default = datetime.now().strftime("%Y-%m-%d"))

    # Foreign Key for relationship at the database level
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'), nullable = False)
    # object, user below can be any name doens't matter. This is an SQLAlchemy relationship: nests an instance of a related model into this one (here nests an instance of users in this model)
    user = db.relationship('User', back_populates = 'cards')
    # cards up here in populates is the cards in user.py class User model : cards = db.relationship

    comments = db.relationship('Comment', back_populates = 'card')



# Class to tell marshmallow which fields we want to serialise which is done through a "SCHEMA"
class CardSchema(ma.Schema):
    # Tell Marshmallow to nest a user schema instance when serializing
    user = fields.Nested('UserSchema', exclude = ['password'])
    comments = fields.Nested('CommentSchema', many = True, exclude = ['card'])

    class Meta:
        fields = ('id', 'title', 'description', 'status', 'date_created', 'user', 'comments' )
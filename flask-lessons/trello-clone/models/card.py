from setup import db, ma

class Card(db.Model):
    # last step: we need to rename the table name to cards (plural)
    __tablename__ = 'cards'
# subclass db.model (inheritance)
# this is an object that represents a table in database

# first column is the primary key : serial id will automatically be made if primary key is declared
    id = db.Column(db.Integer, primary_key = True)
    # next column is the title:
    title = db.Column(db.String(100))
    # desciption
    description = db.Column(db.Text())
    # tracking status of a card
    status = db.Column(db.String(30))
    # date created in date type
    date_created = db.Column(db.Date())

# Class to tell marshmallow which fields we want to serialise which is done through a "SCHEMA"
class CardSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'status', 'date_created')
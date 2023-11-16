from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

import json
from flask_marshmallow import Marshmallow


app = Flask(__name__)
# CREATE configurations (set up database uri in the config)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:spameggs123@localhost:5432/trello'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:spameggs123@127.0.0.1:5432/trello'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# psycopg2 is an adapter, next trello_dev is the user followed by the password, the port and finally the database name



# now we can create sql alchemt instance (must be after the config setting but before anything else like routes and error handling. So as early as possible but still after the config setting)

db = SQLAlchemy(app)
ma = Marshmallow(app)



# now we define models (we define and declare our columns in python as classes and the orm, when we call method eg get all the users, the orm takes care of sql and brings data to us to use in python)

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
    
    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'description': self.description, 'status': self.status, 'date_created': self.date_created}




# we've declared the class but now we need to define all the models we need. Once these declarations are done, to create the tables in the physical database, we need to call the create all method. What we're declaring here is a custom terminal command

@app.cli.command('db_create')
def db_create():
    # drop here so that when we want to update, we will rewrite. So we will drop everything before recreating. This was we guarantee the database is clean before we seed
    db.drop_all()
    db.create_all()
    print('Created tables')

# Seeding a database: inserting some test data for development purposes into our database (So we have data to work with)
@app.cli.command('db_seed')
def db_seed():
    cards = [
    Card(
        title = 'Start of project',
        description = 'Stage 1 - Create ERD',
        status = 'Done',
        date_created = date.today()
        ),
    Card(
        title = 'QRM Queries',
        description = 'Stage 2 - Implement CRUD queries',
        status = 'In Progress',
        date_created = date.today()
    ),
    Card(
        title = 'Marshmallow',
        description = 'Stage 3 - Implement JSONify od models',
        status = 'In Progress',
        date_created = date.today()
    ),
    ]




# 'session' creates a database transaction: 
    db.session.add_all(cards)
    # now we must commit after writing all the edits
    db.session.commit()
    print('Database seeded')

# We've created an instance in memory (RAM) but we havent put it into the database yet (wont do it automatically because in some instances, we may want to do other things before commiting to database) So how do we commit to the database? We add in line 48. 



# QUERY
@app.route('/cards')
def all_cards():
    # select & from cards is what we're looking for
    # stmt = db.select(Card)

    # if you want to be specific so in this case the first card:
    # stmt = db.select(Card).limit(1)

    # select more specific like the where statement in sql
    stmt = db.select(Card).where(Card.id < 3)

    # select cards that are not done AND card id is greater than 2
    # stmt = db.select(Card).where(Card.status != 'Done', cards.id > 2)

    # To do OR, we pass the entire thing to db.or_ which will now interpret the , as an OR
    # stmt = db.select(Card).where(db.or_(Card.status != 'Done', cards.id > 2))

    # SORTING
    # Sorted ascending by card title by adding the .order_by
    # stmt = db.select(Card).where(Card.id < 3).order_by(Card.title)
    # # descending order
    # stmt = db.select(Card).where(Card.id < 3).order_by(Card.title.desc())

    # scalars method telle alchemy to execute the statement and creates instances of the class for us
    cards = db.session.scalars(stmt).all()
# if you not iterating, you need to add .all to the above^
    # print(cards.all())

    # iterate to get each card
    # for card in cards:
    #     print(card)
    #     # more useful info:
    #     print(card.__dict__)
    #     # more specific data:
    #     print(card.title)
    return 

    





@app.route('/')
def index():
    return 'Hello, World!'



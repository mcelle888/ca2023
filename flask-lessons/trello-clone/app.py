from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date
app = Flask(__name__)

# CREATE configurations
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:spameggs123@localhost:5432/trello'

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:spameggs123@127.0.0.1:5432/trello'

# now we can create sql alchemt instance (must be after the config setting but before anything else like routes and error handling. So as early as possible but still after the config setting)

db = SQLAlchemy(app)

# print(db) : was ued to check if alchemy instance was made

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
    # date created in date type
    date_created = db.Column(db.Date())

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
    card = Card(
        title = 'Start of project',
        description = 'Stage 1 - Create ERD',
        date_created = date.today()
    )

    db.session.add(card)
    # now we must commit after writing all the edits
    db.session.commit()
    print('Database seeded')

# We've created an instance in memory (RAM) but we havent put it into the database yet (wont do it automatically because in some instances, we may want to do other things before commiting to database) So how do we commit to the database? We add in line 48. 


@app.route('/')
def index():
    return 'Hello, World!'



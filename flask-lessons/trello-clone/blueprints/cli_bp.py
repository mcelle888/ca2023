from flask import Blueprint
from setup import db, bcrypt
from models.card import Card
from models.user import User
from datetime import date

# create an instance of a blueprint

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create')
def db_create():
    # drop here so that when we want to update, we will rewrite. So we will drop everything before recreating. This was we guarantee the database is clean before we seed
    db.drop_all()
    db.create_all()
    print('Created tables')

# Seeding a database: inserting some test data for development purposes into our database (So we have data to work with)
@db_commands.cli.command('seed')
def db_seed():


    users = [
        User(
            email = 'admin@spam.com',
            password = bcrypt.generate_password_hash ('spinynorman').decode('utf8'),
            is_admin = True
        ),
        User(
            name = 'John Cleese',
            email = 'cheese@spam.com',
            password = bcrypt.generate_password_hash ('tisbutascratch').decode('utf8'),
        )
    ]


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
    db.session.add_all(users)
    db.session.add_all(cards)
    # now we must commit after writing all the edits
    db.session.commit()
    print('Database seeded')
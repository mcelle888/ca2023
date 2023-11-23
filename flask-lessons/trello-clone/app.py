from flask import abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User, UserSchema
from setup import *
from models.card import Card, CardSchema
from blueprints.cli_bp import db_commands
from blueprints.users_bp import users_bp


app.register_blueprint(db_commands)

app.register_blueprint(users_bp)


def admin_required():
    user_email = get_jwt_identity()
    stmt = db.select(User).where(User.email == user_email)
    user = db.session.scalar(stmt)
    if not (user and user.is_admin):
        abort(401)


@app.errorhandler(401)
def unauthorized(err):
    return {'Error': 'You must be an administrator'}
# now we define models (we define and declare our columns in python as classes and the orm, when we call method eg get all the users, the orm takes care of sql and brings data to us to use in python)


# we've declared the class but now we need to define all the models we need. Once these declarations are done, to create the tables in the physical database, we need to call the create all method. What we're declaring here is a custom terminal command



# We've created an instance in memory (RAM) but we havent put it into the database yet (wont do it automatically because in some instances, we may want to do other things before commiting to database) So how do we commit to the database? We add in line 48. 



# QUERY
@app.route('/cards')
@jwt_required()
def all_cards():
    
    admin_required()
    # select & from cards is what we're looking for
    # stmt = db.select(Card)

    # if you want to be specific so in this case the first card: 
    # stmt = db.select(Card).limit(1)

    # select more specific like the where statement in sql
    # stmt = db.select(Card).where(Card.id < 3)

    # select cards that are not done AND card id is greater than 2
    # stmt = db.select(Card).where(Card.status != 'Done', cards.id > 2)

    # To do OR, we pass the entire thing to db.or_ which will now interpret the , as an OR
    # stmt = db.select(Card).where(db.or_(Card.status != 'Done', cards.id > 2))

    # SORTING
    # Sorted ascending by card title by adding the .order_by
    # stmt = db.select(Card).where(Card.id < 3).order_by(Card.title)]
    stmt = db.select(
        Card
    )
    # # descending order
    # stmt = db.select(Card).where(db.or_(Card.status != 'Done', Card.id > 2)).order_by(Card.title.desc())

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
    return CardSchema(many = True).dump(cards)
# this converts it to a list of dictionaries (to primative python data types which are easily serialized to json which is done by flask)




@app.route('/')
def index():
    return 'Hello, World!'


# @app.errorhandler(IntegrityError)
# def integrity_error(err):
#     return {'error': str(err)}, 409
from flask import Blueprint, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from setup import db
from models.card import CardSchema, Card
from auth import admin_required

cards_bp = Blueprint('cards', __name__, url_prefix = '/cards')

@cards_bp.route('/')
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
    return CardSchema(many = True, exclude = ['user.cards']).dump(cards)
# this converts it to a list of dictionaries (to primative python data types which are easily serialized to json which is done by flask)


# Get one card / note this is is a singular instance so no plural for Card and no need for many = true

@cards_bp.route('/<int:id>')
@jwt_required()
def one_card(id):
    stmt = db.select(Card).filter_by(id = id) # .where(Card.id == id)
    card = db.session.scalar(stmt)
    if card:
        return CardSchema().dump(card)
    else:
        return {'error': 'card not found'}, 404
    
# Create a new card
@cards_bp.route('/', methods = ['POST'])
@jwt_required()
def create_card():
    admin_required()
    card_info = CardSchema(exclude = ['id', 'date_created']).load(request.json)
    card = Card(
        title = card_info['title'],
        description = card_info.get('description', ''),
        status = card_info.get('status','To Do'),
        user_id = get_jwt_identity()
    )
    # print(card.__dict__)
    db.session.add(card)
    db.session.commit()
    return CardSchema().dump(card), 201

# Update a card
@cards_bp.route('/<int:id>', methods = ['PUT', 'PATCH'])
@jwt_required()
def update_card(id):
    admin_required()
    card_info = CardSchema(exclude = ['id', 'date_created']).load(request.json)
    stmt = db.select(Card).filter_by(id = id)
    card = db.session.scalar(stmt)
    if card:
        card.title = card_info.get('title', card.title)
        card.description = card_info.get('description', card.description)
        card.status = card_info.get('status', card.status)
        db.session.commit()
        return CardSchema().dump(card)
    else:
        return {'error': 'Card not found'}, 404

# Delete a card
@cards_bp.route('/<int:id>', methods = ['DELETE'])
@jwt_required()
def delete_card(id):
    admin_required()
    stmt = db.select(Card).filter_by(id=id)
    card = db.session.scalar(stmt)
    if card:
        db.session.delete(card)
        db.session.commit()
        return {}, 200
    else:
        return {'error': 'Card not found'}, 404
    

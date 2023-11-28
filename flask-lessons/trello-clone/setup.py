from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from os import environ


app = Flask(__name__)
# CREATE configurations (set up database uri in the config)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:spameggs123@localhost:5432/trello'

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# psycopg2 is an adapter, next trello_dev is the user followed by the password, the port and finally the database name
app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')


# now we can create sql alchemt instance (must be after the config setting but before anything else like routes and error handling. So as early as possible but still after the config setting)

db = SQLAlchemy(app)
ma = Marshmallow(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# ERROR HANDLING

@app.errorhandler(401)
def unauthorized(err):
    return {'Error': 'You must be an administrator'}




# @app.errorhandler(IntegrityError)
# def integrity_error(err):
#     return {'error': str(err)}, 409
from setup import app
from blueprints.cli_bp import db_commands
from blueprints.users_bp import users_bp
from blueprints.cards_bp import cards_bp
# attatches the cli_bp module to this main app

app.register_blueprint(db_commands)
# attaches the routes in users_bp tp this main app
app.register_blueprint(users_bp)

#blueprint for cards
app.register_blueprint(cards_bp)


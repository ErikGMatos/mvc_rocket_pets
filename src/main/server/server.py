from flask import Flask
from flask_cors import CORS

from src.main.routes.pets_routes import pet_routes_bp
from src.models.sqlite.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(pet_routes_bp)
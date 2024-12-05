from flask import Blueprint, jsonify

pet_routes_bp = Blueprint('pets_routes', __name__)


@pet_routes_bp.route("/pets", methods=["GET"])
def list_pets():
    return jsonify({"message": "Rota de listagem de pets"})

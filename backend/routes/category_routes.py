from flask import Blueprint, jsonify
from backend.services.category_service import CategoryService
from flask_jwt_extended import jwt_required

category_bp = Blueprint('category_bp', __name__)

@category_bp.route('/categories', methods=['GET'])
@jwt_required()
def get_all_categories():
    categories = CategoryService.get_all_categories()

    if categories != None:
        return jsonify([{'title': category.title} for category in categories]), 200
    else:
        return jsonify({"error": "Categories not found"}), 400
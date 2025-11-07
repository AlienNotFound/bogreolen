from flask import Blueprint, jsonify
from backend.services.author_service import AuthorService
from backend.DTOs.author_dto import AuthorDTO
from flask_jwt_extended import jwt_required

author_bp = Blueprint('author_bp', __name__)

@author_bp.route('/authors', methods=['GET'])
@jwt_required()
def get_all_books():
    authors = AuthorService.get_all_authors()

    if authors != None:
        return jsonify([AuthorDTO.to_dict(author) for author in authors]), 200
    else:
        return jsonify({"Error": "Authors not found"}), 400
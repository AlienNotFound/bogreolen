from flask import Blueprint, jsonify, request
from backend.models import Lists
from backend.services.list_service import ListService
from backend.services.track_service import TrackService
from flask_jwt_extended import jwt_required, get_jwt_identity

list_bp = Blueprint('list_bp', __name__)

@list_bp.route('/add-to-list', methods=['POST'])
@jwt_required()
def add_to_list():
    data = request.get_json()
    book_id = data.get('book_id')
    listname = data.get('listname')

    user_id = get_jwt_identity()

    if (ListService.get_list_by_user_and_book(user_id, book_id)):
        return jsonify({"Error": "This book is already on a list!"})

    result = ListService.add_to_list(user_id, book_id, listname)

    if isinstance(result, Lists):
        TrackService.track_book(user_id, book_id, False, 0, 0)
        return jsonify({"Success": f"\'{result.book.title}\' got added to {listname}"}), 200
    else:
        return jsonify({"Error": f"{result}"}), 400

@list_bp.route('/move-to-list/<id>', methods=['PUT'])
@jwt_required()
def move_to_list(id):
    data = request.get_json()
    listname = data.get('listname')

    user_id = get_jwt_identity()
    book_id = id

    result = ListService.move_to_list(user_id, book_id, listname)

    if isinstance(result, Lists):
        return jsonify({"Success": f"\'{result.book.title}\' got moved to {listname}"}), 200
    else:
        return jsonify({"Error": f"{result}"}), 400

@list_bp.route('/delete-from-lists/<id>', methods=['DELETE'])
@jwt_required()
def delete_book_from_lists(id):
    user_id = get_jwt_identity()
    book_id = id

    if ListService.get_list_by_user_and_book(user_id, book_id) == None:
        return jsonify({"Error": "Entry does not exist."}), 404
    
    result = ListService.delete_book_from_lists(user_id, book_id)

    if result == None:
        return jsonify({"Success": "Entry succesfully deleted!"}), 200
    else:
        return jsonify({"Error": f"{list}Could not delete entry."}), 500
    
@list_bp.route('/book-status/<book_id>', methods=['GET'])
@jwt_required()
def get_book_status(book_id):
    user_id = get_jwt_identity()

    result = ListService.get_book_status(user_id, book_id)

    if result:
        return jsonify({"book_id": book_id, "book_status": f"{result.listname.value}"}), 200
    else:
        return jsonify({"book_id": book_id, "book_status": None}), 200
    
@list_bp.route('/list_by_user/<user_id>')
def get_lists_by_user(user_id):
    result = ListService.get_lists_by_user(user_id)

    if result:
        return jsonify([{"user_id": user_id,
                        "book_id": r.book_id,
                        "title": r.book.title,
                        "book_status": f"{r.listname.value}"} for r in result]), 200
    else:
        return jsonify({"message": "User haven't added any books to a list."}), 200
    
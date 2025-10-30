from flask import Blueprint, jsonify, request
from backend.models import Liststb
from backend.services.list_service import ListService

list_bp = Blueprint('list_bp', __name__)

@list_bp.route('/add-to-list', methods=['POST'])
def add_to_list():
    data = request.get_json()
    book_id = data.get('bookid')
    listname = data.get('listname')

    user_id = 1

    if (ListService.get_list_by_user_and_book(user_id, book_id)):
        return jsonify({"Error": "This book is already on a list!"})

    result = ListService.add_to_list(user_id, book_id, listname)

    if isinstance(result, Liststb):
        return jsonify({"Success": f"\'{result.book.title}\' got added to {listname}"}), 200
    else:
        return jsonify({"Error": f"{result}"}), 400

@list_bp.route('/move-to-list/<id>', methods=['PUT'])
def move_to_list(id):
    data = request.get_json()
    listname = data.get('listname')

    userid = 1
    bookid = id

    result = ListService.move_to_list(userid, bookid, listname)

    if isinstance(result, Liststb):
        return jsonify({"Success": f"\'{result.book.title}\' got moved to {listname}"}), 200
    else:
        return jsonify({"Error": f"{result}"}), 400

@list_bp.route('/delete-from-lists', methods=['DELETE'])
def delete_book_from_lists():
    userid = 1
    bookid = 1

    if ListService.get_list_by_user_and_book(userid, bookid) == None:
        return jsonify({"Error": "Entry does not exist."}), 404
    
    result = ListService.delete_book_from_lists(userid, bookid)

    if result == None:
        return jsonify({"Success": "Entry succesfully deleted!"}), 200
    else:
        return jsonify({"Error": f"{list}Could not delete entry."}), 500
    
@list_bp.route('/book-status/<book_id>', methods=['GET'])
def get_book_status(book_id):
    userid = 1

    result = ListService.get_book_status(userid, book_id)

    if result:
        return jsonify({"bookid": book_id, "book_status": f"{result.listname.value}"}), 200
    else:
        return jsonify({"book_id": book_id, "book_status": None}), 200
    
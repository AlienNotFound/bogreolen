from flask import Blueprint, jsonify, request
from backend.models import Liststb
from backend.services.list_service import ListService

list_bp = Blueprint('list_bp', __name__)

@list_bp.route('/move-to-list', methods=['PUT'])
def move_to_list():
    data = request.get_json()
    listname = data.get('listname')

    userid = 1
    bookid = 1

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
from flask import Blueprint, jsonify, request
from backend.services.book_service import BookService

book_bp = Blueprint('book_bp', __name__)

@book_bp.route('/books', methods=['GET'])
def get_all_books():
    books = BookService.get_all_books()
    books_list = [dict(row._mapping) for row in books]

    if len(books_list) > 0:
        return jsonify([book for book in books_list]), 200
    else:
        return jsonify({"Error": "There was an error"}), 500
    
@book_bp.route('/book/<id>', methods=['GET'])
def get_books_by_id(id):
    book = BookService.get_book_by_id(id)

    if book != None:
        book_list = dict(book._mapping)
        return jsonify(book_list), 200
    else:
        return jsonify({"Error": "Book not found"}), 400
    
@book_bp.route('/book', methods=['POST'])
def create_book():
    data = request.get_json()

    result = BookService.create_book(
        title=data.get('title'),
        authorid=data.get('authorid'),
        image=data.get('image'),
        summary=data.get('summary'),
        year=data.get('year'),
        categoryid=data.get('categoryid')
    )

    if result > 0:
        return jsonify({"Success": "Book created!"}), 200
    elif result == -1:
        return jsonify({"Error": "Book already exists."}), 409
    else:
        return jsonify({"Error": "An error occured"}), 500
    
@book_bp.route('/book/<id>', methods=['PUT'])
def edit_book(id):
    data = request.get_json()
    
    result = BookService.edit_book(
        id=id,
        title=data.get('title'),
        authorid=data.get('authorid'),
        image=data.get('image'),
        summary=data.get('summary'),
        year=data.get('year'),
        categoryid=data.get('categoryid')
    )

    if result > 0:
        return jsonify({"Success": "Book editted!"}), 200
    elif result == -1:
        return jsonify({"Error": "Book not found."}), 404
    elif result == -2:
        return jsonify({"Error": "Book already exists."}), 409
    else:
        return jsonify({"Error": "An error occured"}), 500
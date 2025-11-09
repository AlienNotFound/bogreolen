from flask import Blueprint, jsonify, request
from backend.services.book_service import BookService
from backend.services.author_service import AuthorService
from backend.services.category_service import CategoryService
from backend.services.list_service import ListService
from backend.DTOs.book_dto import BookDTO
from flask_jwt_extended import jwt_required, get_jwt_identity

book_bp = Blueprint('book_bp', __name__)

@book_bp.route('/books', methods=['GET'])
@jwt_required()
def get_all_books():
    _, books = BookService.get_all_books()

    if books != None:
        return jsonify([BookDTO.to_dict(book) for book in books]), 200
    else:
        return jsonify({"Error": "Books not found"}), 400
    
@book_bp.route('/book/<id>', methods=['GET'])
@jwt_required()
def get_books_by_id(id):
    result, book = BookService.get_book_by_id(id)
        
    if result:        
        return jsonify(BookDTO.to_dict(book)), 200
    else:
        return jsonify({"Error": "Book not found"}), 400
    
@book_bp.route('/book', methods=['POST'])
@jwt_required()
def create_book():
    data = request.get_json()

    user_id = get_jwt_identity()

    title = data.get('title')
    author_name = data.get('author_name')
    image = data.get('image')
    summary = data.get('summary')
    year = data.get('year')
    category_title = data.get('category_title')
    listname = data.get('listname')

    author = AuthorService.get_author_by_name(author_name)

    if author == None:
        author = AuthorService.create_author(name=author_name)

    category = CategoryService.get_category_by_title(category_title)

    if category == None:
        category = CategoryService.create_category(title=category_title)

    result, message = BookService.create_book(
        title=title,
        author_id=author.author_id,
        image=image,
        summary=summary,
        year=year,
        category_id=category.category_id
    )

    if listname and result:
        ListService.add_to_list(user_id=user_id, book_id=BookService.get_latest_book().book_id, listname=listname)

    if result:
        return jsonify({"Success": f"Book created!"}), 200
    elif not result and message == "Book already exists.":
        return jsonify({"Error": f"{message}"}), 409
    else:
        return jsonify({"Error": "An error occured"}), 500
    
@book_bp.route('/book/<id>', methods=['PUT'])
@jwt_required()
def edit_book(id):
    data = request.get_json()

    title = data.get('title')
    author_name = data.get('author_name')
    image = data.get('image')
    summary = data.get('summary')
    year = data.get('year')
    category_title = data.get('category_title')

    author = AuthorService.get_author_by_name(author_name)

    if author == None:
        author = AuthorService.create_author(name=author_name)

    category = CategoryService.get_category_by_title(category_title)

    if category == None:
        category = CategoryService.create_category(title=category_title)
    
    result, message = BookService.edit_book(
        id=id,
        title=title,
        author_id=author.author_id,
        image=image,
        summary=summary,
        year=year,
        category_id=category.category_id
    )

    if result:
        return jsonify({"Success": "Book editted."}), 200
    elif message == "Book does not exist.":
        return jsonify({"Error": f'{message}'}), 404
    elif message == "Book already exists.":
        return jsonify({"Error": f'{message}'}), 409
    else:
        return jsonify({"Error": "An error occured"}), 500

@book_bp.route('/book/<id>', methods=['DELETE'])
@jwt_required()
def delete_book(id):
    if BookService.get_book_by_id(id) == None:
        return jsonify({"Error": "Book does not exist."}), 404
    
    result, message = BookService.delete_book(id)

    if result:
        return jsonify({"Success": f'{message}'}), 200
    elif message == "Book does not exist.":
        return jsonify({"Error": f'{message}'}), 404
    else:
        return jsonify({"Error": "Could not delete book."}), 500
    
@book_bp.route('/search/<title>', methods=['GET'])
@jwt_required()
def search_for_book(title):
    success, result = BookService.search_for_book(title)

    if success:
        return jsonify([BookDTO.to_dict(book) for book in result])
    else:
        return jsonify({"Error": "An error occured."}), 500
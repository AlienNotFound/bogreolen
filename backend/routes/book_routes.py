from flask import Blueprint, jsonify, request
from backend.services.book_service import BookService
from backend.services.author_service import AuthorService
from backend.services.category_service import CategoryService
from backend.services.list_service import ListService
from flask_jwt_extended import jwt_required

book_bp = Blueprint('book_bp', __name__)

@book_bp.route('/books', methods=['GET'])
@jwt_required()
def get_all_books():
    books = BookService.get_all_books()

    if books != None:
        return jsonify([book.to_dict() for book in books]), 200
    else:
        return jsonify({"Error": "Books not found"}), 400
    
@book_bp.route('/book/<id>', methods=['GET'])
@jwt_required()
def get_books_by_id(id):
    book = BookService.get_book_by_id(id)

    if book != None:
        average_rating = BookService.get_average_rating(id)
        
        return jsonify({
            "book_id": book.book_id,
            "title": book.title,
            "author_id": book.author_id,
            "author_name": book.author.name,
            "image": book.image,
            "summary": book.summary,
            "year": book.year,
            "category_id": book.category_id,
            "category_title": book.category.title,
            "average_rating": average_rating,
            "reviews": [
                    r.to_dict() for r in book.reviews
                ]
        }), 200
    else:
        return jsonify({"Error": "Book not found"}), 400
    
@book_bp.route('/book', methods=['POST'])
@jwt_required()
def create_book():
    data = request.get_json()

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
        ListService.add_to_list(user_id=1, book_id=BookService.get_latest_book().book_id, listname=listname)

    if result:
        return jsonify({"Success": f"Book created!"}), 200
    elif not result and message == "Book already exists!":
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
    
    result = BookService.edit_book(
        id=id,
        title=title,
        author_id=author.author_id,
        image=image,
        summary=summary,
        year=year,
        category_id=category.category_id
    )

    if result > 0:
        return jsonify({"Success": "Book editted!"}), 200
    elif result == -1:
        return jsonify({"Error": "Book not found."}), 404
    elif result == -2:
        return jsonify({"Error": "Book already exists."}), 409
    else:
        return jsonify({"Error": "An error occured"}), 500
    
@book_bp.route('/search/<title>', methods=['GET'])
@jwt_required()
def serach_for_book(title):
    book = BookService.search_for_book(title)

    return jsonify([b.to_dict() for b in book])
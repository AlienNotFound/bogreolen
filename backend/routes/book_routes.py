from flask import Blueprint, jsonify, request
from backend.services.book_service import BookService
from backend.services.author_service import AuthorService

book_bp = Blueprint('book_bp', __name__)

@book_bp.route('/books', methods=['GET'])
def get_all_books():
    books = BookService.get_all_books()

    if books != None:
        return jsonify([book.to_dict() for book in books]), 200
    else:
        return jsonify({"Error": "Books not found"}), 400
    
@book_bp.route('/book/<id>', methods=['GET'])
def get_books_by_id(id):
    book = BookService.get_book_by_id(id)

    if book != None:
        return jsonify({
            "bookid": book.bookid,
            "title": book.title,
            "authorid": book.authorid,
            "author_name": book.author.name,
            "image": book.image,
            "summary": book.summary,
            "categoryid": book.categoryid
        }), 200
    else:
        return jsonify({"Error": "Book not found"}), 400
    
@book_bp.route('/book', methods=['POST'])
def create_book():
    data = request.get_json()

    title = data.get('title')
    author_name = data.get('author_name')
    image = data.get('image')
    summary = data.get('summary')
    year = data.get('year')
    categoryid = data.get('categoryid')

    author = AuthorService.get_author_by_name(author_name)

    if author == None:
        author = AuthorService.create_author(name=author_name)

    result = BookService.create_book(
        title=title,
        authorid=author.authorid,
        image=image,
        summary=summary,
        year=year,
        categoryid=categoryid
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

    title = data.get('title')
    author_name = data.get('author_name')
    image = data.get('image')
    summary = data.get('summary')
    year = data.get('year')
    categoryid = data.get('categoryid')

    author = AuthorService.get_author_by_name(author_name)

    if author == None:
        author = AuthorService.create_author(name=author_name)
    
    result = BookService.edit_book(
        id=id,
        title=title,
        authorid=author.authorid,
        image=image,
        summary=summary,
        year=year,
        categoryid=categoryid
    )

    if result > 0:
        return jsonify({"Success": "Book editted!"}), 200
    elif result == -1:
        return jsonify({"Error": "Book not found."}), 404
    elif result == -2:
        return jsonify({"Error": "Book already exists."}), 409
    else:
        return jsonify({"Error": "An error occured"}), 500
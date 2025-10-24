from flask import Blueprint, jsonify, request
from backend.services.book_service import BookService
from backend.services.author_service import AuthorService
from backend.services.category_service import CategoryService
from backend.services.list_service import ListService

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
        average_rating = BookService.get_average_rating(id)
        
        return jsonify({
            "bookid": book.bookid,
            "title": book.title,
            "authorid": book.authorid,
            "author_name": book.author.name,
            "image": book.image,
            "summary": book.summary,
            "categoryid": book.categoryid,
            "category_title": book.category.title,
            "average_rating": average_rating,
            "reviews": [
                    r.to_dict() for r in book.reviews
                ]
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
    category_title = data.get('category_title')
    listname = data.get('listname')

    author = AuthorService.get_author_by_name(author_name)

    if author == None:
        author = AuthorService.create_author(name=author_name)

    category = CategoryService.get_category_by_title(category_title)

    if category == None:
        category = CategoryService.create_category(title=category_title)

    result = BookService.create_book(
        title=title,
        authorid=author.authorid,
        image=image,
        summary=summary,
        year=year,
        categoryid=category.categoryid
    )

    if listname and result > 0:
        ListService.add_book(userid=1, bookid=BookService.get_latest_book().bookid, listname=listname)

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
        authorid=author.authorid,
        image=image,
        summary=summary,
        year=year,
        categoryid=category.categoryid
    )

    if result > 0:
        return jsonify({"Success": "Book editted!"}), 200
    elif result == -1:
        return jsonify({"Error": "Book not found."}), 404
    elif result == -2:
        return jsonify({"Error": "Book already exists."}), 409
    else:
        return jsonify({"Error": "An error occured"}), 500
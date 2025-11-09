import pytest
from backend.connection import db, create_app
from backend.models.book_model import Books
from backend.services.book_service import BookService
from backend.services.user_service import UserService
from backend.services.author_service import AuthorService
from backend.services.review_service import ReviewService
from backend.services.category_service import CategoryService

book = Books(title="Test book",
                author_id=1,
                image="imageurl.jpg",
                summary="This is a summary",
                year=2000,
                category_id=1)


@pytest.fixture
def clean_db(scope="function"):
    app = create_app()

    with app.app_context():
        db.drop_all()
        db.create_all()
        
        AuthorService.create_author('Test author 1')
        AuthorService.create_author('Test author 2')

        CategoryService.create_category('Fantasy')
        CategoryService.create_category('Horror')

        UserService.create_user("test_user1", "test1@test.com", "123", "123")
        UserService.create_user("test_user2", "test2@test.com", "123", "123")
        
        yield app
        for table in reversed(db.metadata.sorted_tables):
            db.session.execute(table.delete())
        db.session.commit()

def test_create_book(clean_db):
    with clean_db.app_context():
        BookService.create_book(
            book.title,
            book.author_id,
            book.image,
            book.summary,
            book.year,
            book.category_id
        )

        success, result = BookService.get_book_by_id(1)

        assert success == True
        assert result.title == book.title
        assert result.author_id == book.author_id
        assert result.image == book.image
        assert result.summary == book.summary
        assert result.year == book.year
        assert result.category_id == book.category_id

def test_create_duplicate_fail(clean_db):
    with clean_db.app_context():
        assert BookService.get_all_books() == False, None

        BookService.create_book(
            book.title,
            book.author_id,
            book.image,
            book.summary,
            book.year,
            book.category_id
        )

        BookService.create_book(
            book.title,
            book.author_id,
            book.image,
            book.summary,
            book.year,
            book.category_id
        )

        assert len(BookService.get_all_books()) == True, 1

def test_book_get_all(clean_db):
    with clean_db.app_context():
        assert BookService.get_all_books() == False, None

        BookService.create_book(
            book.title,
            book.author_id,
            book.image,
            book.summary,
            book.year,
            book.category_id
        )

        BookService.create_book(
            book.title + "1",
            book.author_id + 1,
            book.image + "1",
            book.summary + "1",
            book.year + 1,
            book.category_id + 1
        )

        assert len(BookService.get_all_books()) == True, 2

def test_book_get_by_id(clean_db):
    with clean_db.app_context():
        BookService.create_book(
            book.title,
            book.author_id,
            book.image,
            book.summary,
            book.year,
            book.category_id
        )

        success, result = BookService.get_book_by_id(1)

        assert success == True
        assert result.book_id == 1

def test_book_edit(clean_db):
    with clean_db.app_context():
        BookService.create_book(
            book.title,
            book.author_id,
            book.image,
            book.summary,
            book.year,
            book.category_id
        )

    success, result = BookService.get_book_by_id(1)

    assert success == True
    assert result.title == book.title
    assert result.author_id == book.author_id
    assert result.image == book.image
    assert result.summary == book.summary
    assert result.year == book.year
    assert result.category_id == book.category_id

    newtitle = "New title"
    newauthor = 2
    newimage = "newimage.jpg"
    newsummary = "New summary"
    newyear = 2015
    newcategory = 2
    
    BookService.edit_book(
        1,
        newtitle,
        newauthor,
        newimage,
        newsummary,
        newyear,
        newcategory
    )

    success, result = BookService.get_book_by_id(1)

    assert success == True
    assert result.title == newtitle
    assert result.author_id == newauthor
    assert result.image == newimage
    assert result.summary == newsummary
    assert result.year == newyear
    assert result.category_id == newcategory

def test_get_average_rating(clean_db):
    with clean_db.app_context():
        BookService.create_book(
            book.title,
            book.author_id,
            book.image,
            book.summary,
            book.year,
            book.category_id
        )
        
        ReviewService.create_review(1, 1, 2, "Test1")
        ReviewService.create_review(1, 2, 4, "Test2")

    average_rating = BookService.get_average_rating(1)

    assert average_rating == 3.0
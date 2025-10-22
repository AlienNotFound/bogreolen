import pytest
from backend.connection import db, create_app
from backend.models.bookstb import Bookstb
from backend.services.book_service import BookService

book = Bookstb(title="Test book",
                authorid=1,
                image="imageurl.jpg",
                summary="This is a summary",
                year=2000,
                categoryid=1)

@pytest.fixture
def test_db():
    app = create_app()

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

def test_create_book(test_db):
    with test_db.app_context():
        result = BookService.create_book(
            book.title,
            book.authorid,
            book.image,
            book.summary,
            book.year,
            book.categoryid
        )

        assert result.fetchone()[0] == "Entry succesfully added!"

def test_create_duplicate_fail(test_db):
    pass
    # with test_db.app_context():
    #     db.session.add(book)
    #     db.session.commit()

def test_book_get_all():
    pass

def test_book_get_by_id():
    pass

def test_book_edit():
    pass

def test_book_delete():
    pass
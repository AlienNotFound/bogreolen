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
    app = create_app({
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'TESTING': True
    })

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

        print(result)

        # assert fetched.id == 1
        # assert fetched.title == "Test book"
        # assert fetched.authorid == 1
        # assert fetched.image == "imageurl.jpg"
        # assert fetched.summary == "This is a summary"
        # assert fetched.year == 2000
        # assert fetched.categoryid == 1
        assert result == "Entry succesfully added!"

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
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
def clean_db(scope="function"):
    app = create_app()

    with app.app_context():
        connection = db.engine.connect()
        transaction = connection.begin()
        options = dict(bind=connection, binds={})
        sess = db.create_scoped_session(options=options)
        db.session = sess
        yield app
        transaction.rollback()
        connection.close()
        sess.remove()

def test_create_book(clean_db):
    with clean_db.app_context():
        BookService.create_book(
            book.title,
            book.authorid,
            book.image,
            book.summary,
            book.year,
            book.categoryid
        )

        assert BookService.get_book_by_id(1).title == book.title
        assert BookService.get_book_by_id(1).authorid == book.authorid
        assert BookService.get_book_by_id(1).image == book.image
        assert BookService.get_book_by_id(1).summary == book.summary
        assert BookService.get_book_by_id(1).year == book.year
        assert BookService.get_book_by_id(1).categoryid == book.categoryid

def test_create_duplicate_fail(clean_db):
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
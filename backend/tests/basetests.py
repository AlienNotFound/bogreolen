import pytest
from backend.connection import db, create_app
from backend.models.bookstb import Bookstb

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

def test_book_creation(test_db):
    with test_db.app_context():
        book = Bookstb(title="Test book", authorid=1, image="imageurl.jpg", summary="This is a summary", year=2000, categoryid=1)
        db.session.add(book)
        db.session.commit()

        fetched = Bookstb.query.first()
        assert fetched.title == "Test book"
        assert fetched.year == 2000
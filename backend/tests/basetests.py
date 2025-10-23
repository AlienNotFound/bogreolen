import pytest
from backend.connection import db, create_app
from backend.models.bookstb import Bookstb
from backend.services.book_service import BookService
from backend.services.author_service import AuthorService

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
        db.drop_all()
        db.create_all()
        
        AuthorService.create_author('Test author 1')
        AuthorService.create_author('Test author 2')
        yield app
        for table in reversed(db.metadata.sorted_tables):
            db.session.execute(table.delete())
        db.session.commit()

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
    with clean_db.app_context():
        assert BookService.get_all_books() == None

        BookService.create_book(
            book.title,
            book.authorid,
            book.image,
            book.summary,
            book.year,
            book.categoryid
        )

        BookService.create_book(
            book.title,
            book.authorid,
            book.image,
            book.summary,
            book.year,
            book.categoryid
        )

        assert len(BookService.get_all_books()) == 1



def test_book_get_all(clean_db):
    with clean_db.app_context():
        assert BookService.get_all_books() == None

        BookService.create_book(
            book.title,
            book.authorid,
            book.image,
            book.summary,
            book.year,
            book.categoryid
        )

        BookService.create_book(
            book.title + "1",
            book.authorid + 1,
            book.image + "1",
            book.summary + "1",
            book.year + 1,
            book.categoryid + 1
        )

        assert len(BookService.get_all_books()) == 2

def test_book_get_by_id(clean_db):
    with clean_db.app_context():
        BookService.create_book(
            book.title,
            book.authorid,
            book.image,
            book.summary,
            book.year,
            book.categoryid
        )

        assert BookService.get_book_by_id(1).bookid == 1

def test_book_edit(clean_db):
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

    assert BookService.get_book_by_id(1).title == newtitle
    assert BookService.get_book_by_id(1).authorid == newauthor
    assert BookService.get_book_by_id(1).image == newimage
    assert BookService.get_book_by_id(1).summary == newsummary
    assert BookService.get_book_by_id(1).year == newyear
    assert BookService.get_book_by_id(1).categoryid == newcategory

def test_get_average_rating(clean_db):
    pass
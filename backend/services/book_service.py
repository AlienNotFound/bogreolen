from backend.connection import db
from backend.models import Bookstb
from sqlalchemy.sql import text

class BookService:
    @staticmethod
    def create_book(title, authorid, image, summary, year, categoryid):
        try:
            sql = text("""
                    CALL AddBook(:title, :authorid, :image, :summary, :year, :categoryid)""")
            result = db.session.execute(sql, {
                "title": title,
                "authorid":authorid,
                "image":image,
                "summary":summary,
                "year":year,
                "categoryid":categoryid,
            })

            db.session.commit()

            print(result.fetchone()[0])

            return result
        except Exception as e:
            print(f'Database error: ', e)
    
    @staticmethod
    def edit_book(id, title, authorid, image, summary, year, categoryid):
        book = Bookstb.query.get(id)

        setattr(book, 'title', title)
        setattr(book, 'authorid', authorid)
        setattr(book, 'image', image)
        setattr(book, 'summary', summary)
        setattr(book, 'year', year)
        setattr(book, 'categoryid', categoryid)

        db.session.commit()

        return book
    
    @staticmethod
    def get_book_by_id(id):
        book = Bookstb.query.get(id)

        db.session.commit()

        return book
    
    @staticmethod
    def get_all_books():
        books = Bookstb.query.all()

        db.session.commit()
        
        return books


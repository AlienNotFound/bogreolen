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

            return result.fetchone()[0]
            
        except Exception as e:
            print(f'Database error: ', e)
    
    @staticmethod
    def edit_book(id, title, authorid, image, summary, year, categoryid):
        try:
            sql = text("""
                        CALL UpdateBook(:bookid, :title, :authorid, :image, :summary, :year, :categoryid)
                       """)
            result = db.session.execute(sql, {
                "bookid": id,
                "title": title,
                "authorid":authorid,
                "image":image,
                "summary":summary,
                "year":year,
                "categoryid":categoryid,
            })

            db.session.commit()

            return result.fetchone()[0]

        except Exception as e:
            print(f'Database error: ', e)
    
    @staticmethod
    def get_book_by_id(id):
        book = db.session.query(Bookstb).filter_by(bookid=id).first()
        if book:
            return book
        
        return None
    
    @staticmethod
    def get_all_books():
        books = db.session.query(Bookstb).all()

        if books:
            return books
        
        return None

    def get_average_rating():
        pass

from backend.connection import db
from backend.models import Bookstb
from backend.services.base_service import BaseService
from sqlalchemy.sql import text
from sqlalchemy import func
from statistics import mean


class BookService(BaseService):
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
    
    @staticmethod
    def get_latest_book():
        return BaseService.get_by_latest(Bookstb, Bookstb.bookid)

    @staticmethod
    def get_average_rating(bookid):
        
        reviews = BookService.get_book_by_id(bookid).reviews
        ratings = []

        for r in reviews:
            ratings.append(r.rating)

        avg = mean(ratings)

        return avg

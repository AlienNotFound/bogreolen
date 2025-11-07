from backend.connection import db
from backend.models import Bookstb
from backend.services.base_service import BaseService
from sqlalchemy.sql import text
from statistics import mean


class BookService(BaseService):
    @staticmethod
    def create_book(title, author_id, image, summary, year, category_id):
        try:
            existing_book = BookService.get_book_by_title(title)
            
            if existing_book:
                return False, "Book already exists!"
            
            book = Bookstb(title=title,
                           author_id=author_id,
                           image=image,
                           summary=summary,
                           year=year,
                           category_id=category_id)
            db.session.add(book)

            success, result = BaseService.commit_session(book)

            return success, result
        except Exception as e:
            print(f'Database error: ', e)
    
    @staticmethod
    def edit_book(id, title, author_id, image, summary, year, category_id):
        try:
            sql = text("""
                        CALL UpdateBook(:book_id, :title, :author_id, :image, :summary, :year, :category_id)
                       """)
            result = db.session.execute(sql, {
                "book_id": id,
                "title": title,
                "author_id":author_id,
                "image":image,
                "summary":summary,
                "year":year,
                "category_id":category_id,
            })

            db.session.commit()

            return result.fetchone()[0]

        except Exception as e:
            print(f'Database error: ', e)
    
    @staticmethod
    def get_book_by_id(id):
        book = db.session.query(Bookstb).filter_by(book_id=id).first()
        if book:
            return book
        
        return None
    
    @staticmethod
    def get_book_by_title(title):
        book = BaseService.get_by_id(Bookstb, Bookstb.title, title)

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
        return BaseService.get_by_latest(Bookstb, Bookstb.book_id)

    @staticmethod
    def get_average_rating(book_id):
        
        reviews = BookService.get_book_by_id(book_id).reviews
        ratings = []

        for r in reviews:
            ratings.append(r.rating)

        avg = mean(ratings) if ratings else 0

        return avg
    
    @staticmethod
    def search_for_book(search_query):
        return BaseService.search_for(Bookstb, Bookstb.title, search_query)
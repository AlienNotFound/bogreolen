from backend.connection import db
from backend.models import Books
from backend.services.base_service import BaseService
from backend.services.validators.general_validators import GeneralValidator
from statistics import mean


class BookService(BaseService):
    @staticmethod
    def create_book(title, author_id, image, summary, year, category_id):
        try:
            existing_book = BookService.get_book_by_title(title)
            
            if existing_book:
                return False, "Book already exists."
            
            book = Books(title=title,
                           author_id=author_id,
                           image=image,
                           summary=summary,
                           year=year,
                           category_id=category_id)
            
            success, result = BaseService.add_entry(book)

            return success, result
        except Exception as e:
            print(f'Database error: ', e)
    
    @staticmethod
    def edit_book(id, title, author_id, image, summary, year, category_id):
        success, book = BookService.get_book_by_id(id)
        compared_book = BookService.get_book_by_title(title)
                
        if not success:
            return False, "Book does not exist."
        
        if compared_book:
            if (str(compared_book.book_id) != id) and (str(compared_book.author_id) != author_id):
                return False, "Book already exists."
        
        book.title = title
        book.author_id = author_id        
        book.image = image
        book.summary = summary
        book.year = year
        book.category_id = category_id

        success, result = BaseService.commit_session(book)

        return result, success
    
    @staticmethod
    def delete_book(id):
        success, _ = BookService.get_book_by_id(id)
        
        if success:
            BaseService.delete(Books, Books.book_id, id)
            return success, "Book deleted."
        else:
            return False, "Book does not exist."

    @staticmethod
    def get_book_by_id(id):
        book = BaseService.get_by_id(Books, Books.book_id, id)

        if book:
            return True, book
        else:
            return False, "Book does not exist."
    
    @staticmethod
    def get_book_by_title(title):
        book = BaseService.get_by_id(Books, Books.title, title)

        if book:
            return book
        
        return None
    
    @staticmethod
    def get_all_books():
        books = db.session.query(Books).all()

        if books:
            return books
        
        return None
    
    @staticmethod
    def get_latest_book():
        return BaseService.get_by_latest(Books, Books.book_id)

    @staticmethod
    def get_average_rating(book_id):
        
        _, book = BookService.get_book_by_id(book_id)
        ratings = []

        for r in book.reviews:
            ratings.append(r.rating)

        avg = mean(ratings) if ratings else 0

        return avg
    
    @staticmethod
    def search_for_book(search_query):
        result = BaseService.search_for(Books, Books.title, search_query)

        if result:
            return True, result
        else:
            return True, ''
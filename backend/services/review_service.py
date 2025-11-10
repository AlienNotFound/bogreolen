from backend.connection import db
from backend.models import Reviews
from backend.services.list_service import ListService
from backend.services.base_service import BaseService
from backend.services.validators.uservalidator import UserValidator

class ReviewService(BaseService):
    @staticmethod
    def create_review(book_id, user_id, rating, reviewtext):
        existing_review = Reviews.query.filter_by(user_id=user_id, book_id=book_id).first()

        if existing_review:
            return "You've already reviewed this book"
        
        review = Reviews(book_id=book_id, user_id=user_id, rating=rating, review=reviewtext)
        db.session.add(review)

        success, result = BaseService.commit_session(review)

        return result
        
    @staticmethod
    def edit_review(id, rating, reviewtext):
        review = Reviews.query.get(id)
        
        review.rating = rating
        review.review = reviewtext

        success, result = BaseService.commit_session(review)

        if not success:
            return UserValidator.check_for_duplicate(result)
        
        return result
    
    @staticmethod
    def get_review_by_id(id):
        return BaseService.get_by_id(Reviews, Reviews.review_id, id)
    
    @staticmethod
    def get_all_reviews():
        return BaseService.get_all(Reviews)
    
    @staticmethod
    def delete_review(id):
        return BaseService.delete(Reviews, Reviews.review_id, id)
    
    @staticmethod
    def get_reviews_based_on_user_list(user_id):
        lists = ListService.get_lists_by_user(user_id)
        book_ids = [list.book_id for list in lists]

        return Reviews.query.order_by(Reviews.review_id.desc()).filter(Reviews.book_id.in_(book_ids)).all()

    
    @staticmethod
    def get_reviews_by_user(user_id):
        reviews = BaseService.get_all_by_id(Reviews, Reviews.user_id, user_id)
        return reviews
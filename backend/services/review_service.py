from backend.connection import db
from backend.models import Reviewstb
from backend.services.list_service import ListService
from backend.services.base_service import BaseService
from backend.services.validators.uservalidator import UserValidator

class ReviewService(BaseService):
    @staticmethod
    def create_review(book_id, user_id, rating, reviewtext):
        existing_review = Reviewstb.query.filter_by(user_id=user_id, book_id=book_id).first()

        if existing_review:
            return "You've already reviewed this book"
        
        review = Reviewstb(book_id=book_id, user_id=user_id, rating=rating, review=reviewtext)
        db.session.add(review)

        success, result = BaseService.commit_session(review)

        return result
        
    @staticmethod
    def edit_review(id, rating, reviewtext):
        review = Reviewstb.query.get(id)
        
        review.rating = rating
        review.review = reviewtext

        success, result = BaseService.commit_session(review)

        if not success:
            return UserValidator.check_for_duplicate(result)
        
        return result
    
    @staticmethod
    def get_review_by_id(id):
        return BaseService.get_by_id(Reviewstb, Reviewstb.review_id, id)
    
    @staticmethod
    def get_all_reviews():
        return BaseService.get_all(Reviewstb)
    
    @staticmethod
    def delete_review(id):
        return BaseService.delete(Reviewstb, Reviewstb.review_id, id)
    
    @staticmethod
    def get_reviews_based_on_user_list(user_id):
        lists = ListService.get_lists_by_user(user_id)
        book_ids = [list.book_id for list in lists]

        return Reviewstb.query.order_by(Reviewstb.review_id.desc()).filter(Reviewstb.book_id.in_(book_ids)).all()

    
    @staticmethod
    def get_reviews_by_user(user_id):
        reviews = BaseService.get_all_by_id(Reviewstb, Reviewstb.user_id, user_id)
        return [
            {
                "book_id": review.book_id,
                "title": review.book.title,
                "rating": review.rating,
                "username": review.user.username,
                "review": review.review
            }
            for review in reviews
        ]
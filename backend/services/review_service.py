from backend.connection import db
from backend.models import Reviewstb
from backend.services.base_service import BaseService
from backend.services.validators.uservalidator import UserValidator
from werkzeug.security import generate_password_hash

class ReviewService(BaseService):
    @staticmethod
    def create_review(bookid, userid, rating, reviewtext):
        review = Reviewstb(bookid=bookid, userid=userid, rating=rating, review=reviewtext)
        db.session.add(review)

        success, result = BaseService.commit_session(review)

        if not success:
            return UserValidator.check_for_duplicate(result)

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
        return BaseService.get_by_id(Reviewstb, Reviewstb.reviewid, id)
    
    @staticmethod
    def get_all_reviews():
        return BaseService.get_all(Reviewstb)
    
    @staticmethod
    def delete_review(id):
        return BaseService.delete(Reviewstb, Reviewstb.reviewid, id)
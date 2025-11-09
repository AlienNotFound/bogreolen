from backend.connection import db
from backend.models import Comments
from backend.services.base_service import BaseService
from backend.services.review_service import ReviewService

class CommentService:
    @staticmethod
    def create_comment(user_id, review_id, comment_text):
        comment = Comments(user_id=user_id,
                           review_id=review_id,
                           comment=comment_text)
        
        success, result = BaseService.add_entry(comment)

        return success, result

    @staticmethod
    def edit_comment(id, comment_text):
        success, result = CommentService.get_comments_by_id(id)

        if not success:
            return success, result
        
        result.comment = comment_text

        success, result = BaseService.commit_session(result)

        return success, result
    
    @staticmethod
    def delete_comment(id):
        success, _ = CommentService.get_comments_by_id(id)

        if success:
            BaseService.delete(Comments, Comments.comment_id, id)
            return success, "Comment deleted."
        else:
            return False, "Comment does not exist."

    @staticmethod
    def get_all_comments_for_review(id):
        review = ReviewService.get_review_by_id(id)

        if not review:
            return False, "Review does not exist"
        
        comments = BaseService.get_all_by_id(Comments, Comments.review_id, id)

        return True, comments

    @staticmethod
    def get_comments_by_id(id):
        comment = BaseService.get_by_id(Comments, Comments.comment_id, id)

        if comment:
            return True, comment
        else:
            return False, "Comment does not exist."

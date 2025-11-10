from backend.DTOs.comment_dto import CommentDTO
class ReviewDTO:
    @staticmethod
    def to_dict(review):
        return {
            "review_id": review.review_id,
            "username": review.user.username,
            "user_id": review.user.user_id,
            "book_id": review.book_id,
            "title": review.book.title,
            "review": review.review,
            "rating": review.rating,
            "comments": [
                CommentDTO.to_dict(comment) for comment in review.comments
            ]
        }
    
    @staticmethod
    def overview_dict(review):
        return {
            "review_id": review.review_id,
            "book_title": review.book.title
        }
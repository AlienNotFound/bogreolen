from backend.models import Reviewstb

class ReviewDTO:
    @staticmethod
    def to_dict(review):
        return {
            "reviewid": review.userid,
            "bookid": review.bookid,
            "userid": review.userid,
            "rating": review.rating,
            "review": review.review,
        }
class ReviewDTO:
    @staticmethod
    def to_dict(review):
        return {
            "reviewid": review.reviewid,
            "bookid": review.bookid,
            "userid": review.userid,
            "rating": review.rating,
            "review": review.review,
        }
    
    @staticmethod
    def overview_dict(review):
        return {
            "reviewid": review.reviewid,
            "booktitle": review.book.title
        }
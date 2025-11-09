class ReviewDTO:
    @staticmethod
    def to_dict(review):
        return {
            "username": review.user.username,
            "user_id": review.user.userid,
            "book_id": review.bookid,
            "title": review.book.title,
            "review": review.review,
            "rating": review.rating,
        }
    
    @staticmethod
    def overview_dict(review):
        return {
            "review_id": review.review_id,
            "book_title": review.book.title
        }
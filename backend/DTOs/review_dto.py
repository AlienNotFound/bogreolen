class ReviewDTO:
    @staticmethod
    def to_dict(review):
        return {
            "review_id": review.review_id,
            "book_id": review.book_id,
            "user_id": review.user_id,
            "rating": review.rating,
            "review": review.review,
        }
    
    @staticmethod
    def overview_dict(review):
        return {
            "review_id": review.review_id,
            "book_title": review.book.title
        }
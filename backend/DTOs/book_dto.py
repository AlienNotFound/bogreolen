from backend.services.book_service import BookService
from backend.DTOs.review_dto import ReviewDTO
class BookDTO:
    @staticmethod
    def to_dict(book):
        average_rating = BookService.get_average_rating(book.book_id)

        return {
            "book_id": book.book_id,
            "title": book.title,
            "author_id": book.author_id,
            "author_name": book.author.name,
            "image": book.image,
            "summary": book.summary,
            "year": book.year,
            "category_id": book.category_id,
            "category_title": book.category.title,
            "average_rating": average_rating,
            "reviews": [
                ReviewDTO.to_dict(review) for review in book.reviews
            ]
        }
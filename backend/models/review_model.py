from backend.connection import db
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .book_model import Books
    from .user_model import Users
    from .comment_model import Comments

class Reviews(db.Model):
    review_id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey('books.book_id', ondelete='CASCADE'), nullable=False)
    book: Mapped['Books'] = relationship('Books', back_populates='reviews')
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'), nullable=False)
    user: Mapped['Users'] = relationship('Users', back_populates='reviews')
    rating: Mapped[float] = mapped_column(nullable=False)
    review: Mapped[str] = mapped_column(String(300))

    comments: Mapped[list['Comments']] = relationship('Comments', back_populates='review', cascade="all, delete-orphan")

    def to_dict(self):
        reviews = {field.name:getattr(self, field.name) for field in self.__table__.c}
        reviews['username'] = self.user.username

        return reviews

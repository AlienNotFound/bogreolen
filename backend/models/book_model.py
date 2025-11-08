from backend.connection import db
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .author_model import Authors
    from .category_model import Categories
    from .review_model import Reviews
    from .list_model import Lists
    from .track_model import Tracks
class Books(db.Model):
    book_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    author_id: Mapped[int] = mapped_column(ForeignKey('authors.author_id'), nullable=False)
    author: Mapped['Authors'] = relationship('Authors', back_populates='books')
    image: Mapped[str] = mapped_column(String(200))
    summary: Mapped[str] = mapped_column(String(200))
    year: Mapped[int]
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.category_id'), nullable=False)
    category: Mapped['Categories'] = relationship('Categories', back_populates='books')

    reviews: Mapped[list['Reviews']] = relationship('Reviews', back_populates='book', cascade="all, delete-orphan")
    lists: Mapped[list['Lists']] = relationship('Lists', back_populates='book', cascade="all, delete-orphan")
    tracks: Mapped[list['Tracks']] = relationship('Tracks', back_populates='book', cascade="all, delete-orphan")

    def to_dict(self):
        books = {field.name:getattr(self, field.name) for field in self.__table__.c}
        books['author'] = self.author.name
        books['category'] = self.category.title
        books['reviews'] = [r.to_dict() for r in self.reviews]

        return books
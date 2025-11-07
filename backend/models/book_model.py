from backend.connection import db
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .author_model import Authorstb
    from .category_model import Categoriestb
    from .review_model import Reviewstb
    from .list_model import Liststb
    from .track_model import Trackstb
class Bookstb(db.Model):
    book_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    author_id: Mapped[int] = mapped_column(ForeignKey('authorstb.authorid'), nullable=False)
    author: Mapped['Authorstb'] = relationship('Authorstb', back_populates='books')
    image: Mapped[str] = mapped_column(String(200))
    summary: Mapped[str] = mapped_column(String(200))
    year: Mapped[int]
    category_id: Mapped[int] = mapped_column(ForeignKey('categoriestb.categoryid'), nullable=False)
    category: Mapped['Categoriestb'] = relationship('Categoriestb', back_populates='books')

    reviews: Mapped[list['Reviewstb']] = relationship('Reviewstb', back_populates='book')
    lists: Mapped[list['Liststb']] = relationship('Liststb', back_populates='book')
    tracks: Mapped[list['Trackstb']] = relationship('Trackstb', back_populates='book')

    def to_dict(self):
        books = {field.name:getattr(self, field.name) for field in self.__table__.c}
        books['author'] = self.author.name
        books['category'] = self.category.title
        books['reviews'] = [r.to_dict() for r in self.reviews]

        return books
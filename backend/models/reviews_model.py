from backend.connection import db
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .bookstb import Bookstb

class Reviewstb(db.Model):
    reviewid: Mapped[int] = mapped_column(primary_key=True)
    bookid: Mapped[int] = mapped_column(ForeignKey('bookstb.bookid'), nullable=False)
    book: Mapped['Bookstb'] = relationship('Bookstb', back_populates='reviews')
    # userid: Mapped[int] = mapped_column(ForeignKey('userstb.userid'), nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
    review: Mapped[str] = mapped_column(String(300))

    def to_dict(self):
        reviews = {field.name:getattr(self, field.name) for field in self.__table__.c}

        return reviews

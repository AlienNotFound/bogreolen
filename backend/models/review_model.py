from backend.connection import db
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .book_model import Bookstb
    from .user_model import Userstb

class Reviewstb(db.Model):
    review_id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey('bookstb.bookid'), nullable=False)
    book: Mapped['Bookstb'] = relationship('Bookstb', back_populates='reviews')
    user_id: Mapped[int] = mapped_column(ForeignKey('userstb.userid'), nullable=False)
    user: Mapped['Userstb'] = relationship('Userstb', back_populates='reviews')
    rating: Mapped[float] = mapped_column(nullable=False)
    review: Mapped[str] = mapped_column(String(300))

    def to_dict(self):
        reviews = {field.name:getattr(self, field.name) for field in self.__table__.c}
        reviews['username'] = self.user.username

        return reviews

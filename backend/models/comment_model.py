from backend.connection import db
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .review_model import Reviews
    from .user_model import Users

class Comments(db.Model):
    comment_id: Mapped[int] = mapped_column(primary_key=True)
    review_id: Mapped[int] = mapped_column(ForeignKey('reviews.review_id', ondelete='CASCADE'), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'), nullable=False)
    comment: Mapped[str] = mapped_column(String(150))

    # user: Mapped['Users'] = relationship('Users', back_populates='comments')
    # review: Mapped['Reviews'] = relationship(back_populates='comments')

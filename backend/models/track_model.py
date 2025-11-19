from backend.connection import db
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .book_model import Books
    from .user_model import Users

class Tracks(db.Model):
    track_id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey('books.book_id', ondelete="CASCADE"), nullable=False)
    book: Mapped['Books'] = relationship('Books', back_populates='tracks')
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id'), nullable=False)
    user: Mapped['Users'] = relationship('Users', back_populates='tracks')
    current_page: Mapped[int]
    last_page: Mapped[int]
    date: Mapped[datetime] = mapped_column()
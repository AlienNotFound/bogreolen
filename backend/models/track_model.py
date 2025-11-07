from backend.connection import db
from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .book_model import Bookstb
    from .user_model import Userstb

class Trackstb(db.Model):
    track_id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey('bookstb.bookid'), nullable=False)
    book: Mapped['Bookstb'] = relationship('Bookstb', back_populates='tracks')
    user_id: Mapped[int] = mapped_column(ForeignKey('userstb.userid'), nullable=False)
    user: Mapped['Userstb'] = relationship('Userstb', back_populates='tracks')
    current_page: Mapped[int]
    last_page: Mapped[int]
    date: Mapped[datetime] = mapped_column(insert_default=func.now())
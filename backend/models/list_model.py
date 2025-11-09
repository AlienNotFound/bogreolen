from backend.connection import db
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .book_model import Books
    from .user_model import Users

class ListName(Enum):
    WANT_TO_READ = 'Want to read'
    READING = 'Reading'
    DIDNTFINISH = 'Didn\'t finish'
    FINISHED = 'Finished'

class Lists(db.Model):
    book_id: Mapped[int] = mapped_column(ForeignKey('books.book_id', ondelete="CASCADE"), nullable=False, primary_key=True)
    book: Mapped['Books'] = relationship('Books', back_populates='lists')
    user_id: Mapped[int] = mapped_column(ForeignKey('users.user_id', ondelete="CASCADE"), nullable=False, primary_key=True)
    user: Mapped['Users'] = relationship('Users', back_populates='lists')
    listname: Mapped[ListName]

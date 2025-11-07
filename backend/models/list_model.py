from backend.connection import db
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .book_model import Bookstb
    from .user_model import Userstb

class ListName(Enum):
    WANT_TO_READ = 'Want to read'
    READING = 'Reading'
    DIDNTFINISH = 'Didn\'t finish'
    FINISHED = 'Finished'

class Liststb(db.Model):
    book_id: Mapped[int] = mapped_column(ForeignKey('bookstb.bookid'), nullable=False, primary_key=True)
    book: Mapped['Bookstb'] = relationship('Bookstb', back_populates='lists')
    user_id: Mapped[int] = mapped_column(ForeignKey('userstb.userid'), nullable=False, primary_key=True)
    user: Mapped['Userstb'] = relationship('Userstb', back_populates='lists')
    listname: Mapped[ListName]

from backend.connection import db
from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .book_model import Books

class Authors(db.Model):
    author_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)
    UniqueConstraint('name')
 
    books: Mapped['Books'] = relationship('Books', back_populates='author', cascade="all, delete-orphan")

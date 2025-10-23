from backend.connection import db
from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .bookstb import Bookstb

class Categoriestb(db.Model):
    categoryid: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30), unique=True)
    UniqueConstraint('title')
 
    books: Mapped['Bookstb'] = relationship('Bookstb', back_populates='category')

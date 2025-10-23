from backend.connection import db
from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Authorstb(db.Model):
    authorid: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)
    UniqueConstraint('name')
 
    books: Mapped['Bookstb'] = relationship('Bookstb', back_populates='author')

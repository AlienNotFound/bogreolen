from backend.connection import db
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Bookstb(db.Model):
    bookid: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    authorid: Mapped[int] = mapped_column(ForeignKey('authorstb.authorid'), nullable=False)
    author: Mapped['Authorstb'] = relationship('Authorstb', back_populates='books')
    image: Mapped[str] = mapped_column(String(30))
    summary: Mapped[str] = mapped_column(String(200))
    year: Mapped[int]
    categoryid: Mapped[int]
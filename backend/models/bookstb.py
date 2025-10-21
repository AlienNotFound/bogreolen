from backend.connection import db
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import YEAR

class Bookstb(db.Model):
    bookid: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(15), unique=True)
    authorid: Mapped[int]
    image: Mapped[str] = mapped_column(String(30))
    summary: Mapped[str] = mapped_column(String(200))
    year: Mapped[int]
    categoryid: Mapped[int]

    def create_book():
        print("book")

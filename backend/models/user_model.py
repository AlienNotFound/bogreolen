from backend.connection import db
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .bookstb import Bookstb

class Userstb(db.Model):
    userid: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    passwordhash: Mapped[str] = mapped_column(String(255), nullable=False)

    def to_dict(self):
        reviews = {field.name:getattr(self, field.name) for field in self.__table__.c}

        return reviews

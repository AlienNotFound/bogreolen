from backend.connection import db
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .review_model import Reviews
    from .list_model import Lists
    from .track_model import Tracks
class Users(db.Model):
    user_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    passwordhash: Mapped[str] = mapped_column(String(255), nullable=False)

    reviews: Mapped[list['Reviews']] = relationship('Reviews', back_populates='user', cascade="all, delete-orphan")
    lists: Mapped[list['Lists']] = relationship('Lists', back_populates='user', cascade="all, delete-orphan")
    tracks: Mapped[list['Tracks']] = relationship('Tracks', back_populates='user', cascade="all, delete-orphan")

    def to_dict(self):
        reviews = {field.name:getattr(self, field.name) for field in self.__table__.c}

        return reviews

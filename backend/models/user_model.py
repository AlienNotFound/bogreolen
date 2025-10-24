from backend.connection import db
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .reviews_model import Reviewstb
    from .list_model import Liststb
    from .tracks_model import Trackstb
class Userstb(db.Model):
    userid: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    passwordhash: Mapped[str] = mapped_column(String(255), nullable=False)

    reviews: Mapped[list['Reviewstb']] = relationship('Reviewstb', back_populates='user')
    lists: Mapped[list['Liststb']] = relationship('Liststb', back_populates='user')
    tracks: Mapped[list['Trackstb']] = relationship('Trackstb', back_populates='user')

    def to_dict(self):
        reviews = {field.name:getattr(self, field.name) for field in self.__table__.c}

        return reviews

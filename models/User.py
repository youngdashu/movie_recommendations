from typing import List

from sqlalchemy.orm import mapped_column, Mapped, relationship

from models.Base import Base


class User(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True)
    ratings: Mapped[List["Rating"]] = relationship(back_populates="user")
    tags: Mapped[List["Tag"]] = relationship(back_populates="user")

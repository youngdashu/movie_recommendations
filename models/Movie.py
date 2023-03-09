from typing import List

from sqlalchemy import String, Table, ForeignKey, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Base import Base
from models.Rating import Rating
from models.Tag import Tag
from models.Link import Link



movie_genres = Table(
    "movie_genres",
    Base.metadata,
    Column("movie_id", ForeignKey("movie.id")),
    Column("genre_id", ForeignKey("genre.id")),
)


class Movie(Base):
    __tablename__ = "movie"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))

    genres: Mapped[List["Genre"]] = relationship(
        secondary=movie_genres, back_populates="movies"
    )
    ratings: Mapped[List["Rating"]] = relationship(back_populates="movie")
    links: Mapped[List["Link"]] = relationship(back_populates="movie")
    tags: Mapped[List["Tag"]] = relationship(back_populates="movie")


class Genre(Base):
    __tablename__ = "genre"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    movies: Mapped[List[Movie]] = relationship(
        secondary=movie_genres, back_populates="genres"
    )

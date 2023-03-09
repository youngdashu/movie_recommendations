from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from models.Base import Base


class Link(Base):
    __tablename__ = "link"

    id: Mapped[int] = mapped_column(primary_key=True)
    movie_id: Mapped[int] = mapped_column(ForeignKey("movie.id"))
    movie: Mapped["Movie"] = relationship(back_populates="links")
    imdbId: Mapped[str] = mapped_column(String(30))
    tmdbId: Mapped[str] = mapped_column(String(30))

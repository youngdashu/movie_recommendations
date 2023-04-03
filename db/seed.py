from sqlalchemy import delete, insert
from sqlalchemy.orm import Session

from db import Connection
from models.Base import Base
from models.Movie import Genre


def main():
    connection = Connection()
    Base.metadata.drop_all(connection.engine)
    Base.metadata.create_all(connection.engine)
    with Session(connection.engine) as session:
        session.execute(delete(Genre))

    with Session(connection.engine) as session:
        genre_names = [
            "Action",
            "Adventure",
            "Animation",
            "Children",
            "Comedy",
            "Crime",
            "Documentary",
            "Drama",
            "Fantasy",
            "Film-Noir",
            "Horror",
            "Musical",
            "Mystery",
            "Romance",
            "Sci-Fi",
            "Thriller",
            "War",
            "Western",
        ]

        special_genres = ['IMAX']

        session.execute(
            insert(Genre),
            list(
                map(lambda name: {"name": name}, genre_names + special_genres)
            )

        )

        session.commit()


if __name__ == "__main__":
    print("start")
    main()

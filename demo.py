from sqlalchemy import select
from sqlalchemy.orm import Session

from db.Connection import Connection
from models.Movie import Movie


def main():
    connection = Connection()
    with Session(connection.engine) as session:
        movies = session.scalars(select(Movie)).all()
        for movie in movies:
            print(movie.name)
            list(map(lambda genre: print(genre.name), movie.genres))
            break


if __name__ == "__main__":
    main()
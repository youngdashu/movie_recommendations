import csv
import os

from sqlalchemy import select
from sqlalchemy.orm import Session

from db.Connection import Connection
from models.Movie import Movie, Genre
from models.Rating import Rating
from models.Tag import Tag
from models.User import User

from datetime import datetime

import pandas as pd


def parse_file(path: str, read_lines):
    with open(path) as f:
        connection = Connection()
        with Session(connection.engine) as session:
            csv_reader = csv.reader(f)

            header = next(csv_reader)
            read_lines(csv_reader, session)

            session.commit()


def movies_and_genres(csv_reader, session: Session):
    print("Movies and genres")
    all_genres = session.scalars(select(Genre)).all()
    all_genres = {genre.name: genre for genre in all_genres}
    for line in csv_reader:
        (id_value, title, genres) = line
        movie_genres = genres.split('|')
        try:
            movie = Movie(id=id_value, name=title, genres=[all_genres[genre_name] for genre_name in movie_genres])
        except KeyError:
            movie = Movie(id=id_value, name=title, genres=[])

        session.add(movie)


def ratings(file_name):
    print("Ratings")
    df = pd.read_csv(file_name)
    row_count = df.shape[0]
    connection = Connection()
    with Session(connection.engine) as session:
        for row in df.itertuples():
            rating = Rating(user_id=int(row.userId), movie_id=int(row.movieId), timestamp=int(row.timestamp),
                            rating=row.rating)
            session.add(rating)
            if row.Index % 10000 == 0:
                print(int(float(row.Index) / float(row_count) * 100), ' %')
                session.commit()
        session.commit()


def users(path):
    print("Users")
    with open(path) as f:
        connection = Connection()
        with Session(connection.engine) as session:
            last_line = f.readlines()[-1]
            user_count = int(last_line.split(',')[0])
            session.add_all(tuple(User() for _ in range(user_count)))
            session.commit()


def tags(csv_reader, session: Session):
    print("Tags")
    for line in csv_reader:
        (user_id, movie_id, tag, timestamp) = line
        tag = Tag(user_id=int(user_id), movie_id=int(movie_id), name=tag, timestamp=timestamp)
        session.add(tag)


def main():
    path_base = './ml-latest/' if os.environ.get('IS_DOCKER', False) else '../ml-latest/'

    users('%sratings.csv' % path_base)
    parse_file('%smovies.csv' % path_base, movies_and_genres)
    parse_file('%stags.csv' % path_base, tags)
    ratings('%sratings.csv' % path_base)


if __name__ == "__main__":
    main()

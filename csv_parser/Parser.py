import csv

from sqlalchemy import select
from sqlalchemy.orm import Session

from db.Connection import Connection
from models.Movie import Movie, Genre
from models.Rating import Rating
from models.Tag import Tag
from models.User import User

from datetime import datetime

import pandas as pd


def parse_file(name: str, read_lines):
    with open('../ml-latest/' + name) as f:
        connection = Connection()
        with Session(connection.engine) as session:
            csv_reader = csv.reader(f)

            header = next(csv_reader)
            read_lines(csv_reader, session)

            session.commit()


def movies_and_genres(csv_reader, session: Session):

    all_genres = session.scalars(select(Genre)).all()
    all_genres = {genre.name: genre for genre in all_genres}
    for line in csv_reader:
        (_, title, genres) = line
        movie_genres = genres.split('|')
        try:
            movie = Movie(name=title, genres=[all_genres[genre_name] for genre_name in movie_genres])
        except KeyError:
            movie = Movie(name=title, genres=[])

        session.add(movie)

def ratings(file_name):
    csv_file = pd.read_csv(file_name)
    connection = Connection()
    with Session(connection.engine) as session:
        for r in csv_file:
            print(r)
            return




def users():
    with open('../ml-latest/ratings.csv') as f:
        connection = Connection()
        with Session(connection.engine) as session:
            last_line = f.readlines()[-1]
            user_count = int(last_line.split(',')[0])
            print(user_count)
            session.add_all(tuple(User() for _ in range(user_count)))
            session.commit()
    print(datetime.now())


def tags(csv_reader, session: Session):
    for line in csv_reader:
        (user_id, movie_id, tag, timestamp) = line
        tag = Tag(user_id=int(user_id), movie_id=int(movie_id), name=tag, timestamp=timestamp)
        session.add(tag)

def main():
    # users()
    # parse_file('movies.csv', movies_and_genres)
    # parse_file('tags.csv', tags)
    ratings('../ml-latest/' + 'ratings.csv')



if __name__ == "__main__":
    main()
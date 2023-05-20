import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import base64

poster_url = "https://image.tmdb.org/t/p/w600_and_h900_bestv2{}"
apikey = "c64ddb28627cb5229e96a8538d22e8f8"
endpoint_url = "https://api.themoviedb.org/3/movie/{}?api_key=c64ddb28627cb5229e96a8538d22e8f8"
cast_endpoint_url = "https://api.themoviedb.org/3/movie/{}/credits?api_key=c64ddb28627cb5229e96a8538d22e8f8"


def split_genres(text):
    if text == '(no genres listed)':
        return []

    return text.split("|")


def clean(text):
    new_text = ''
    for x in text:
        if x != '[' and x != ']' and x != ',' and x != "'":
            new_text += x

    return new_text


class CommonUtils:
    movies, ratings, tags, links = [None] * 4
    vectorized = None

    def __init__(self, path: str):
        engine = 'python'

        self.movies = pd.read_csv(path + 'movies.csv')
        self.ratings = pd.read_csv(path + 'ratings.csv')
        self.tags = pd.read_csv(path + 'tags.csv')
        self.links = pd.read_csv(path + 'links.csv')
        self.combined = None

    def combine_tags_and_genres(self):
        grouped = self.tags.groupby(by='movieId')['tag'].apply(list).reset_index(name='tags')
        movies_tag_merged = self.movies.merge(grouped, how='left', on='movieId')

        movies_tag_merged['genres'] = movies_tag_merged['genres'].apply(split_genres)

        movies_tag_merged['tags'] = movies_tag_merged['tags'].apply(lambda d: d if isinstance(d, list) else [])

        movies_tag_merged['combined_genres_tags'] = movies_tag_merged['genres'] + movies_tag_merged['tags']
        movies_tag_merged['combined_genres_tags'] = movies_tag_merged['combined_genres_tags'].astype('str')

        movies_tag_merged['combined_genres_tags'] = movies_tag_merged['combined_genres_tags'].apply(clean)

        self.combined = movies_tag_merged

    def get_tags_for_movie(self, movie_id):
        return self.tags[self.tags['movieId'] == movie_id]['tag'].tolist()

    def get_poster_base64(self, tmdb_id):
        missing_ids = []
        try:
            response = requests.get(endpoint_url.format(tmdb_id))
            path = response.json()['poster_path']

            response = requests.get(poster_url.format(path))
            img = Image.open(BytesIO(response.content))
            img.thumbnail((128, 128), Image.LANCZOS)
            return img
        except:
            missing_ids.append(tmdb_id)
            return None

    def get_poster_for_movie(self, movie_id):
        tmdb_id = self.links[self.links['movieId'] == movie_id]['tmdbId'].iloc[0]

        return self.get_poster_base64(tmdb_id)

import math
from io import BytesIO

import pandas as pd
import requests
from PIL import Image
from matplotlib import pyplot as plt

from ml_models import CollaborationModel
from ml_models import CommonUtils
from ml_models import ContentBasedModel
from ml_models import HybridModel
from ml_models.CommonUtils import endpoint_url


def load_movies_ratings_tags_links(dirpath):
    print(dirpath)
    movies = pd.read_csv(dirpath + 'movies.csv', lineterminator='\n')
    ratings = pd.read_csv(dirpath + 'ratings.csv')
    tags = pd.read_csv(dirpath + 'tags.csv')
    links = pd.read_csv(dirpath + 'links.csv')

    return movies, ratings, tags, links


def visualise(result):
    dirpath = "./data/"
    movies, ratings, tags, links = load_movies_ratings_tags_links(dirpath)
    print(links)
    visualise_sugestions(result,tags,movies,links)


def get_poster_for_movie(movieId, links):
    tmdbId = links[links['movieId'] == movieId]['tmdbId'].iloc[0]

    return get_poster_base64(tmdbId)


def get_poster_base64(tmdbId):
    poster_url = "https://image.tmdb.org/t/p/w600_and_h900_bestv2{}"

    try:
        response = requests.get(endpoint_url.format(tmdbId))
        path = response.json()['poster_path']

        response = requests.get(poster_url.format(path))
        img = Image.open(BytesIO(response.content))
        img.thumbnail((128, 128), Image.LANCZOS)
        return img

    except:
        print(tmdbId)
        return None


def get_tags_for_movie(movieId, tags):
    return tags[tags['movieId'] == movieId]['tag'].tolist()


def visualise_sugestions(results, tags, movies,links, n=10):
    top_10 = results[1:n + 1]

    fig, ax = plt.subplots(math.ceil(n / 5), 5, layout="compressed", figsize=(10, 8))
    axes = ax.flat

    i = 0
    for (top_idx, similarity) in map(lambda x:(x[1],x[0]),top_10):
        row_movie = movies.iloc[top_idx]

        similarity = "{:.3f}".format(similarity)
        row_tags = ', '.join(get_tags_for_movie(row_movie['movieId'], tags))

        axes[i].imshow(get_poster_for_movie(row_movie['movieId'],links), aspect='auto')
        i += 1
    plt.show()


if __name__ == '__main__':
    common = CommonUtils("./data/")

    common.combine_tags_and_genres()

    content_based = ContentBasedModel(common)

    collaboration_model = CollaborationModel(common)

    hybrid_model = HybridModel(common, content_based, collaboration_model)

    result = hybrid_model.get_recommendation(1, "Toy Story (1995)")

    visualise(result)

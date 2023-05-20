from . import CommonUtils
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
import math

default_vectorizer = TfidfVectorizer(analyzer='word', stop_words='english', min_df=0, ngram_range=(1, 2))

# TODO: dodać metadane w końcu
# TODO: filtrowanie słabych filmów (na podstawie średniej albo percentyli sory zapomniałem o tym)
class ContentBasedModel:
    common_utils = None
    transformed = None

    cosine_sim = None

    def __init__(self, common_utils: CommonUtils, vectorizer=default_vectorizer):
        self.common_utils = common_utils

        self.transformed = vectorizer.fit_transform(self.common_utils.combined['combined_genres_tags'])
        self.cosine_sim = linear_kernel(self.transformed)

    def get_similar(self, title, n=10):
        movies = self.common_utils.movies

        idx = movies[movies['title'] == title].index[0]
        queried_movie = movies.iloc[idx]

        index_score = list(enumerate(self.cosine_sim[idx]))
        sim_scores = sorted(index_score, key=lambda x: x[1], reverse=True)

        top_10 = sim_scores[1:n + 1]

        fig, ax = plt.subplots(math.ceil(n / 5), 5, layout="compressed", figsize=(10, 8))
        axes = ax.flat

        print(
            f'Propozycje dla: {queried_movie.title} ({queried_movie.genres}) ({self.common_utils.get_tags_for_movie(queried_movie["movieId"])})')

        i = 0
        for (top_idx, similarity) in top_10:
            row_movie = movies.iloc[top_idx]

            similarity = "{:.3f}".format(similarity)
            row_tags = ', '.join(self.common_utils.get_tags_for_movie(row_movie['movieId']))

            print(f'{row_movie.title}, cosine_sim: {similarity}')
            print(f'  > Gatunki: {row_movie.genres}')
            print(f'  > Tagi: {row_tags}')

            axes[i].imshow(self.common_utils.get_poster_for_movie(row_movie['movieId']), aspect='auto')
            i += 1

        plt.savefig('contentbased_posters.png')
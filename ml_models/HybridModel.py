from . import CommonUtils, ContentBasedModel, CollaborationModel


# TODO: analiza dla jakiegoś usera, jakie filmy ocenil dotychczasowo i czy zwrocony wynik ma sens

class HybridModel:
    common_utils = None
    content_based = None
    collaboration_model = None

    def __init__(self, common_utils: CommonUtils, content_based: ContentBasedModel, collaboration_model: CollaborationModel):
        self.common_utils = common_utils
        self.content_based = content_based
        self.collaboration_model = collaboration_model

    def get_recommendation(self, user_id, title, n=10):
        top_similar = self.content_based.get_similar(title, n=n, verbose=False)

        scores = [self.collaboration_model.get_prediction(user_id, idx_similarity_pair[0]).est for idx_similarity_pair in top_similar]
        movie_ids, sim_scores = zip(*top_similar)
        titles = [self.common_utils.get_title_by_movie_id(x) for x in movie_ids]

        combined = zip(scores, movie_ids, titles)

        sorted_by_predicted_score = sorted(combined, key= lambda x: x[0], reverse=True)

        return sorted_by_predicted_score



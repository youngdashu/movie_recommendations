from surprise import accuracy, Dataset, SVD, Reader
from surprise.model_selection import train_test_split
from . import CommonUtils


class CollaborationModel:
    common_utils = None
    data = None
    algo = None

    # TODO: test/train split uwzględnić nwm by nie predyktować dla istniejących ocen w train secie albo to jebac i wytrenowac na calym secie
    def __init__(self, common_utils: CommonUtils):
        self.common_utils = common_utils
        self.data = Dataset.load_from_df(self.common_utils.ratings[['userId', 'movieId', 'rating']],
                                         reader=Reader(rating_scale=(1, 5)))

        trainset = self.data.build_full_trainset()
        self.algo = SVD()
        self.algo.fit(trainset)

    def get_prediction(self, user_id, movie_id):
        return self.algo.predict(user_id, movie_id)

from . import CommonUtils, ContentBasedModel

# TODO:

class HybridModel:
    common_utils = None
    content_based = None
    collaboration_model = None

    def __init__(self, common_utils: CommonUtils, content_based: ContentBasedModel, collaboration_model):
        self.common_utils = common_utils
        self.content_based = content_based
        self.collaboration_model = collaboration_model

    def get_recommendation(self, user_id, title, n=10):
        pass
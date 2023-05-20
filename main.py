from ml_models import CommonUtils
from ml_models import ContentBasedModel
from ml_models import CollaborationModel

common = CommonUtils("./data/")

common.combine_tags_and_genres()

content_based = ContentBasedModel(common)

content_based.get_similar("Toy Story (1995)")


# collaboration_model = CollaborationModel(common)
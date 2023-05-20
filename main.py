from ml_models import CommonUtils
from ml_models import ContentBasedModel
from ml_models import CollaborationModel
from ml_models import HybridModel

common = CommonUtils("./data/")

common.combine_tags_and_genres()

content_based = ContentBasedModel(common)

collaboration_model = CollaborationModel(common)

hybrid_model = HybridModel(common, content_based, collaboration_model)

result = hybrid_model.get_recommendation(1, "Toy Story (1995)")

print(result)
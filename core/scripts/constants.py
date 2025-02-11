CLASSIFIED_LABELS_ARRAY = {
    "masterCategory": {"label": "", "confidence": 0.0},
    "subCategory": {"label": "", "confidence": 0.0},
    "articleType": {"label": "", "confidence": 0.0},
    "baseColour": {"label": "", "confidence": 0.0},
    "season": {"label": "", "confidence": 0.0},
    "usage": {"label": "", "confidence": 0.0},
}


PATH_ARTICLE_TYPE_RELATIONSHIP_DATA = "core/data/article_type_relationships.csv"
PATH_LABELS = "core/labels"
PATH_MODELS = "core/models"
PATH_TEMP_FILES = "temp"

MODEL_ARTICLE_TYPE = f"{PATH_MODELS}/article_type.pt"
MODEL_BASE_COLOUR = f"{PATH_MODELS}/base_colour.pt"
MODEL_SEASON = f"{PATH_MODELS}/season.pt"
MODEL_USAGE = f"{PATH_MODELS}/usage.pt"

LAYERS_ARTICLE_TYPE = 33
LAYERS_BASE_COLOUR = 46
LAYERS_SEASON = 4
LAYERS_USAGE = 8

TAG_NAME_ARTICLE_TYPE = "article_types"
TAG_NAME_BASE_COLOUR = "base_colours"
TAG_NAME_SEASON = "seasons"
TAG_NAME_USAGE = "usages"

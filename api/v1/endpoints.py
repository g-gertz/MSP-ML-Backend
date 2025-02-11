import os
import uuid

from fastapi import APIRouter, File, UploadFile

from core.scripts.classification import classify_single_label
from core.scripts.constants import (
    CLASSIFIED_LABELS_ARRAY,
    LAYERS_ARTICLE_TYPE,
    LAYERS_BASE_COLOUR,
    LAYERS_SEASON,
    LAYERS_USAGE,
    MODEL_ARTICLE_TYPE,
    MODEL_BASE_COLOUR,
    MODEL_SEASON,
    MODEL_USAGE,
    PATH_TEMP_FILES,
    TAG_NAME_ARTICLE_TYPE,
    TAG_NAME_BASE_COLOUR,
    TAG_NAME_SEASON,
    TAG_NAME_USAGE,
)
from core.scripts.utils import find_master_and_sub_category_from_article_type

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "API is working!"}


@router.post("/classify")
async def classify_uploaded_image(input_image: UploadFile = File(...)):
    input_image_path = f"{PATH_TEMP_FILES}/{uuid.uuid4()}.jpg"

    if not os.path.exists(PATH_TEMP_FILES):
        os.mkdir(PATH_TEMP_FILES)

    with open(input_image_path, "wb") as buffer:
        buffer.write(input_image.file.read())

    classified_labels = CLASSIFIED_LABELS_ARRAY.copy()

    article_type, article_type_conf = classify_single_label(
        MODEL_ARTICLE_TYPE, LAYERS_ARTICLE_TYPE, TAG_NAME_ARTICLE_TYPE, input_image_path
    )
    base_colour, base_colour_conf = classify_single_label(
        MODEL_BASE_COLOUR, LAYERS_BASE_COLOUR, TAG_NAME_BASE_COLOUR, input_image_path
    )
    season, season_conf = classify_single_label(
        MODEL_SEASON, LAYERS_SEASON, TAG_NAME_SEASON, input_image_path
    )
    usage, usage_conf = classify_single_label(
        MODEL_USAGE, LAYERS_USAGE, TAG_NAME_USAGE, input_image_path
    )

    master_category, sub_category = find_master_and_sub_category_from_article_type(
        article_type
    )

    classified_labels["masterCategory"] = {
        "label": master_category,
        "confidence": 1.0,
    }
    classified_labels["subCategory"] = {
        "label": sub_category,
        "confidence": 1.0,
    }
    classified_labels["articleType"] = {
        "label": article_type,
        "confidence": article_type_conf,
    }
    classified_labels["baseColour"] = {
        "label": base_colour,
        "confidence": base_colour_conf,
    }
    classified_labels["season"] = {"label": season, "confidence": season_conf}
    classified_labels["usage"] = {"label": usage, "confidence": usage_conf}

    os.remove(input_image_path)

    return classified_labels

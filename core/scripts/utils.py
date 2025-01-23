def resize_image_to_fixed_height(image, fixed_height=900):
    import cv2

    original_height, original_width = image.shape[:2]
    ratio = fixed_height / original_height
    new_width = int(original_width * ratio)
    resized_image = cv2.resize(
        image, (new_width, fixed_height), interpolation=cv2.INTER_AREA
    )

    return resized_image


def find_master_and_sub_category_from_article_type(article_type):
    import pandas as pd

    from core.scripts.constants import PATH_ARTICLE_TYPE_RELATIONSHIP_DATA

    df = pd.read_csv(PATH_ARTICLE_TYPE_RELATIONSHIP_DATA)

    result = df[df["articleType"] == article_type]
    if not result.empty:
        master_category = result["masterCategory"].values[0]
        sub_category = result["subCategory"].values[0]
        return master_category, sub_category
    else:
        return None, None

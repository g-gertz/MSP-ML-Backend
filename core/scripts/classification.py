import cv2
import joblib
import numpy as np
import torch
import torch.nn.functional as F
import torchvision.transforms as transforms

from core.scripts.constants import PATH_LABELS
from core.scripts.models import SingleHeadResNet50

# loss_fn has to be imported due to -> https://github.com/pytorch/pytorch/issues/18325
from loss_functions import loss_fn


def classify_single_label(
    model_path: str, layers_count: int, tag_name: str, input_image_path: str
) -> tuple[str, float]:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = SingleHeadResNet50(
        pretrained=False, requires_grad=False, layers=layers_count
    )
    checkpoint = torch.load(model_path, map_location=device, weights_only=False)

    model.load_state_dict(checkpoint["model_state_dict"])
    model.to(device)
    model.eval()

    transform = transforms.Compose(
        [
            transforms.ToPILImage(),
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )

    image = cv2.imread(input_image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = transform(image)
    image = image.unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(image)
        probabilities = F.softmax(output, dim=1)

    out_label_idx = np.argmax(output.cpu().numpy())
    confidence = round(probabilities[0, out_label_idx].item(), 2)

    num_list_data = joblib.load(f"{PATH_LABELS}/{tag_name}.pkl")

    data_keys = list(num_list_data.keys())
    data_values = list(num_list_data.values())

    final_label = data_keys[data_values.index(out_label_idx)]

    return final_label, confidence

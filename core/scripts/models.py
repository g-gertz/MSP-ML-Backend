import pretrainedmodels
import torch.nn as nn
import torch.nn.functional as F


class SingleHeadResNet50(nn.Module):
    def __init__(self, pretrained, requires_grad, layers):
        super(SingleHeadResNet50, self).__init__()

        if pretrained:
            self.model = pretrainedmodels.__dict__["resnet50"](pretrained="imagenet")
        else:
            self.model = pretrainedmodels.__dict__["resnet50"](pretrained=None)

        if requires_grad:
            for param in self.model.parameters():
                param.requires_grad = True
            print("Training intermediate layer parameters...")
        else:
            for param in self.model.parameters():
                param.requires_grad = False
            print("Freezing intermediate layer parameters...")

        self.l0 = nn.Linear(2048, layers)

    def forward(self, x):
        batch_size, _, _, _ = x.shape
        x = self.model.features(x)
        x = F.adaptive_avg_pool2d(x, 1).reshape(batch_size, -1)
        l0 = self.l0(x)
        return l0

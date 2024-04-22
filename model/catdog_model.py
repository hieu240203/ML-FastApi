import torch
import torch.nn as nn 

from torchvision.models import resnet18

class CatDogModel(nn.Module):
    def __init__(self, n_classes) -> None:
        super(CatDogModel, self).__init__()

        resnet18_model = resnet18(weights = 'IMAGENET1K_V1')
        self.backbone = nn.Sequential(*list(resnet18_model.children())[:-1])
        for param in self.backbone.parameters():
            param.requires_grad = False

        in_features = resnet18_model.fc.in_features
        self.fc = nn.Linear(in_features, n_classes)

    def forward(self, x):
        x = self.backbone(x)
        x = torch.flatten(x,1)
        x = self.fc(x)
        return x
    
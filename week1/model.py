import torch
import torch.nn as nn
from torchvision.models import resnet18

class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()

        # input 3*32*32
        # output 8
        self.conv = nn.Conv2d(
            in_channels=3,
            out_channels=8,
            kernel_size=5,
            padding=2 #31=32-5+4
        )

        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(
            kernel_size=2,
            stride=2
        )
        # 通常MaxPool2d(2, 2)会让H W减半

        self.fc = nn.Linear(
            8*16*16,10
        ) 

    def forward(self,x):
        x = self.conv(x)
        #print("conv",x.shape)
        x = self.relu(x)
        x = self.pool(x)
        #print("pool",x.shape)
        x = torch.flatten(x,1)

        x = self.fc(x)

        return x

def get_resnet18():
    model = resnet18(weights = None)

    model.fc = nn.Linear(
        model.fc.in_features,
        10
    )
    return model

if __name__ == "__main__":
    model = SimpleCNN()

    x = torch.randn(64, 3, 32, 32)

    output = model(x)

    print(output.shape)
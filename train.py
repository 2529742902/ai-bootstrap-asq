import torch
import torch.nn as nn
from torch.optim import Adam

from dataset import train_loader
from model import SimpleCNN,get_resnet18


device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

#model = SimpleCNN()
model = get_resnet18().to(device)

loss_fn = nn.CrossEntropyLoss()

optimizer = Adam(
    model.parameters(),
    lr = 0.001
)

epochs = 10
for epoch in range(epochs):

    total_loss = 0

    for images, labels in train_loader:
        images = images.to(device)
        labels = labels.to(device)

        optimizer.zero_grad() #梯度清零

        outputs = model(images)
        # print(outputs.shape) torch.Size([64, 10])
        
        loss = loss_fn(outputs,labels)

        loss.backward()#反向传播
        optimizer.step()#更新梯度

        #print(loss.item())
        total_loss += loss.item()
    average_loss = total_loss / len(train_loader)
    print(f"Epoch:{epoch},Average Loss:{average_loss}")
torch.save(model.state_dict(),"model_resnet18_augmentaion.pth")
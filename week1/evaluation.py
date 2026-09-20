import torch

from dataset import test_loader
from model import SimpleCNN,get_resnet18

device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

#model = SimpleCNN()
model = get_resnet18().to(device)


model.load_state_dict(
    torch.load("model_resnet18_augmentaion.pth")
)

model.eval() # 测试

correct = 0
total = 0

with torch.no_grad(): #不计算梯度
    for images,labels in test_loader:
        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)
        # outputs.shape 为 torch.Size([64, 10])
        prediction = outputs.argmax(dim=1) #对每个样本，在类别维度上取最大值对应的索引

        correct += (prediction == labels).sum().item() # sum把list中的true当成1相加，然后item把列表变成数字

        total += labels.size(0) #计算一个batch中的图片

accuracy = correct/total
print("Test accuracy:",accuracy)
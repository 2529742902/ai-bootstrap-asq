from torchvision.datasets import CIFAR10
from torchvision import transforms
from torch.utils.data import DataLoader


# transforms.Compose([...]) 把多个transform组合起来
transform = transforms.Compose([
    transforms.RandomCrop(32, padding=4), #在周围各补充4像素，32*32->40*40 然后在随机裁切出32*32
    # 更加鲁棒

    transforms.RandomHorizontalFlip(), # 随机进行水平翻转
    transforms.ToTensor()
])

test_transform = transforms.ToTensor()

train_dataset = CIFAR10(
    root="./data",
    train=True,
    download=True,
    transform=transform
)

test_dataset = CIFAR10(
    root="./data",
    train=False,
    download=True,
    transform=test_transform # 测试集不做随机增强
)

train_loader = DataLoader(
    train_dataset,
    batch_size = 64,
    shuffle = True
)

test_loader = DataLoader(
    test_dataset,
    batch_size= 64,
    shuffle= True
)


print("训练集大小:", len(train_dataset))
print("测试集大小:", len(test_dataset))
for images, labels in train_loader:
    print("images shape:", images.shape)
    print("labels shape:", labels.shape)
    break
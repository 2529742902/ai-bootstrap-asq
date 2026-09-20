# Week 1：图像分类 Baseline

## 1. 任务

本项目完成一个基础的图像分类任务，用于熟悉 PyTorch 中完整的深度学习训练流程：

```text
Dataset
   ↓
DataLoader
   ↓
CNN / ResNet18
   ↓
Training
   ↓
Evaluation
```

实验基于 CIFAR-10 数据集，分别使用简单 CNN 和 ResNet18 进行训练，并通过两个对照实验观察模型结构和数据增强对分类性能的影响。

---

## 2. 数据集

本项目使用 **CIFAR-10** 数据集。

CIFAR-10 共包含 60,000 张 `32 × 32` RGB 彩色图片，共 10 个类别。

- 训练集：50,000 张
- 测试集：10,000 张
- 类别数量：10

每张图片输入模型后的基本 shape 为：

```text
[3, 32, 32]
```

经过 DataLoader 组成 batch 后，例如 `batch_size=64`：

```text
[64, 3, 32, 32]
```

---

## 3. 项目结构

```text
week1/
└── image_classification/
    ├── dataset.py
    ├── model.py
    ├── train.py
    ├── evaluation.py
    ├── README.md
    └── data/
```

各文件作用：

```text
dataset.py
    CIFAR-10 数据读取、数据增强和 DataLoader

model.py
    SimpleCNN 和 ResNet18 模型定义

train.py
    模型训练、Loss 计算、反向传播和参数保存

evaluation.py
    在测试集上计算分类 Accuracy
```

---

## 4. 模型

### 4.1 SimpleCNN

首先实现了一个简单 CNN，基本结构为：

```text
Input
[3, 32, 32]

↓

Conv2d

↓

ReLU

↓

MaxPool2d

↓

Flatten

↓

Linear

↓

10-class logits
```

用于建立最基础的图像分类 baseline。

---

### 4.2 ResNet18

第二个模型使用 torchvision 提供的 ResNet18：

```python
resnet18(weights=None)
```

本实验不使用 ImageNet 预训练权重，而是从随机初始化开始训练。

由于原始 ResNet18 最后的全连接层输出 1000 类，因此将最后的分类层修改为：

```python
model.fc = nn.Linear(
    model.fc.in_features,
    10
)
```

使模型适配 CIFAR-10 的 10 分类任务。

---

## 5. 训练设置

主要训练参数：

```text
Epochs: 10
Batch Size: 64
Optimizer: Adam
Learning Rate: 0.001
Loss Function: CrossEntropyLoss
```

每个 batch 的训练流程：

```text
images
   ↓
Model
   ↓
logits
   ↓
CrossEntropyLoss
   ↓
loss.backward()
   ↓
optimizer.step()
```

训练前通过：

```python
optimizer.zero_grad()
```

清空上一轮累计的梯度。

---

## 6. 运行方法

### 训练模型

```bash
python train.py
```

训练完成后保存模型参数：

```python
torch.save(model.state_dict(), "model.pth")
```

### 测试模型

```bash
python evaluation.py
```

Evaluation 阶段使用：

```python
model.eval()
```

并通过：

```python
with torch.no_grad():
```

关闭梯度计算。

最终使用测试集计算分类 Accuracy。

---

## 7. 对照实验

### 实验 1：SimpleCNN vs ResNet18

保持数据集和基本训练设置不变，只改变模型结构。

| Model | Epochs | Final Train Loss | Test Accuracy |
|---|---:|---:|---:|
| SimpleCNN | 10 | 1.1727 | 58.22% |
| ResNet18 | 10 | 0.2391 | 73.26% |

结果显示：

```text
58.22% → 73.26%
```

ResNet18 相比 SimpleCNN 的测试准确率提高了 **15.04 个百分点**。

这说明更深的网络结构以及 ResNet 中的残差连接能够学习到更强的图像特征表示。

---

### 实验 2：有无 Data Augmentation

在 ResNet18 上进一步加入数据增强：

```python
train_transform = transforms.Compose([
    transforms.RandomCrop(32, padding=4),
    transforms.RandomHorizontalFlip(),
    transforms.ToTensor()
])
```

测试集不进行随机数据增强：

```python
test_transform = transforms.ToTensor()
```

实验结果：

| Model | Data Augmentation | Final Train Loss | Test Accuracy |
|---|---|---:|---:|
| ResNet18 | No | 0.2391 | 73.26% |
| ResNet18 | Yes | 0.6466 | 76.03% |

加入数据增强后：

```text
73.26% → 76.03%
```

测试准确率提高了 **2.77 个百分点**。

虽然加入数据增强后的训练 loss 更高，但测试准确率反而更高。

这是因为随机裁剪和水平翻转增加了训练数据的变化，使模型更难直接记住训练样本，从而提升了对测试数据的泛化能力。

---

## 8. 最终结果

本项目得到的最佳结果为：

```text
Model: ResNet18
Data Augmentation: RandomCrop + RandomHorizontalFlip
Epochs: 10
Test Accuracy: 76.03%
```

整体实验结果：

| Experiment | Model | Augmentation | Test Accuracy |
|---|---|---|---:|
| Baseline | SimpleCNN | No | 58.22% |
| Experiment 1 | ResNet18 | No | 73.26% |
| Experiment 2 | ResNet18 | Yes | **76.03%** |

---

## 9. 学到了什么

通过这个项目，我完成了第一次完整的 PyTorch 图像分类训练流程。

### 1. Dataset 和 DataLoader

理解了 Dataset 负责读取单个样本，而 DataLoader 负责将多个样本组成 batch：

```text
Dataset
   ↓
image, label
   ↓
DataLoader
   ↓
images, labels
```

---

### 2. CNN 中 Tensor shape 的变化

理解了图片在 CNN 中的基本数据流，例如：

```text
[64, 3, 32, 32]
        ↓ Conv
[64, C, 32, 32]
        ↓ Pool
[64, C, 16, 16]
        ↓ Flatten
[64, features]
        ↓ Linear
[64, 10]
```

其中最后的 10 对应 CIFAR-10 的 10 个类别。

---

### 3. Training Loop

理解了基本训练流程：

```python
optimizer.zero_grad()

outputs = model(images)

loss = loss_fn(outputs, labels)

loss.backward()

optimizer.step()
```

其中：

- `zero_grad()`：清空梯度
- `backward()`：通过反向传播计算梯度
- `step()`：根据梯度更新模型参数

---

### 4. Training 和 Evaluation 的区别

训练阶段需要计算梯度并更新参数，而测试阶段只进行前向传播。

Evaluation 使用：

```python
model.eval()

with torch.no_grad():
```

避免不必要的梯度计算。

---

### 5. Train Loss 低不代表泛化一定更好

实验中：

```text
ResNet18 without augmentation
Train Loss: 0.2391
Test Accuracy: 73.26%

ResNet18 with augmentation
Train Loss: 0.6466
Test Accuracy: 76.03%
```

虽然数据增强后的训练 loss 更高，但 Test Accuracy 更高。

因此模型训练时不能只关注训练 loss，还需要通过独立测试集观察模型的泛化能力。

---

### 6. 模型结构对性能有明显影响

SimpleCNN 的测试准确率为：

```text
58.22%
```

ResNet18 提升到了：

```text
73.26%
```

说明更强的模型结构能够提取更加有效的图像特征。

---

## 10. 总结

本项目完成了：

```text
CIFAR-10
   ↓
Dataset / DataLoader
   ↓
SimpleCNN / ResNet18
   ↓
Training
   ↓
Evaluation
   ↓
Model Comparison
   ↓
Data Augmentation
```

最终最佳 Test Accuracy 为：

```text
76.03%
```

通过两个简单对照实验，初步理解了 **模型结构、数据增强、训练 loss 和模型泛化能力之间的关系**。

import os
import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from torch.utils.data import DataLoader

train_dir = os.path.join("data/train")
test_dir = os.path.join("data/test")
meta_file = os.path.join("meta.csv")


# 定义图像预处理
transform = transforms.Compose([
    transforms.Resize(218),
    transforms.CenterCrop(218),
    transforms.RandomHorizontalFlip(),
    transforms.RandomVerticalFlip(),
    transforms.ToTensor(),
    # transforms.Normalize(mean=[0.485, 0.456, 0],std=[0.229, 0.224, 0.225])
])

# 加载训练集
train_dataset = torchvision.datasets.ImageFolder(train_dir, transform=transform)

# 加载测试集
test_dataset = torchvision.datasets.ImageFolder(test_dir, transform=transform)

# 加载类别标签
with open(meta_file, "r") as f:
    labels = [line.strip().split(",")[1] for line in f]

# 构建 ResNet50 模型
model = torchvision.models.resnet101()

# 修改最后一层
model.fc = nn.Linear(model.fc.in_features, len(labels))
print(len(labels))
train_loader = DataLoader(
    train_dataset,      # Pass the training dataset
    batch_size=5,  # Adjust batch size as needed
    shuffle=True    # Shuffle the data for better training
)

test_loader = DataLoader(
    test_dataset,      # Pass the training dataset
    batch_size=5,  # Adjust batch size as needed
    shuffle=True    # Shuffle the data for better training
)


# 定义损失函数和优化器
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# 训练模型
epochs = 5

for epoch in range(epochs):
    # 训练
    for i, (images, labels) in enumerate(train_loader):
        # 前向传播
        outputs = model(images)
        # 计算损失
        loss = criterion(outputs, labels)
        # 反向传播
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    # 打印训练信息
    if epoch % 1 == 0:
        print("Epoch: {} Loss: {:.4f}".format(epoch, loss.item()))


# 测试模型
correct = 0
total = 0
for images, labels in test_loader:
    outputs = model(images)
    _, predicted = torch.max(outputs.data, 1)
    total += labels.size(0)
    correct += (predicted == labels).sum().item()

# 计算准确率
accuracy = correct / total
print("Accuracy: {:.4f}".format(accuracy))

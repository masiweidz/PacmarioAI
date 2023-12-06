import torch
import numpy as np
from torchvision import transforms
from PIL import Image

# 定义观察数据的预处理转换
transform = transforms.Compose([
    transforms.ToPILImage(),          # 将 numpy 数组转换为 PIL 图像
    transforms.Resize((84, 84)),      # 调整图像大小
    transforms.Grayscale(),           # 转换为灰度图像
    transforms.ToTensor(),            # 转换为 PyTorch 张量
    transforms.Normalize((0.5,), (0.5,))  # 标准化
])

def process_observation(observation):
    """
    处理环境观察数据。

    参数:
    observation: 从环境获得的原始观察数据，通常是一个 numpy 数组。

    返回:
    处理后的观察数据，作为 PyTorch 张量。
    """
    # 如果观察数据是 numpy 数组，先将其转换为 PIL 图像
    if isinstance(observation, np.ndarray):
        observation = Image.fromarray(observation)

    # 应用预处理转换
    observation = transform(observation).unsqueeze(0)  # 添加一个批次维度
    return observation
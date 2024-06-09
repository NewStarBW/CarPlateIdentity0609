# 初夏 2024/6/9 20:07 plate_divide
import os
import shutil
import random

def split_dataset(input_folder, train_folder, test_folder, split_ratio=0.8):
    # 创建训练集和测试集文件夹
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    # 遍历输入文件夹中的所有文件和子文件夹
    for root, dirs, files in os.walk(input_folder):
        for filename in files:
            # 获取文件的绝对路径
            filepath = os.path.join(root, filename)
            # 获取文件的相对路径（相对于输入文件夹）
            relative_path = os.path.relpath(filepath, input_folder)

            # 随机决定将文件放入训练集还是测试集
            if random.random() < split_ratio:
                output_folder = os.path.join(train_folder, os.path.dirname(relative_path))
            else:
                output_folder = os.path.join(test_folder, os.path.dirname(relative_path))

            # 创建输出文件夹（如果不存在）
            os.makedirs(output_folder, exist_ok=True)

            # 复制文件到相应的输出文件夹中
            shutil.copy(filepath, output_folder)

# 设置输入文件夹和输出文件夹
input_folder = "../carIdentityData/cnn_plate_train1"
train_folder = "../carIdentityData/cnn_plate_train"
test_folder = "../carIdentityData/cnn_plate_test"

# 划分数据集（默认80%训练集，20%测试集）
split_dataset(input_folder, train_folder, test_folder)

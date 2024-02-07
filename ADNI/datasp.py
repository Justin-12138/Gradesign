import os
import random
import shutil

def split_dataset(source_folder, train_ratio=0.7, test_ratio=0.2, val_ratio=0.1):
    # 获取文件列表
    file_list = os.listdir(source_folder)
    
    # 随机打乱文件列表
    random.shuffle(file_list)
    
    # 计算切分索引
    num_files = len(file_list)
    train_split = int(num_files * train_ratio)
    test_split = int(num_files * (train_ratio + test_ratio))
    
    # 划分数据集
    train_set = file_list[:train_split]
    test_set = file_list[train_split:test_split]
    val_set = file_list[test_split:]
    
    # 创建目标文件夹
    dest_train_folder = os.path.join(source_folder, 'train')
    dest_test_folder = os.path.join(source_folder, 'test')
    dest_val_folder = os.path.join(source_folder, 'val')
    
    os.makedirs(dest_train_folder, exist_ok=True)
    os.makedirs(dest_test_folder, exist_ok=True)
    os.makedirs(dest_val_folder, exist_ok=True)
    
    # 将文件复制到目标文件夹
    for file in train_set:
        shutil.copy(os.path.join(source_folder, file), os.path.join(dest_train_folder, file))
    
    for file in test_set:
        shutil.copy(os.path.join(source_folder, file), os.path.join(dest_test_folder, file))
    
    for file in val_set:
        shutil.copy(os.path.join(source_folder, file), os.path.join(dest_val_folder, file))

# 使用示例
split_dataset('slice/x/AD')  # 替换 'AD' 为你的文件夹路径
split_dataset('slice/x/CN')  # 替换 'CN' 为你的文件夹路径
split_dataset('slice/x/MCI')  # 替换 'MCI' 为你的文件夹路径


split_dataset('slice/y/AD')  # 替换 'AD' 为你的文件夹路径
split_dataset('slice/y/CN')  # 替换 'CN' 为你的文件夹路径
split_dataset('slice/y/MCI')


split_dataset('slice/z/AD')  # 替换 'AD' 为你的文件夹路径
split_dataset('slice/z/CN')  # 替换 'CN' 为你的文件夹路径
split_dataset('slice/z/MCI')



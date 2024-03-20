import os
import shutil
import numpy as np

# 定义源目录和目标目录
src_dirs = ['AD', 'MCI', 'CN']
dst_dirs = ['train', 'test', 'val']

# 创建目标目录结构
for dst in dst_dirs:
    for src in src_dirs:
        os.makedirs(os.path.join(dst, src), exist_ok=True)

# 定义分配比例
ratios = [0.6, 0.3, 0.1]

# 将文件按比例分配到目标目录
for src in src_dirs:
    files = os.listdir(src)
    np.random.shuffle(files)
    
    split_points = np.cumsum([0] + ratios)
    split_indices = [int(round(point * len(files))) for point in split_points]
    
    for dst, start, end in zip(dst_dirs, split_indices[:-1], split_indices[1:]):
        for file in files[start:end]:
            shutil.copy(os.path.join(src, file), os.path.join(dst, src, file))


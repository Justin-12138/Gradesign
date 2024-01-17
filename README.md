# 基于图神经网络的AD分类研究

#### Update

+ **2024.01.15:背景调查,以及数据预处理**

#### TODO

- [x] 基本的数据预处理
- [ ] 常见的神经网络模型
- [ ] 图神经网络

#### Tools

```latex
python==3.10.8
itksnap-4.0.2-20230925-Linux-gcc64
fsl
```

#### Dataset

+ 数据集介绍

  ```latex
  1. 数据预处理： ADNI的数据通常已经进行了一些预处理，包括强度标准化和梯度去扭曲1。但是，您可能还需要进行以下步骤：
  脑提取：移除非脑部分，例如使用FSL的BET工具。
  图像配准：将所有图像对齐到一个公共空间，例如使用FSL的FLIRT工具。
  偏差场校正：纠正MRI图像的光照不均，例如使用N4方法。
  强度归一化：将图像的强度范围标准化到[-1,1]
  在Python中，可以使用nibabel库来读取和处理NiFTI格式的数据
  2. 特征提取： 取决于打算使用的模型。对于传统的机器学习模型，可能需要提取一些手工特征，例如基于区域的灰度强度统计或基于体素的特征。对于深度学习模型，可以直接使用原始像素值作为输入。
  3. 模型建立和训练： 有许多方法可以用于阿尔茨海默病的图像分类，包括：
  机器学习方法：例如支持向量机5、决策树、随机森林和梯度提升6等。
  神经网络方法：包括卷积神经网络78和深度神经网络7。
  图神经网络方法：例如Graph Convolutional Neural Networks910。
  在Python中，可以使用scikit-learn库来实现传统的机器学习模型，使用TensorFlow或PyTorch来实现神经网络模型。
  4. 模型评估： 使用交叉验证来评估模型的性能。计算准确率、召回率、F1分数等指标。
  https://adni.loni.usc.edu/methods/mri-tool/mri-analysis/#mri-pre-processing-container
  ```

+ 数据预处理

+ 

  + 从ADNI下载数据集
    ```latex
    https://adni.loni.usc.edu
    ```
  
  + 去掉重复的数据
  
    ```latex
    #!/bin/bash
    cd .
    for dir in $(ls -d */); do
      cd $dir
      subdirs=(*/)
      for ((i=1; i<${#subdirs[@]}; i++)); do
        rm -r ${subdirs[$i]}
      done
      cd ..
    done
    ```
  
    ![image-20240116225634983](/home/lz/snap/typora/86/.config/Typora/typora-user-images/image-20240116225634983.png)
    
  
  + 提取出所有的.nii文件
    ```latex
    #!/bin/bash
    
    cd ./
    mkdir -p data
    for dir in */; do
      dir_name=${dir%/}
      last_nii_file=$(find "$dir" -name "*.nii" | tail -1)
      if [[ -n $last_nii_file ]]; then
        cp "$last_nii_file" "data/${dir_name}.nii"
      fi
    done
    ```
  
  + 颅骨剥离
  
    ```latex
    #!/bin/bash
    input_dir="data"
    output_dir="process"
    mkdir -p $output_dir
    for file in $input_dir/*.nii
    do
      base_name=$(basename $file .nii)
      output_file="$output_dir/${base_name}_brain.nii.gz"
      bet2 $file $output_file -f 0.5
    done
    在使用 FSL 的 BET 工具进行脑提取时，会生成以下三个文件：
    T1Flair_brain_mask.nii.gz：这是一个二值图像，其中脑部的体素被标记为1，非脑部的体素被标记为0。
    T1Flair_brain.nii.gz：这是原始图像，但是所有非脑部的体素都被设置为0。这意味着，这个图像只包含脑部的信息。
    T1Flair_brain_overlay.nii.gz：这是一个叠加图像，它将脑提取的结果（即脑部）叠加在原始图像上。这个图像可以用来检查脑提取的结果是否准确。
    
    ```
  
    ![image-20240116225715118](/home/lz/snap/typora/86/.config/Typora/typora-user-images/image-20240116225715118.png)
  
  + 平均配准
  
    ```latex
    #创建平均图像：将所有图像配准到一个初始的参考图像，然后创建一个平均图像，再将所有图像配准到这个平均图像。
    
    # 先选取一个作为参考reference.nii.gz
    cd ./data
    for file in *.nii.gz;
    do
      flirt -in $file -ref reference.nii.gz -out registered_$file -omat registered_$file.mat
    done
    
    # 设置第一个图像为平均图像
    cp $(ls *.nii.gz | head -1) average.nii.gz
    for file in $(ls *.nii.gz | tail -n +2); do
      fslmaths average.nii.gz -add $file average.nii.gz
    done
    num_images=$(ls *.nii.gz | wc -l)
    fslmaths average.nii.gz -div $num_images average.nii.gz
    
    # 将所有图像配准到这个平均图像。
    cd ./new_folder
    for file in *.nii.gz; do
      flirt -in $file -ref average.nii.gz -out avg$file -omat avg_$file.mat
    done
    ```
  
    ![image-20240116225822658](/home/lz/snap/typora/86/.config/Typora/typora-user-images/image-20240116225822658.png)
  
  + 偏差场校正加归一化：纠正MRI图像的光照不均，例如使用N4方法。
    ```latex
    import os
    import concurrent.futures
    import SimpleITK as sitk
    
    def process_file(file_path):
        input_image = sitk.ReadImage(file_path)
        mask_image = sitk.OtsuThreshold(input_image, 0, 1, 200)
        input_image = sitk.Cast(input_image, sitk.sitkFloat32)
        corrector = sitk.N4BiasFieldCorrectionImageFilter()
        output_image = corrector.Execute(input_image, mask_image)
        output_image = sitk.Cast(output_image, sitk.sitkInt16)
        output_filename = os.path.splitext(os.path.basename(file_path))[0] + '_N4.nii.gz'
        output_path = os.path.join('N4', output_filename)
        sitk.WriteImage(output_image, output_path)
    
    
    nii_files = [f for f in os.listdir('.') if f.endswith('.nii.gz')]
    if not os.path.exists('N4'):
        os.makedirs('N4')
    # 多线程
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(process_file, nii_files)
    ```
  
    ![image-20240116225853688](/home/lz/snap/typora/86/.config/Typora/typora-user-images/image-20240116225853688.png)


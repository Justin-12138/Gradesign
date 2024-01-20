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

  + 原始图像

    <img src="/home/lz/snap/typora/86/.config/Typora/typora-user-images/image-20240119151051485.png" alt="image-20240119151051485" style="zoom:25%;" />

  + 颅骨剥离

    <img src="/home/lz/snap/typora/86/.config/Typora/typora-user-images/image-20240119015518284.png" alt="image-20240119015518284" style="zoom:25%;" />

    

  + 配准(182x218x182)

  <img src="/home/lz/snap/typora/86/.config/Typora/typora-user-images/image-20240119015700542.png" alt="image-20240119015700542" style="zoom:25%;" />

  + 高斯平滑

  <img src="/home/lz/snap/typora/86/.config/Typora/typora-user-images/image-20240119015751695.png" alt="image-20240119015751695" style="zoom:25%;" />

  

  + 灰度归一化(使用fsleyes展示，itksnap只支持16位精度)

    ![image-20240119020106590](/home/lz/snap/typora/86/.config/Typora/typora-user-images/image-20240119020106590.png)

  + 切片(182x218x182)
    
    90,100,90
    
    ![](/home/lz/repo/Gradesign/imgs/slice.png)
    
    9,18,9
    
    ![](/home/lz/repo/Gradesign/imgs/Figure_2.png)
    
    170,200,170
    
    ![](/home/lz/repo/Gradesign/imgs/Figure_3.png)


  + 

    
    
  + 

    

  + 

    
    
  + 

    


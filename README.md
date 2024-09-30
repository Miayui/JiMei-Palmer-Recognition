# JiMei-Palmer-Recognition
    本仓库主要用作集美队比赛数据交流，目前暂定包含内容如下：
    -dataset
    -初步架构代码
    |-代码
    |-环境配置
# 掌纹Dataset（维护人：huang）
| 数据集名称  | type | 采集环境 | 对象个数 | 图片个数 | 特别说明 |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| CASIA-PalmprintV1  | 非接触式  | 控制环境 | 312 | 5502 |  |
| CASIA-Multi-Spectral-PalmprintV1  | 非接触式  | 控制环境 | 100 | 7200 | 采用多光谱技术采集，数据集包含静脉信息 |
## CASIA-PalmprintV1
说明详见/dataset/Palmprint/CASIA-PalmprintV1/Note_CASIA-PalmprintV1.pdf
## CASIA-Multi_Spectral-PlamprintV1
说明详见/dataset/Palmprint/CASIA-Multi-Spectral-PalmprintV1/Database description.pdf
# 初步架构代码（维护人：li）
## 处理流程
### 图像预处理
- 灰度化：将彩色图像转换为灰度图像。
- 去噪：使用高斯滤波或中值滤波去除图像噪声。
- 增强：使用直方图均衡化或对比度调整来增强图像质量。
### 手掌定位
- 边缘检测：使用Canny边缘检测算法或Sobel算子检测图像边缘。
- 轮廓提取：使用轮廓检测算法（如OpenCV的findContours）提取手掌轮廓。
- 最小外接矩形：找到手掌轮廓的最小外接矩形，以确定手掌的大致位置。
### ROI提取
- 裁剪：根据最小外接矩形裁剪出手掌区域。
- 归一化：将裁剪后的手掌区域调整到固定大小，以便于后续处理。
### 特征提取模型
#### 传统方式
- 纹理特征：使用**Gabor滤波器**、LBP（局部二值模式）等方法提取掌纹纹理特征。
- 几何特征：提取手掌的几何特征，如手指间距、手掌宽度等。
#### 深度学习 （也可以端到端-提取+分类一个模型）
- resnet
### 特征分类模型
建立掌纹特征库
### 掌纹信息匹配

## 代码说明


# 可参考资料
## 数据集
|链接|说明|
|:---|:--|
| https://github.com/Lin-Dxin/PalmprintRecognition| 深度学习训练+数据集|
|https://github.com/ruofei7/Palmprint_Recognition | 机器学习+数据集|

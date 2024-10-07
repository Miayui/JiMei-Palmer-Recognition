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
## 数据集格式
![image](https://github.com/user-attachments/assets/299b8413-b95a-4381-bace-473253cac3a4)


## 处理流程
### 图像预处理
- [x] 手掌定位
- [x] ROI提取
## 特征提取
- [] 特征分类模型
- [] 建立掌纹特征库
## 掌纹信息匹配
- [] test
## 代码说明


# 可参考资料
## 数据集
|链接|说明|
|:---|:--|
| https://github.com/Lin-Dxin/PalmprintRecognition| 深度学习训练+数据集|
|https://github.com/ruofei7/Palmprint_Recognition | 机器学习+数据集|

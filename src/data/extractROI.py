import math
import cv2
import numpy as np
import mediapipe as mp
from glob import glob
import os

debug = 1


class ExtractROI():
    def __init__(self,images_dir,save_dir) -> None:
        self.images_dir=images_dir
        if save_dir=="":
            self.save_dir=images_dir
        else:
            self.save_dir=save_dir
        self.process_images(self.images_dir,self.save_dir)
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
    
    

    def read_image(self,path):
        image = cv2.imread(path, 1)
        # image= cv2.flip(image,1)
        if image is None:
            print('图片没读到')
            exit(0)
        return image
    
    def key_points_detect(self,image_path):
        image=self.read_image(image_path)
        key_points_list=[0,5,9,13,17]
        detect_correct=False
        cropped_image=None
        mp_hands = mp.solutions.hands
        hands = mp_hands.Hands(
                static_image_mode=True,  #图片就要设置成True,视频设置为false
                max_num_hands=2,
                min_detection_confidence=0.5,  #手部检测的最小置信度值，大于这个数值被认为是成功的检测。默认为0.5
                min_tracking_confidence=0.5)
        results = hands.process(image)
        # print(results.multi_handedness)
        # print(results.multi_hand_landmarks)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            key_points=[]
            for hand_landmarks in results.multi_hand_landmarks:
                for id, lm in enumerate(hand_landmarks.landmark):
                    # 归一化坐标转换为图像坐标
                    if not id in key_points_list:
                        continue
                    # print(lm)
                    cx, cy = int(lm.x * image.shape[1]), int(lm.y * image.shape[0])
                    key_points.append([cx,cy])
            # 创建一个与原图大小相同的黑色掩码
            mask = np.zeros_like(image[:, :, 0])
            if len(key_points)==5:
                detect_correct=True
            key_points=np.array(key_points,dtype=np.int32)
            # 使用关键点构建多边形
            # print(key_points)
            # print(image.shape)
            cv2.fillPoly(mask, [key_points], 255)
            # 使用掩码提取 ROI
            masked_image = cv2.bitwise_and(image, image, mask=mask)
            binary=cv2.cvtColor(masked_image,cv2.COLOR_RGB2GRAY)
            contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # 遍历每个轮廓
            for contour in contours:
                # 计算轴对齐的最小内接矩形
                x, y, w, h = cv2.boundingRect(contour)
                
                # 在原图上绘制矩形
                cv2.rectangle(masked_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cropped_image =masked_image[y:y+h, x:x+w]
            # cv2.imshow('Hand Landmarks', cropped_image)
            # cv2.waitKey(0)
        return detect_correct,cropped_image



    def process_images(self,image_dir,save_dir):
        image_pathes=glob(os.path.join(image_dir,"*.jpg"))
        
        correct=0
        all=0
        for image_path in image_pathes:
            detect_correct,cropped_image=self.key_points_detect(image_path)
            if detect_correct:
                image_name=image_path.split("\\")[-1]
                if "detect" in image_name:
                    continue
                dst_name=image_name.replace(".jpg","_detect.jpg")
                save_path=os.path.join(save_dir,dst_name)
                cv2.imwrite(save_path,cropped_image)
                correct+=1
            all+=1
            print("detect rate: ",correct/all," detect num: ",correct," all num:",all)


if __name__=="__main__":
    # img_path = r'JiMei-Palmer-Recognition\test_data\002_l_460_06.jpg'

    # key_points_detect(img_path)

    images_dir="JiMei-Palmer-Recognition\\JiMei-Palmer-Recognition\\test_data"
    extracr=ExtractROI(images_dir,"")

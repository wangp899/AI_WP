"""
图像滤波演示
"""
import cv2 
import numpy as np 
cap = cv2.VideoCapture(0) 
# 浮雕滤波
kernel = np.array([[-2, -1, 0], 
                   [-1, 1, 1], 
                   [0, 1, 2]], dtype="float32")
# 平均模糊 
#kernel = np.ones([8, 8])/64 
## 纵向边缘 
##kernel = np.ones([8, 8]) 
#kernel[:, :4] = -1 
# 横向边缘 
#kernel = np.ones([8, 8]) 
#kernel[:4, :] = -1
while True:
    _, img = cap.read() 
    img_flt = cv2.filter2D(img, -1, kernel)
    cv2.imshow("a", img_flt) 
    ret = cv2.waitKey(100)
    print(ret)
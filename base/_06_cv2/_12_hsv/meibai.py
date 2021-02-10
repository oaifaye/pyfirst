# coding=utf-8
#================================================================
#
#   File name   : meibai.py
#   Author      : Faye
#   Created date: 2021/2/8 10:36 
#   Description :
#
'''

美肤-磨皮算法

Dest =(Src * (100 - Opacity) + (Src + 2 * GuassBlur(EPFFilter(Src) - Src + 128) - 256) * Opacity) /100 ;

'''
#================================================================


import cv2

import numpy as np

def beauty_face(img):

    dst = np.zeros_like(img)
    #int value1 = 3, value2 = 1; 磨皮程度与细节程度的确定
    v1 = 3
    v2 = 1
    dx = v1 * 5 # 双边滤波参数之一
    fc = v1 * 12.5 # 双边滤波参数之一
    p = 0.1
    temp4 = np.zeros_like(img)
    temp1 = cv2.bilateralFilter(img,dx,fc,fc)
    temp2 = cv2.subtract(temp1,img);
    temp2 = cv2.add(temp2,(10,10,10,128))
    temp3 = cv2.GaussianBlur(temp2,(2*v2 - 1,2*v2-1),0)
    temp4 = cv2.add(img,temp3)
    dst = cv2.addWeighted(img,p,temp4,1-p,0.0)
    dst = cv2.add(dst,(10, 10, 10,255))
    return dst

img = cv2.imread(r'G:\datasets\smile_data\my_face\face_res1\b_00024_1_-2.jpg')
dst = beauty_face(img)
cv2.imshow("SRC", img)
cv2.imshow("DST", dst)
whi = 0.5
white = np.uint8(np.clip((whi * dst + 10), 0, 255))
cv2.imshow("white", white)

cv2.waitKey()
cv2.destroyAllWindows()

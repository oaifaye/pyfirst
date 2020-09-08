# encoding: utf-8
from __future__ import division
import sys

import cv2
import numpy as np

#读取原图
image=cv2.imread("_04_lena.jpg")
cv2.imshow('original',image)




#低通滤波器
kernel1=np.array([[0.11,0.11,0.11],[0.11,0.11,0.11],[0.11,0.11,0.11]])
rect=cv2.filter2D(image,-1,kernel1)
# cv2.imwrite("_04_img/rect.jpg",rect)
cv2.imshow('rect',rect)

#高斯滤波器
kernel2=np.array([[1,4,7,4,1],[4,16,26,16,4],[7,26,41,26,7],[4,16,26,16,4],[1,4,7,4,1]])/273.0
gaussian=cv2.filter2D(image,-1,kernel2)
# cv2.imwrite("_04_img/gaussian.jpg",gaussian)
cv2.imshow('gaussian',gaussian)

#锐化滤波器
kernel3=np.array([[0,-2,0],[-2,9,-2],[0,-2,0]])
sharpen=cv2.filter2D(image,-1,kernel3)
# cv2.imwrite("_04_img/sharpen.jpg",sharpen)
cv2.imshow('sharpen',sharpen)

#边缘检测
kernel4=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
edges=cv2.filter2D(image,-1,kernel4)
# cv2.imwrite("_04_img/edges.jpg",edges)
cv2.imshow('edges',edges)

#浮雕滤波器
# kernel5=np.array([[-2,-2,-2,-2,0],[-2,-2,-2,0,2],[-2,-2,0,2,2],[-2,0,2,2,2],[0,2,2,2,2]])
# emboss=cv2.filter2D(image,-1,kernel5)
# emboss=cv2.cvtColor(emboss,cv2.COLOR_BGR2GRAY)
# # cv2.imwrite("_04_img/emboss.jpg",emboss)
# cv2.imshow('emboss',emboss)

cv2.waitKey(0)
cv2.destroyAllWindows()
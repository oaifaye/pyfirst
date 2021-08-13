# coding=utf-8
#================================================================
#
#   File name   : _07_warpAffine.py
#   Author      : Faye
#   Created date: 2020/7/14 8:06 
#   Description : 仿射
#
#================================================================

import cv2
import numpy as np
import matplotlib.pylab  as plt

img = cv2.imread('_07_img/31.jpg')
rows,cols,ch = img.shape
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# pts1 = np.float32([[50,50],[200,50],[50,200]])
# pts2 = np.float32([[10,100],[200,50],[100,250]])

pts1 = np.float32([[0,0],[332,30],[694,22]])
pts2 = np.float32([[0,0],[332,22],[694,0]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(cols,rows), borderValue=226)
cv2.imwrite('_07_img/31_1.jpg', dst)
# plt.subplot(121),plt.imshow(img),plt.title('Input')
# plt.subplot(122),plt.imshow(dst),plt.title('Output')
# plt.show()

# 平移
img = cv2.imread('_07_img/roi.jpg')
rows, cols = img.shape[:2]
# 定义平移矩阵，需要是numpy的float32类型
# x轴平移100，y轴平移50, 2*3矩阵
M = np.float32([[1, 0, 100], [0, 1, 50]])
# 用仿射变换实现平移
img_s = cv2.warpAffine(img, M, (cols, rows), borderValue=(155, 150, 200))
cv2.imshow('1', img)
cv2.imshow('2', img_s)
cv2.waitKey(0)
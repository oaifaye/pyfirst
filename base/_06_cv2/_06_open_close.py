# coding=utf-8
#================================================================
#
#   File name   : _06_open.py
#   Author      : Faye
#   Created date: 2020/7/10 15:54 
#   Description :
#   cv2的开运算 闭运算
#================================================================

import cv2

img = cv2.imread('_06_img/2.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = cv2.blur(gray, (5, 5))

sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, ksize=3)

# 二值化
ret, binary = cv2.threshold(sobel, 128, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)
# cv2.imshow('binary', binary)
# cv2.waitKey(0)
# 膨胀、腐蚀
# element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 9))
# element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (24, 6))
element1 = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
element2 = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 3))

# 膨胀一次，让轮廓突出
dilation = cv2.dilate(binary, element2, iterations=1)
cv2.imshow('1', dilation)
cv2.waitKey(0)

# 腐蚀一次，去掉细节
erosion = cv2.erode(dilation, element1, iterations=1)
cv2.imshow('2', dilation)
cv2.waitKey(0)

# 再次膨胀，让轮廓明显一些
dilation2 = cv2.dilate(erosion, element2, iterations=2)

cv2.imshow('3', dilation2)
cv2.waitKey(0)
# encoding: utf-8
from __future__ import division
import sys

import cv2
import numpy as np



#读取原图
image = cv2.imread("_04_lena.jpg")
cv2.imshow('original', image)

'''
中值滤波器是一种常用的非线性滤波器，其基本原理是：选择待处理像素的一个邻域中各像素值的中值来代替待处理的像素。
主要功能使某像素的灰度值与周围领域内的像素比较接近，从而消除一些孤立的噪声点，所以中值滤波器能够很好的消除椒盐噪声。
不仅如此，中值滤波器在消除噪声的同时，还能有效的保护图像的边界信息，不会对图像造成很大的模糊（相比于均值滤波器）。
中值滤波器的效果受滤波窗口尺寸的影响较大，在消除噪声和保护图像的细节存在着矛盾：滤波窗口较小，则能很好的保护图像中的某些细节，但对噪声的过滤效果就不是很好，
因为实际中的噪声不可能只占一个像素位置；反之，窗口尺寸较大有较好的噪声过滤效果，但是会对图像造成一定的模糊。
另外，根据中值滤波器原理，如果在滤波窗口内的噪声点的个数大于整个窗口内非噪声像素的个数，则中值滤波就不能很好的过滤掉噪声。
'''
medianBlur=cv2.medianBlur(image,5)
cv2.imshow('medianBlur', medianBlur)
print('中值滤波器完成')

'''
    自适应中值滤波算法
    自适应滤波器不但能够滤除概率较大的椒盐噪声，而且能够更好的保护图像的细节，这是常规的中值滤波器做不到的。
    自适应的中值滤波器也需要一个矩形的窗口 ，和常规中值滤波器不同的是这个窗口的大小会在滤波处理的过程中进行改变（增大）。
 '''
def AdaptProcess(src, i, j, minSize, maxSize):
    filter_size = minSize
    kernelSize = filter_size // 2
    rio = src[i-kernelSize:i+kernelSize+1, j-kernelSize:j+kernelSize+1]
    minPix = np.min(rio)
    maxPix = np.max(rio)
    medPix = np.median(rio)
    zxy = src[i,j]
    if (medPix > minPix) and (medPix < maxPix):
        if (np.mean(zxy) > minPix) and (np.mean(zxy) < maxPix):
            return zxy
        else:
            return medPix
    else:
        filter_size = filter_size + 2
        if filter_size <= maxSize:
            return AdaptProcess(src, i, j, filter_size, maxSize)
        else:
            return medPix
def adapt_meadian_filter(img, minsize, maxsize):
    borderSize = maxsize // 2
    src = cv2.copyMakeBorder(img, borderSize, borderSize, borderSize, borderSize, cv2.BORDER_REFLECT)
    for m in range(borderSize, src.shape[0] - borderSize):
        for n in range(borderSize, src.shape[1] - borderSize):
            src[m,n] = AdaptProcess(src, m, n, minsize, maxsize)
    dst = src[borderSize:borderSize+img.shape[0], borderSize:borderSize+img.shape[1]]
    return dst
# adaptMeadianFilter = adapt_meadian_filter(image,5,10)
# cv2.imshow('adapt_meadian_filter', adaptMeadianFilter)
# print('自适应中值滤波器完成')

#低通滤波器
kernel1=np.array([[0.11,0.11,0.11],
                  [0.11,0.11,0.11],
                  [0.11,0.11,0.11]])
rect=cv2.filter2D(image,-1,kernel1)
# cv2.imwrite("_04_img/rect.jpg",rect)
cv2.imshow('rect',rect)
print('低通滤波器完成')

#高斯滤波器
kernel2=np.array([[1,4,7,4,1],
                  [4,16,26,16,4],
                  [7,26,41,26,7],
                  [4,16,26,16,4],
                  [1,4,7,4,1]])/273.0
gaussian=cv2.filter2D(image,-1,kernel2)
# cv2.imwrite("_04_img/gaussian.jpg",gaussian)
cv2.imshow('gaussian',gaussian)
print('高斯滤波器完成')

#锐化滤波器
kernel3=np.array([[0,-2,0],
                  [-2,9,-2],
                  [0,-2,0]])
sharpen=cv2.filter2D(image,-1,kernel3)
# cv2.imwrite("_04_img/sharpen.jpg",sharpen)
cv2.imshow('sharpen',sharpen)
print('锐化滤波器完成')

#边缘检测
kernel4=np.array([[-1,-1,-1],
                  [-1,8,-1],
                  [-1,-1,-1]])
edges=cv2.filter2D(image,-1,kernel4)
# cv2.imwrite("_04_img/edges.jpg",edges)
cv2.imshow('edges', edges)
print('边缘检测完成')

#高斯双边滤波
# bilateral = cv2.bilateralFilter(src=image, d=0, sigmaColor=100, sigmaSpace=15)
# # bilateral = cv2.resize(bilateral, (image.shape[1], image.shape[0]))
# # cv2.namedWindow('bi_demo', 0)
# cv2.imshow("bilateral", image)
# print('高斯双边滤波完成')

#浮雕滤波器
kernel5=np.array([[-2,-2,-2,-2,0],
                  [-2,-2,-2,0,2],
                  [-2,-2,0,2,2],
                  [-2,0,2,2,2],
                  [0,2,2,2,2]])
emboss=cv2.filter2D(image,-1,kernel5)
emboss=cv2.cvtColor(emboss,cv2.COLOR_BGR2GRAY)
# cv2.imwrite("_04_img/emboss.jpg",emboss)
cv2.imshow('emboss',emboss)
print('浮雕滤波器完成')

cv2.waitKey(0)
cv2.destroyAllWindows()
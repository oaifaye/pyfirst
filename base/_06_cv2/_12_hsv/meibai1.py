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

original_image1 = cv2.imread(r'C:\Users\Administrator\Desktop\zawu\20210202\img\single.jpg').astype(np.float32)/255

# 设置调整颜色参数，小于1时，数值越小，越具有美白效果。反之，大于1时数值越大，可对美白照片还原原色
gamma1 = 0.6
whitening = np.power(original_image1, gamma1)

# 去除噪点
denoise = cv2.medianBlur(whitening, 5)

cv2.imshow('original_image', original_image1)
cv2.imshow('whitening', whitening)
cv2.imshow('denoise', denoise)

# 将美白图片还原为原色
gamma2 = 1.8
debeautify = np.power(denoise, gamma2)
cv2.imshow('debeautify', debeautify)

cv2.waitKey(0)
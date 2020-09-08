

# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:11:21 2018

https://blog.csdn.net/weixin_41010198/article/details/85229435
https://blog.csdn.net/Dawn__Z/article/details/82468018
"""
# """
# 图像基础调整: 图像的亮度、对比度、色度，还可以用于增强图像的锐度,美白
# """

from PIL import Image
from PIL import ImageEnhance
import cv2
import numpy as np


# image = Image.open('14.jpg')
#image.show()
def BrightnessEnhancement(brightness):
    # '''
    # #亮度增强 :brightness在（0-1）之间，新图像较原图暗，在（1-~）新图像较原图亮 ,
    # ##brightness=1,保持原图像不变;可自定义参数范围
    # '''
    image = Image.open(filepath)
    enh_bri = ImageEnhance.Brightness(image)
#    brightness =1.5
    image_brightened = enh_bri.enhance(brightness)
    image_brightened.show()

def ContrastEnhancement(contrast):
    # '''
    # #对比度增强: 可自定义参数contrast范围,contrast=1,保持原图像不变
    # '''
    image = Image.open(filepath)
    enh_con = ImageEnhance.Contrast(image)
#    contrast =1.5
    image_contrasted = enh_con.enhance(contrast)
    image_contrasted.show()

def ColorEnhancement(color):
    # '''
    # #色度增强 : 饱和度  color=1,保持原图像不变
    # '''
    image = Image.open(filepath)
    enh_col = ImageEnhance.Color(image)
#    color =0.8
    image_colored = enh_col.enhance(color)
    image_colored.show()

def SharpnessEnhancement(sharpness):
    # '''
    # #锐度增强: 清晰度  sharpness=1,保持原图像不变
    # '''
    image = Image.open(filepath)
    enh_sha = ImageEnhance.Sharpness(image)
#    sharpness = 2
    image_sharped = enh_sha.enhance(sharpness)
    image_sharped.show()

def Filter(image):
    # """
    # 色彩窗的半径
    # 图像将呈现类似于磨皮的效果
    # """
    #image：输入图像，可以是Mat类型，
    #       图像必须是8位或浮点型单通道、三通道的图像
    #0：表示在过滤过程中每个像素邻域的直径范围，一般为0
    #后面两个数字：空间高斯函数标准差，灰度值相似性标准差
    image =cv2.imread(filepath)
    Remove=cv2.bilateralFilter(image,0,0,10)
    cv2.imshow('filter',Remove)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#    res = np.uint8(np.clip((1.2 * image + 10), 0, 255))
#    tmp = np.hstack((dst, res))
#    cv2.imshow('bai',res)


def WhiteBeauty(image,whi):
    # '''
    # 美白
    # '''
    import cv2

    image =cv2.imread(filepath)
    white = np.uint8(np.clip((whi * image + 10), 0, 255))
    cv2.imshow('bai',white)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#    cv2.imwrite('/home/260207/桌面/photo/15-1.jpg',dst)


if __name__ =="__main__":
    filepath = 'data/nv1.jpg'
    #原始图像
    brightness = 1.5
    contrast = 0.2
    color=1.9
    sharpness=0.1
    BrightnessEnhancement(brightness)
    ContrastEnhancement(contrast)
    ColorEnhancement(color)
    SharpnessEnhancement(sharpness)
    whi = 1.2
    image =cv2.imread('data/nv1.jpg')
    Filter(image)
    WhiteBeauty(image,whi)
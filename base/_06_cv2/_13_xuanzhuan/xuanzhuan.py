# coding=utf-8
#================================================================
#
#   File name   : _13_xuanzhuan.py
#   Author      : Faye
#   Created date: 2021/2/18 14:16 
#   Description : 图片旋转
#
#================================================================
import cv2
import random

def get_image_rotation(image, rotation, scale):
    #通用写法，即使传入的是三通道图片依然不会出错
    height, width = image.shape[:2]
    center = (width // 2, height // 2)
    # rotation = random.randint(-20,20)

    #得到旋转矩阵，第一个参数为旋转中心，第二个参数为旋转角度，第三个参数为旋转之前原图像缩放比例
    M = cv2.getRotationMatrix2D(center, -rotation, scale)
    #进行仿射变换，第一个参数图像，第二个参数是旋转矩阵，第三个参数是变换之后的图像大小
    image_rotation = cv2.warpAffine(image, M, (width, height))
    return image_rotation

if __name__ == '__main__':
    img = cv2.imread(r'F:\pythonCode\_01_demos\pyfirst\base\_06_cv2\_13_xuanzhuan\1.jpg')
    img1 = get_image_rotation(img, 30, 0.9)
    cv2.imshow('0', img)
    cv2.imshow('1', img1)
    cv2.waitKey(1000000)
# coding=utf-8
#================================================================
#
#   File name   : all_similarity.py
#   Author      : Faye
#   Created date: 2021/7/16 9:10 
#   Description :
#
#================================================================

import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity
import cv2
import os
import hashlib
import math

'''
    粗暴的md5比较 返回是否完全相同
'''
def md5_similarity(img1_path, img2_path):
    file1 = open(img1_path, "rb")
    file2 = open(img2_path, "rb")
    md = hashlib.md5()
    md.update(file1.read())
    res1 = md.hexdigest()
    md = hashlib.md5()
    md.update(file2.read())
    res2 = md.hexdigest()
    return res1 == res2

def normalize(data):
    return data / np.sum(data)

'''
    直方图相似度
'''
def hist_similarity(img1, img2, hist_size=256):
    imghistb1 = cv2.calcHist([img1], [0], None, [hist_size], [0, 256])
    imghistg1 = cv2.calcHist([img1], [1], None, [hist_size], [0, 256])
    imghistr1 = cv2.calcHist([img1], [2], None, [hist_size], [0, 256])

    imghistb2 = cv2.calcHist([img2], [0], None, [hist_size], [0, 256])
    imghistg2 = cv2.calcHist([img2], [1], None, [hist_size], [0, 256])
    imghistr2 = cv2.calcHist([img2], [2], None, [hist_size], [0, 256])

    distanceb = cv2.compareHist(normalize(imghistb1), normalize(imghistb2), cv2.HISTCMP_CORREL)
    distanceg = cv2.compareHist(normalize(imghistg1), normalize(imghistg2), cv2.HISTCMP_CORREL)
    distancer = cv2.compareHist(normalize(imghistr1), normalize(imghistr2), cv2.HISTCMP_CORREL)
    meandistance = np.mean([distanceb, distanceg, distancer])
    return meandistance

def PSNR(img1, img2):
    mse = np.mean((img1/255. - img2/255.) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 1
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

def SSIM(img1, img2):
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    # 计算两个灰度图像之间的结构相似度
    score, diff = structural_similarity(gray1, gray2, win_size=101, full=True)
    # diff = (diff * 255).astype("uint8")
    # print("SSIM:{}".format(score))
    return score, diff

if __name__ == '__main__':
    img1_path = 'dui/1.png'
    img2_path = 'dui/2.png'
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    # 1.粗暴的md5比较 返回是否完全相同
    print('md5_similarity:', md5_similarity(img1_path, img2_path))
    # 2.直方图相似度
    print('hist_similarity:', hist_similarity(img1, img2))
    # 3.PSNR
    print('PSNR:', PSNR(img1, img2))
    # 4.SSIM
    print('SSIM:', SSIM(img1, img2))
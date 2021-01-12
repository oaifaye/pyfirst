# coding=utf-8
#================================================================
#
#   File name   : _09_quality.py
#   Author      : Faye
#   Created date: 2021/1/12 11:09 
#   Description : 降低图片质量
#
#================================================================

import cv2

img = cv2.imread(r'quality.jpg', cv2.IMREAD_UNCHANGED)

def quality(q):
    result, encimg = cv2.imencode('.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), q])
    z10 = cv2.imdecode(encimg, 1)
    cv2.imwrite(r'C:\Users\Administrator\Desktop\zawu\20210105\z'+str(q)+'.jpg', z10, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

    # 直接保存的
    # cv2.imwrite(r'C:\Users\Administrator\Desktop\zawu\20210105\z10.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 10])


if __name__ == '__main__':
    for i in range(5, 101, 5):
        quality(i)
# coding=utf-8
#================================================================
#
#   File name   : _08_face_detector.py
#   Author      : Faye
#   Created date: 2020/8/13 17:14 
#   Description :
#
#================================================================


import cv2

nba = cv2.imread('1.jpg')

# 人脸数据，级联分类器，给人脸特征数据，返回可以识别人脸的对象
detector = cv2.CascadeClassifier(r'E:\soft-setup\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
# g = cv2.cvtColor(nba, cv2.COLOR_BGR2GRAY)
face_zone = detector.detectMultiScale(nba, minSize=(100, 100))

for x, y, w, h in face_zone:
    cv2.rectangle(nba, pt1=(x, y), pt2=(x + w, y + h), color=[0, 0, 255])

cv2.imshow('nba', nba)
cv2.waitKey(0)

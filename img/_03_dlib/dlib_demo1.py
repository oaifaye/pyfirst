# coding=utf-8
#================================================================
#
#   File name   : dlib_demo1.py
#   Author      : Faye
#   Created date: 2020/12/30 13:17 
#   Description :
#
#================================================================

import dlib
from PIL import Image, ImageDraw
import numpy as np

# 人脸识别 最普通的方式
def face_detector():
    face_detector = dlib.get_frontal_face_detector()
    img = Image.open('t.jpg')
    dets = face_detector(np.asarray(img), 1)
    draw = ImageDraw.ImageDraw(img)
    for idx, det in enumerate(dets):
        x_min = det.left()
        y_min = det.top()
        x_max = det.right()
        y_max = det.bottom()
        # 起点x, 起点y,
        draw.rectangle((x_min, y_min, x_max, y_max), outline=(255,0,0), width=2)
    img.save("t1.jpg")

# 人脸识别 cnn
def face_detector_cnn():
    cnn_face_detector = dlib.cnn_face_detection_model_v1('mmod_human_face_detector.dat')
    img = Image.open('t.jpg')
    dets = cnn_face_detector(np.asarray(img), 1)
    draw = ImageDraw.ImageDraw(img)
    for idx, det in enumerate(dets):
        x_min = det.rect.left()
        y_min = det.rect.top()
        x_max = det.rect.right()
        y_max = det.rect.bottom()
        conf = det.confidence
        print('conf:', conf)
        if conf > 1.0:
            # 起点x, 起点y,
            draw.rectangle((x_min, y_min, x_max, y_max), outline=(255, 0, 0), width=2)
    img.save("t_cnn.jpg")

if __name__ == '__main__':
    # face_detector()
    face_detector_cnn()
# coding=utf-8
#================================================================
#
#   File name   : photo_restoration.py
#   Author      : Faye
#   Created date: 2021/5/20 16:17 
#   Description :
#
#================================================================


import cv2

import paddlehub as hub

model = hub.Module(name='photo_restoration', visualization=True)
im = cv2.imread('hs.jpg')
res = model.run_image(im, model_select=['Colorization', 'SuperResolution'], save_path='photo_restoration')
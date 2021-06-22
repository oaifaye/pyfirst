# coding=utf-8
#================================================================
#
#   File name   : water.py
#   Author      : Faye
#   Created date: 2021/5/24 15:57 
#   Description :
#
#================================================================

from blind_watermark import WaterMark
import time

bwm1 = WaterMark(password_wm=1, password_img=1)
# 读取原图
bwm1.read_img('jj.jpg')
# 读取水印
bwm1.read_wm('w.png')
# 打上盲水印
t = time.time()
bwm1.embed('jj1.png')
print('打水印:', time.time() - t)

bwm1 = WaterMark(password_wm=1, password_img=1)
# 注意需要设定水印的长宽wm_shape
t = time.time()
bwm1.extract(filename='jj.jpg', wm_shape=(128, 128), out_wm_name='jj2.png', )
print('解水印:', time.time() - t)
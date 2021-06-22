# coding=utf-8
#================================================================
#
#   File name   : douyin1.py
#   Author      : Faye
#   Created date: 2021/2/1 11:26 
#   Description :
#
#================================================================


from PIL import Image
import numpy as np

img_orig = Image.open('douyun.jpg')
# 将图片转化成三维数组
img_orig = img_orig.convert("RGB")
array_orig = np.array(img_orig)

# 将图片转化成四维数组
img_orig = img_orig.convert("RGBA")
array_orig = np.array(img_orig)


# 复制原图的三维数组，将G和B通道的值设为0，只剩下R通道的值非0，这样操作后就生成了只包含R通道的图片
array_r = np.copy(array_orig)
array_r[:, :, 1:3] = 0
image_r = Image.fromarray(array_r)
image_r.show()


# 同样的，生成GB通道的图片，只需要把R通道的值设为0，如下
array_gb = np.copy(array_orig)
array_gb[:, :, 0] = 0
image_gb = Image.fromarray(array_gb)
image_gb.show()

# 接下来，生成一张黑色背景的画布，把R通道的图片贴在画布上，这里粘贴的位置设成 (5, 5) 是为了与GB通道的图片错开位置
canvas_r = Image.new("RGB", img_orig.size, color=(0, 0, 0))
canvas_r.paste(image_r, (-5, -5), image_r)
canvas_r.show()

# 对于GB通道的图片也是类似，贴在另一张画布上，粘贴的位置设成 (0, 0)，与上面R通道的图片错开一定位置
canvas_gb = Image.new("RGB", img_orig.size, color=(0, 0, 0))
canvas_gb.paste(image_gb, (0, 0), image_gb)
canvas_gb.show()

# 将两张画布的三维数组相加，合成效果并显示
result_array = np.array(canvas_r) + np.array(canvas_gb)
result = Image.fromarray(result_array)
result.show()



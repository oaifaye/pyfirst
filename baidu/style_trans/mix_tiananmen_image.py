# coding=utf-8
#================================================================
#
#   File name   : mix_style_image.py
#   Author      : Faye
#   Created date: 2021/3/31 13:14 
#   Description : 天安门图片和成
#
#================================================================
import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont
import os

def mix(img, gb, left_top_pt):
    # 黑背景变透明
    tmp = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, alpha = cv2.threshold(tmp, 10, 255, cv2.THRESH_BINARY)
    b, g, r = cv2.split(img)
    rgba = [b, g, r, alpha]
    img = cv2.merge(rgba, 4)

    # 打开背景
    img1 = Image.fromarray(gb.astype('uint8')).convert('RGB')
    # 创建底图
    target = Image.new('RGBA', (img1.size[0], img1.size[1]), (0, 0, 0, 0))
    # 打开水印
    img2 = Image.fromarray(img.astype('uint8'))
    # 分离透明通道
    r, g, b, a = img2.split()
    # 将背景贴到底图
    img1.convert("RGBA")
    target.paste(img1, (0, 0))
    # 将水印贴到底图
    img2.convert("RGBA")
    target.paste(img2, (left_top_pt[0], left_top_pt[1]), mask=a)

    img1 = np.array(target)
    img2 = np.array(img2)

    return img1

    # img = cv2.warpPerspective(img, 0, (992, 728), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT,
    #                           borderValue=[0, 0, 0, 0])
    # gb[left_top_pt[1]: left_top_pt[1] + h, left_top_pt[0]: left_top_pt[0] + w, :] = img

def mix_task(img_path, bg_path, target_path):
    if not os.path.exists(target_path):
        os.makedirs(target_path)

    for i, img_name in enumerate(os.listdir(img_path)):
        for j, bg_name in enumerate(os.listdir(bg_path)):
            img = cv2.imread(os.path.join(img_path, img_name))
            bg = cv2.imread(os.path.join(bg_path, bg_name))
            mix_img = mix(img, bg, (10, 10))
            cv2.imwrite(os.path.join(target_path, str(i)+"_"+str(j)+".png"), mix_img)

if __name__ == '__main__':
    mix_task(r'F:\datasets\tiananmen\img', r'F:\datasets\tiananmen\bg', r'F:\datasets\tiananmen\res')
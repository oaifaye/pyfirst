# coding=utf-8
#================================================================
#
#   File name   : pyexiv2_demo.py
#   Author      : Faye
#   Created date: 2020/8/10 10:13 
#   Description : 修改、读取图片元数据
#
#================================================================

from pyexiv2 import Image

def read_exif():
    i = Image("imgs/2.jpg")
    print(i.read_exif())
    print(i.read_iptc())
    print(i.read_xmp())

def edit_exif():
    i = Image("imgs/1.jpg")
    _dict = {"Exif.Image.Copyright": "津云"}
    i.modify_exif(_dict)

# edit_exif()
read_exif()
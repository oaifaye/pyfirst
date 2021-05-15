# coding=utf-8
#================================================================
#
#   File name   : matting.py
#   Author      : Faye
#   Created date: 2021/4/1 15:55 
#   Description :
#
#================================================================


# encoding:utf-8

import requests
import base64

'''
人像分割
'''

img_path = r'C:\Users\Administrator\Desktop\zawu\baidu\4.jpg'
target_path = r'C:\Users\Administrator\Desktop\zawu\baidu\res\4.png'


# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=HTWtCYB3A4eWjvGs1Vr1SGbH&client_secret=yzqmjrn3Z67GKlBL2hIXM8GuFmQ5PGft'
response = requests.get(host)
if response:
    print(response.json())
json_res = response.json()
access_token = json_res['access_token']

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_seg"
# 二进制方式打开图片文件
f = open(img_path, 'rb')
img = base64.b64encode(f.read())

params = {"image": img}
# access_token = '[调用鉴权接口获取的token]'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    res = response.json()
    print(res)
    base64_data = res['foreground'].replace("data:audio/x-mpeg;base64,", "")
    res_image_data = base64.b64decode(base64_data)
    text = open(target_path, "wb")
    text.write(res_image_data)
    text.close()
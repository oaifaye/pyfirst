import cv2
import pytesseract
from PIL import Image
import cv2

# encoding:utf-8  https://cloud.baidu.com/doc/OCR/s/1k3h7y3db
import requests
import base64
import json
import cv2

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=mmMNGYRgyMvR8TivC42ga6P9&client_secret=g68UStSDD2yBhURfQDrRwT6HGbGR76rK'
response = requests.get(host)
if response:
    print(response.json())

access_token = response.json()['access_token']

'''
通用文字识别（高精度版）
'''

request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate"
# 二进制方式打开图片文件
pic_img = cv2.imread('1.jpg')
retval, buffer = cv2.imencode('.jpg', pic_img)
pic_str = base64.b64encode(buffer)
img = pic_str.decode()
# f = open('22.png', 'rb')
# img = base64.b64encode(f.read())

params = {"image":img}
# access_token = '24.8964ae587d919822e178083952130c75.2592000.1607429829.282335-22947752'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())
    words = response.json()['words_result']
    word = words[0]
    print(word)

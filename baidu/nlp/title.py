# coding=utf-8
#================================================================
#
#   File name   : title.py
#   Author      : Faye
#   Created date: 2021/4/13 17:00 
#   Description : 百度 新闻自动生成标题
#
#================================================================

# encoding:utf-8

import requests
import json

# client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=SD1yWPfl9pMEhviIUplhkFlG&client_secret=LorD2j4w70qZKzt9HGUPybkyaGYua8CS'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=IkYGEETEaWVWYODwRmDm0ZYE&client_secret=d1mhokFTSMSduZWnqkb3xz0TVmkgXkNQ'
response = requests.get(host)
if response:
    print(response.json())
json_res = response.json()
access_token = json_res['access_token']

request_url = "https://aip.baidubce.com/rpc/2.0/nlp/v1/titlepredictor"

with open(r'1.txt', 'r', encoding='utf-8') as f:
    txt = f.read()
params = {"doc": txt}
# access_token = '[调用鉴权接口获取的token]'
request_url=request_url+"?access_token={token}&&charset=UTF-8".format(token=access_token)
print(params)
headers = {'Content-Type': 'application/json'
           }
params = json.dumps(params, ensure_ascii=False).encode('utf-8')
response = requests.post(request_url, data=params, headers=headers)
if response:
    res = response.json()
    print(res)
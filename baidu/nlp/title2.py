# coding=utf-8
#================================================================
#
#   File name   : title2.py
#   Author      : Faye
#   Created date: 2021/4/15 9:36 
#   Description :
#
#================================================================


# -*- coding: utf-8 -*-
#
import requests
import json

# 你自己的ak,一定要修
ak = "IkYGEETEaWVWYODwRmDm0ZYE"
# 你自己的ak
sk = "d1mhokFTSMSduZWnqkb3xz0TVmkgXkNQ"


def get_accessToken():
    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={ak}&client_secret={sk}".format(
        ak=ak, sk=sk)
    response = requests.get(url)
    return response.json()['access_token']


token = get_accessToken()

# 改成接口文档里的url
nameurl = "https://aip.baidubce.com/rpc/2.0/nlp/v1/titlepredictor"
url = nameurl + "?access_token={token}&charset=UTF-8".format(token=token)
# 构造请求数据格式
with open(r'1.txt', 'r', encoding='utf-8') as f:
    txt = f.read()
data = {"doc": txt}
data = json.dumps(data, ensure_ascii=False).encode('utf-8')
res = requests.post(url=url, data=data, headers={'Content-Type': 'application/json'})
print(res.content)

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
import time

ak="Iz7W8tE9rZaP1LZtAjpxEZu5"
sk="FC5xTrz0jv488NQyHNMntG0dO3ih2PoD"
def get_accessToken():
    url="https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={ak}&client_secret={sk}".format(ak=ak,sk=sk)
    response = requests.get(url)
    return response.json()['access_token']
token=get_accessToken()
nameurl="https://aip.baidubce.com/rest/2.0/solution/v1/img_censor/v2/user_defined"
def check_one(img_url):
    url = nameurl+"?access_token={token}&imgType=0&imgUrl={img_url}".format(token=token, img_url=img_url)
    # with open(r'1.txt', 'r', encoding='utf-8') as f:
    #     txt = f.read()
    data = {}
    # data['doc'] = txt
    # data = json.dumps(data, ensure_ascii=True)
    res = requests.post(url=url, data=data, headers={'Content-Type': 'application/json'})
    return res.content.decode()
    # print(json.dumps(res.content, ensure_ascii=False))

if __name__ == '__main__':
    txt_path = '001_01.txt'
    res_path = '001_01_res.txt'
    content = ''
    start = 800
    t = time.time()
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if i < start:
                continue
            line = line.replace('\n', '')
            res = check_one(line)
            content += line + '\t' + res + '\n'
            if i % 20 == 0:
                with open(res_path, 'a', encoding='utf-8') as resf:
                    resf.write(content)
                    content = ''
                    print('i:', time.time() - t,  i, line, res)

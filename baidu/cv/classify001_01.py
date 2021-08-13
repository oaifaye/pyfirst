# coding=utf-8
#================================================================
#
#   File name   : classify.py
#   Author      : Faye
#   Created date: 2021/5/15 13:02 
#   Description : https://ai.baidu.com/ai-doc/IMAGERECOGNITION/Kkbg3gxs7
#
#================================================================


# -*- coding: utf-8 -*-
#
import requests
import json
import time
import json

ak="ZCfB4Hsr2YVELPVDSUiYL1PG"
sk="GrFcEfLPGbTGCThZtxg9mTviLQCR4dvG"
def get_accessToken():
    url="https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={ak}&client_secret={sk}".format(ak=ak,sk=sk)
    response = requests.get(url)
    return response.json()['access_token']
token=get_accessToken()
nameurl="https://aip.baidubce.com/api/v1/solution/direct/imagerecognition/combination"
def check_one(img_url):

    data = "{\"imgUrl\":\""+img_url+"\",\"scenes\":[\"advanced_general\",\"animal\",\"logo_search\",\"currency\",\"landmark\"]}"
    # print(data)
    url = nameurl+"?access_token={token}".format(token=token)
    # print('url:', url)
    res = requests.post(url=url, data=data, headers={'Content-Type': 'application/json'})
    return res.content.decode()
    # print(json.dumps(res.content, ensure_ascii=False))

def check_img_txt():
    txt_path = 'obj_001_01.txt'
    res_path = 'obj_001_01_res.txt'
    content = ''
    start = 0
    t = time.time()
    with open(txt_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if i < start:
                continue
            line = line.replace('\n', '')
            res = check_one(line)
            content += line + '\t' + res + '\n'
            with open(res_path, 'a', encoding='utf-8') as resf:
                resf.write(content)
                content = ''
            if i % 20 == 0:
                print('i:', time.time() - t, i, line, res)

def fenxi_json():
    json_path = 'obj_001_01_res.txt'
    res_dict = {'logo': {}, 'general': {}, 'animal': {}, 'currency': {}, 'landmark': {}}
    with open(json_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            try:
                line = line.replace('\n', '')
                line_arr = line.split('\t')
                url = line_arr[0]
                result = line_arr[1]
                result = json.loads(result)
                result = result['result']
                # logo
                logo_search = result['logo_search']['result']
                for logo in logo_search:
                    if logo['probability'] < 0.5:
                        continue
                    name = logo['name']
                    if name not in res_dict['logo']:
                        res_dict['logo'][name] = []
                    res_dict['logo'][name].append(url)
                # advanced_general
                advanced_general = result['advanced_general']['result']
                for general in advanced_general:
                    if general['score'] < 0.5:
                        continue
                    root = general['root']
                    keyword = general['keyword']
                    name = root + '-' + keyword
                    if name not in res_dict['general']:
                        res_dict['general'][name] = []
                    res_dict['general'][name].append(url)
                # animal
                animals = result['animal']['result']
                for animal in animals:
                    name = animal['name']
                    if name == '非动物':
                        continue
                    if float(animal['score']) < 0.5:
                        continue
                    if name not in res_dict['animals']:
                        res_dict['animals'][name] = []
                    res_dict['animals'][name].append(url)
                # currency
            except Exception as e:
                print('error:', i, line)

        logo_txt_content = ''
        for logo_name, urls in res_dict['logo'].items():
            print(logo_name, len(urls))
            logo_txt_content += logo_name + '\t' + str(len(urls)) + '\t' + ','.join(urls) + '\n'
        with open('logo.txt', 'w+', encoding='utf-8') as f:
            f.write(logo_txt_content)

        general_txt_content = ''
        for general_name, urls in res_dict['general'].items():
            general_txt_content += general_name + '\t' + str(len(urls)) + '\t' + ','.join(urls) + '\n'
            print(general_name, len(urls))
        with open('general.txt', 'w+', encoding='utf-8') as f:
            f.write(general_txt_content)

        animal_txt_content = ''
        for animal_name, urls in res_dict['animal'].items():
            animal_txt_content += animal_name + '\t' + str(len(urls)) + '\t' + ','.join(urls) + '\n'
            print(animal_name, len(urls))
        with open('animal.txt', 'w+', encoding='utf-8') as f:
            f.write(animal_txt_content)


if __name__ == '__main__':
    # fenxi_json()




    res = check_one('https://img.alicdn.com/imgextra/i4/i2/T1CnA.FixaXXXXXXXX_!!0-item_pic.jpg')
    print('res:', res)

    # encoding:utf-8

    # import requests
    #
    # '''
    # 图像识别组合API
    # '''
    #
    # request_url = "https://aip.baidubce.com/api/v1/solution/direct/imagerecognition/combination"
    #
    # params = "{\"imgUrl\":\"http://pic.app2020.tjyun.com/005/014/252/00501425212_d6180e24.jpg\",\"scenes\":[\"advanced_general\",\"plant\",\"animal\",\"logo_search\"]}"
    # # params = {"imgUrl":"http://pic.app2020.tjyun.com/005/014/252/00501425273_eda6e5cd.png",
    # #           "scenes":["currency"]}
    # access_token = '24.97becf55b3c5e79a8ca96540598938fc.2592000.1623649717.282335-24126407'
    # request_url = request_url + "?access_token=" + access_token
    # headers = {'content-type': 'application/json'}
    # response = requests.post(request_url, data=params, headers=headers)
    # if response:
    #     print(response.json())
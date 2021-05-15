# coding=utf-8
#================================================================
#
#   File name   : analysis.py
#   Author      : Faye
#   Created date: 2021/5/1 21:59 
#   Description :
#
#================================================================

import json

def deal_txt(txt_paths):
    jj = 0
    for txt_path in txt_paths:
        with open(txt_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                line = line.replace('\n', '')
                url = line.split('\t')[0]
                j = line.split('\t')[1]
                j = json.loads(j)
                jj += 1
                if 'conclusion' in j and j['conclusion'] == '不合规':
                    data = j['data']
                    for d in data:
                        d_type = str(d['type'])
                        d_subType = str(d['subType'])
                        if d_type not in check_dict:
                            num_dict[d_type] = {'num': 0}
                            check_dict[d_type] = {}
                        num_dict[d_type]['num'] += 1
                        if d_type == '5':
                            if d_subType not in check_dict[d_type]:
                                check_dict[d_type][d_subType] = {}
                                num_dict[d_type][d_subType] = {'num': 0}
                            d_stars = d['stars']
                            for d_star in d_stars:
                                d_name = d_star['name']
                                if d_name not in check_dict[d_type][d_subType]:
                                    check_dict[d_type][d_subType][d_name] = []
                                    num_dict[d_type][d_subType][d_name] = 0
                                check_dict[d_type][d_subType][d_name].append({'url': url, 'probability': d_probability})
                                num_dict[d_type][d_subType][d_name] += 1
                                num_dict[d_type][d_subType]['num'] += 1
                                num_dict[d_type]['num'] += 1
                        else:
                            if d_subType not in check_dict[d_type]:
                                check_dict[d_type][d_subType] = []
                                num_dict[d_type][d_subType] = {'num': 0}
                            d_probability = d['probability']
                            check_dict[d_type][d_subType].append({'url':url, 'probability': d_probability})
                            num_dict[d_type][d_subType]['num'] += 1
                            num_dict[d_type]['num'] += 1

                    print('data:', data)
    print("num_dict['5']['0'].items():", num_dict['5']['0'].items())
    sorted_50 = sorted(num_dict['5']['0'].items(), key=lambda x: x[1], reverse=True)
    sorted_50_dict = {}
    for sorted_50_i in sorted_50:
        sorted_50_dict[sorted_50_i[0]] = sorted_50_i[1]
    sorted_51 = sorted(num_dict['5']['1'].items(), key=lambda x: x[1], reverse=True)
    print('sorted_50:', sorted_50)
    sorted_51_dict = {}
    for sorted_51_i in sorted_51:
        sorted_51_dict[sorted_51_i[0]] = sorted_51_i[1]
    num_dict['5']['0'] = sorted_50_dict
    num_dict['5']['1'] = sorted_51_dict
    print('jj:', jj)
    with open('num_dict.dump', 'w') as f:
        json.dump(num_dict, f)
    with open('check_dict.dump', 'w') as f:
        json.dump(check_dict, f)

if __name__ == '__main__':
    num_dict = {} # 计数用的
    check_dict = {}
    txt_paths = [
        r'C:\Users\Administrator\Desktop\zawu\20210415\001_01_res.txt',
        r'C:\Users\Administrator\Desktop\zawu\20210415\001_02_res.txt',
        r'C:\Users\Administrator\Desktop\zawu\20210415\001_03_res.txt'
    ]
    deal_txt(txt_paths)
    print(num_dict)
    print(check_dict)

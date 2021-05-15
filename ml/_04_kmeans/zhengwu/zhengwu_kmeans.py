# coding=utf-8
#================================================================
#
#   File name   : zhengwu_kmeans.py
#   Author      : Faye
#   Created date: 2021/5/6 7:39 
#   Description :
#
#================================================================

import numpy as np
from sklearn.cluster import KMeans

def onehot():
    with open(r'keywords.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            line = line.replace('\n', '')
            vac = np.zeros((len(lines)))
            vac[i] = 1
            keywords_dict[line] = vac

def make_idcard_vac():
    with open(r'idcard_keywords.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            line = line.replace('\n', '')
            line = line.split('\t')
            idcard = line[0]
            keywords = line[1]
            if keywords == '_':
                continue
            if idcard not in idcard_keywords_dict:
                idcard_keywords_dict[idcard] = np.zeros(len(keywords_dict))
            idcard_keywords_dict[idcard] += keywords_dict[keywords]

def kmeans():
    idcard_list = []
    keywords_list = []
    for idcard, keywords in idcard_keywords_dict.items():
        idcard_list.append(idcard)
        keywords_list.append(keywords)
    y_pred = KMeans(n_clusters=100, random_state=14, max_iter=1000).fit_predict(keywords_list)
    excel = ''
    for idcard, y in zip(idcard_list, y_pred):
        excel += idcard + '\t' + str(y) + '\n'
    print(y_pred)
    with open(r'kmeans_res.cvs', 'w+', encoding='utf-8') as f:
        f.write(excel)

if __name__ == '__main__':
    keywords_dict = {}  # key：中國字 value：獨熱向量
    idcard_keywords_dict = {}  # key：idcard value：這個idcard的向量
    onehot()
    make_idcard_vac()
    # print(idcard_keywords_dict)
    kmeans()
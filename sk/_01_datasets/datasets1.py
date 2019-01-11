from __future__ import print_function
from time import time
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.datasets import fetch_20newsgroups
from sklearn.datasets import load_boston
from sklearn.datasets.base import load_files
from sklearn.datasets.lfw import fetch_lfw_people

n_samples = 2000

print("Loading dataset...")
# t0 = time()
# dataset = fetch_20newsgroups(shuffle=True, random_state=1,
#                              remove=('headers', 'footers', 'quotes'))
# data_samples = dataset.data[:n_samples]
# print(data_samples)
# print("done in %0.3fs." % (time() - t0))

#加载并返回波士顿房价数据集（回归）
def loadboston():
    bos = load_boston()
    print(type(bos))
    for i in bos:
        print(i)
    print(bos.DESCR)

#加载具有子文件夹名称类别的文本文件
def loadfiles():
    files = load_files(container_path='01/')
    print('keys:',str(files.keys()))
    print(files)
    
def lfwpeople():
    lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
    print('keys:',str(lfw_people.keys()))
    print(lfw_people)
    
lfwpeople()

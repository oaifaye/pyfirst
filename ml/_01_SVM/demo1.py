# -*- coding: utf-8 -*-

import numpy as np
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report

'''
1.读取文件并存储
'''
with open("demo1_Iris.txt","r") as file:
    ty=-3 #代表取哪一列label值，-1代表取倒一列所有值
    result=[]
    for line in file.readlines():
        result.append(list(map(str,line.strip().split(','))))

    vec = np.array(result)
    x = vec[:,:-3]#取除掉最后三列以外的所有列，即所有特征列
    y = vec[:,ty]#标签列
    '''
    2.划分测试集及训练集
    '''
    train_x,test_x,train_y,test_y = train_test_split(x,y,test_size=0.2)
    '''
    3.模型训练及预测
    '''
    clf = SVC(kernel='linear',C=0.8)
    clf.fit(train_x,train_y)
    
    pred_y = clf.predict(test_x)
    print(classification_report(test_y,pred_y))
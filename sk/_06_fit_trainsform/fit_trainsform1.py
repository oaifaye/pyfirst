'''
Created on 2018年12月20日
fit transform fit_trainform的区别
https://blog.csdn.net/ljyljyok/article/details/79722089
'''

import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import scale
from sklearn.linear_model.logistic import LogisticRegression
from sklearn.linear_model.base import LinearRegression

#只传一个参数，标准化数据
def guiyihua():
    data=np.array([[1,2,300],[100,3,300],[100,2,300]])
    ss = StandardScaler()
    ss.fit(data)
    print('data:',data)
    print('scale_:',ss.scale_)  #每个属性的缩放比例,即每个属性原来的范围/每个属性归一化之后的范围
    print('mean_:',ss.mean_)  #均值
    print('var_:',ss.var_)  #方差
    print('n_samples_seen_:',ss.n_samples_seen_) #样本数（行数）
    print(ss.transform(data)) #正规标准化数据
    # print(scale(data))
    
#传两个参数，训练数据
def train():
    X = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
    y = np.array([10,20,30])
    X_test = np.array([[10,20,30,40],[40,50,60,70],[70,80,90,100]])
    reg = LinearRegression()
    reg.fit(X, y)
    print('coef_:',reg.coef_)
    print('intercept_:',reg.intercept_)
    print('predict:',reg.predict(X_test))

train()
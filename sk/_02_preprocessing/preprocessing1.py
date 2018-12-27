'''
Created on 2018年12月16日

@author: Administrator
'''
from sklearn.preprocessing import StandardScaler

#标准化数据,将数据转化成均值为0，方差是1的数据
def standardscaler():
    data = [[1],[2],[3],[4],[5],[1000]]
    scaler = StandardScaler(copy=True, with_mean=True, with_std=True)
    scaler.fit(data)
    print(scaler.transform(data))
    print('mean_:',str(scaler.mean_))
    print('标准差scale_:',str(scaler.scale_))
    
standardscaler()
'''
Created on 2019年2月5日

'''
import numpy as np

data = np.arange(10)  
data = data.reshape([1,-1])
data1 = data.repeat([3],axis=0)

print(data1)
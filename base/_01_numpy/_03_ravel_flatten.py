'''
Created on 2018年12月20日

首先声明两者所要实现的功能是一致的（将多维数组降位一维），两者的区别在于返回拷贝（copy）还是返回视图（view），
numpy.flatten()返回一份拷贝，对拷贝所做的修改不会影响（reflects）原始矩阵，
而numpy.ravel()返回的是视图（view，也颇有几分C/C++引用reference的意味），会影响（reflects）原始矩阵。

'''

import numpy as np

x = np.array([[1,2,3],[4,5,6]])
y = np.array([[1,2,3],[4,5,6]])

print('x.flatten():',x.flatten())
x.flatten()[1] = 100
print('x:',x)

print('y.ravel():',y.ravel())
y.ravel()[1] = 100
print('y:',y)


#reshape函数当参数只有一个-1时表示将数组降为一维
print('x.reshape(-1):',x.reshape(-1))

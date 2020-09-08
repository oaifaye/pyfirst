# coding=utf-8
#================================================================
#
#   File name   : _08_reshape.py
#   Author      : Faye
#   Created date: 2020/8/13 14:49 
#   Description : 变换维度和交换维度
#
#================================================================

import numpy as np

a = [1,2,3,4,5,6,7,8,9,10,11,12]
a= np.asarray(a)
b = a.reshape((2, 2, 3))
print('b:', b)

c = b.transpose((0, 2, 1))
print('c:', c)

a = np.zeros((4, 4, 12), dtype=np.int)
n = 0
for i in range(0, 4):
    for j in range(0, 4):
        for k in range(0, 12):
            a[i, j, k] = int(n)+1
            n += 1
print('a:', a)
b = a.reshape((4, 4, 2, 2, 3))
print('b:', b)
c = b.transpose((0, 2, 1, 3, 4))
print('c:', c)
d = c.reshape((8, 8, 3))
print('d:', d)

e = a.reshape((8, 8, 3))
print('e:', e)
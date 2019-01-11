'''
Created on 2019年1月6日

person相关系数矩阵
'''
import numpy as np


a=[[1,2,3,4,5],
   [6,7,8,9,10],
   [7,5,8,4,0]]

# 自己列之间比较；rowvar只在自己比较是有作用：False行之间比较，True列之间比较（默认）
print('自己列之间比较:\n',np.corrcoef(a, rowvar=False))

b = [1,2,3,4,5]
c = [6,7,8,9,10]
d = [7,5,8,4,0]
#两个数组之间比较
print('两个数组之间比较b---c:\n',np.corrcoef(b,c))
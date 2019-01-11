'''
Created on 2019年1月5日

有关相关性分析的混沌
'''
import numpy as np # 导入库
data = np.loadtxt('demo2_Iris.txt', delimiter=' ') # 读取数据文件
x = data[:, :-1] # 切分自变量
correlation_matrix = np.corrcoef(x, rowvar=0) # 相关性分析
print (correlation_matrix.round(2)) # 打印输出相关性结果
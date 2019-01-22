'''
Created on 2018年1月6日

@author: Administrator
'''
import numpy as np
from numpy import int16
data = [(1,11,111,1111,11111,111111),(2,22,222,2222,22222,222222),
        (3,33,333,3333,33333,333333),(4,44,444,4444,44444,444444),
        (5,55,555,5555,55555,555555),(6,66,666,6666,66666,666666),(7,77,777,7777,77777,777777)]
ndata = np.array(data)

'''
ndarray.ndim：数组的维数（即数组轴的个数），等于秩。最常见的为二维数组（矩阵）。
ndarray.shape：数组的维度。为一个表示数组在每个维度上大小的整数元组。例如二维数组中，表示数组的“行数”和“列数”。ndarray.shape返回一个元组，这个元组的长度就是维度的数目，即ndim属性。
ndarray.size：数组元素的总个数，等于shape属性中元组元素的乘积。
ndarray.dtype：表示数组中元素类型的对象，可使用标准的Python类型创建或指定dtype。另外也可使用前一篇文章中介绍的NumPy提供的数据类型。
ndarray.itemsize：数组中每个元素的字节大小。例如，一个元素类型为float64的数组itemsiz属性值为8(float64占用64个bits，每个字节长度为8，所以64/8，占用8个字节），又如，一个元素类型为complex32的数组item属性为4（32/8）。
ndarray.data：包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。
'''
print('维数  ndim',ndata.ndim)
print('维度  shape',ndata.shape)
print('size',ndata.size)
print('dtype',ndata.dtype)
print(ndata[0:2,2:4])

d = np.zeros((3,4))  
print('zeros:',d)

d = np.ones((3,4))  
print('ones:',d)

'''# 手动指定数组中元素类型'''  
d = np.ones( (2,3,4), dtype=int16)  
print('ones-dtype:',d)

d = np.empty((2,3))  
print('empty：',d)

print(ndata[1:3])

print('ndata.T',ndata.T)

'''若我们要生成满足正太分布为N(3，2.5^2)，2行4列的array'''
zheng = 2.5 * np.random.randn(2, 4) + 3
print('zheng',zheng)

x_data = np.linspace(-1, 1, 2000)
print()

print(9%8)


data1 = [(1,11,111),(2,22,222),(3,33,333),(4,44,444),(5,55,555),(6,66,666),(7,77,777)]
ndata1 = np.array(data1)
print('ndata1.shape[0]',ndata1.shape[0])
print('ndata1.shape[1:]',ndata1.shape[1:])
print('ndata1.reshape',ndata1.reshape(ndata1.shape[0],3,1))
print('ndata1(0,0)',ndata1[0,0])

data1 = [[2,3],[4,5]]
print(data1 *2)

#将一个列表a转换成相应的矩阵类型
a = np.mat([[1, 3], [5, 7]])
print('mat:',a)

data2 = np.zeros((4,3))
for i in range(3):
    data2[:,i]=np.random.normal()
print('data2:'+str(data2))

#随机
print('np.random.randn():',np.random.randn(2, 3))

data3 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print('data3.reshape(-1):',data3.reshape(4,-1))

data4=np.array([0,1,2,3,4,5])
date4_1 = np.array([10,20,30,40,50,60])
date4_1[data4]=-1
print('date4_1:',date4_1)

#第一个参数是开始，第二个参数是结束，第三个参数是步长
print('np.arange:',np.arange(1,6.1))

data5=[[1,1,1,1],[1,10,100,100],[1,10,100,1000]]
print('cov:',np.cov(data5))

#堆叠数组（列式）
data6=[[2,2,2,2],[2,20,200,200],[2,20,200,2000]]
print('hstack',np.hstack((data5,data6)))
#堆叠数组（行式）
print('vstack',np.vstack((data5,data6)))
print('stack',np.stack((data5,data6),axis=1))

#np.newaxis 增加一个维度，常用于行向量转列向量
print('data6,np.newaxis:\n',np.array(data6)[:,:,np.newaxis])
data7 = [1,2,3,4,5,6]
print('data7,np.newaxis:\n',np.array(data7)[:,np.newaxis])

data8=[[[1,11],[2,22],[3,33]],[[4,44],[5,55],[6,66]]]
print('data8[-1]:',data8[-1])

#类型转换
data8.astype(np.int32)
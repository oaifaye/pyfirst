'''
Created on 2019年1月10日
numpy中的随机
'''
import numpy as np

'''
1.numpy.random.rand(d0,d1,…,dn)
rand函数根据给定维度生成[0,1)之间的数据，包含0，不包含1
dn表格每个维度
返回值为指定维度的array
'''
print("numpy.random.rand():",np.random.rand(2,3))

'''
2.numpy.random.randn(d0,d1,…,dn)
•randn函数返回一个或一组样本，具有标准正态分布。
•dn表格每个维度
•返回值为指定维度的array
'''
print("numpy.random.randn():",np.random.randn(2,3))

'''
3.numpy.random.randint(low, high=None, size=None, dtype=’l’)
•返回随机整数，范围区间为[low,high），包含low，不包含high
•参数：low为最小值，high为最大值，size为数组维度大小，dtype为数据类型，默认的数据类型是np.int
•high没有填写时，默认生成随机数的范围是[0，low)
numpy.random.random_integers方法不建议使用，用numpy.random.randint代替
'''
print("numpy.random.randint():",np.random.randint(1,100,10,np.int))

'''
4.随机浮点数
'''
print('random_sample:\n', np.random.random_sample((2, 3)))
print('random:\n', np.random.random((2, 3)))
print('ranf:\n', np.random.ranf((2, 3)))
print('sample:\n', np.random.sample((2, 3)))

'''
5.numpy.random.choice(a, size = None, replace=True, p=None)
从给定的一维数组中生成随机数
如a是一个int数， 则产生的数组的元素都在np.arange(a)中
如a是一个1-D array-like， 则产生的数组的元素都在a中
'''
print('numpy.random.choice():\n', np.random.choice((1,2,3,4,5),3))

'''
6.numpy.random.seed(None)
设置相同的seed，每次生成的随机数相同。如果不设置seed，则每次会生成不同的随机数
'''
np.random.seed(2)
print('np.random.seed-rand():',np.random.rand(2, 3))
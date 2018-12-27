'''
Created on 2018年12月20日
enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
Python 2.3. 以上版本可用，2.6 添加 start 参数。
'''


seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print (i, element)
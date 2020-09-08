'''
Created on 2019年4月2日

用函数画一个圆
'''
import matplotlib.pyplot as plt

r = 10  #半径
lamda = 0.001   #步长
x_range_abs = 10 #x范围是正负这个数

x = []
y1 = []
y2 = []
i = -x_range_abs
while i <= x_range_abs:
    y = (r**2 - i**2)**0.5
    x.append(i)
    y1.append(y)
    y2.append(-y)
    i = i + lamda;
plt.figure(num = 0, figsize=(5, 5))
plt.plot(x, y1,'r')
plt.plot(x, y2,'r')
plt.xlabel('X')
plt.ylabel('Y')
# plt.scatter(x, y)
# 必要方法，用于将设置好的figure对象显示出来
plt.show()
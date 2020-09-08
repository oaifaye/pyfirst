import matplotlib.pyplot as plt
import numpy as np

a = np.random.rand(1, 10000)*100000
c = np.random.rand(1, 10000)*100000

z = a*c/((a+c)*(a+c))
# print(z)
print(np.max(z))
# 第一个是横坐标的值，第二个是纵坐标的值
x = [i for i in range(1000)]
x= np.array(x).reshape([1,1000])
plt.plot(a, z)
# 必要方法，用于将设置好的figure对象显示出来
plt.show()


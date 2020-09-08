# coding:utf-8

print (__doc__)
import numpy as np
from matplotlib.collections import LineCollection
from pylab import *

from sklearn.linear_model import LinearRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.utils import check_random_state

x = [1,2,3,4,5,6,7,8,9,10,11,12,13]
y = [1,2,3,4,96,97,98,99,45,46,47,48,49]

#拟合保存回归和线性回归模型
ir = IsotonicRegression()
y_ = ir.fit_transform(x,y)
print(y_)

plt.plot(x,y,"r.",markersize=12)
plt.plot(x,y_,"g.-",markersize=12)

plt.show()
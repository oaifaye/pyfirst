# coding:utf-8

print (__doc__)
import numpy as np
from matplotlib.collections import LineCollection
from pylab import *

from sklearn.linear_model import LinearRegression
from sklearn.isotonic import IsotonicRegression
from sklearn.utils import check_random_state

n = 100
x = np.arange(n)
rs = check_random_state(0)
y = rs.randint(-50,50,size=(n,))+50.*np.log(1+np.arange(n))

#拟合保存回归和线性回归模型
ir = IsotonicRegression()
y_ = ir.fit_transform(x,y)
print(y)
print(y_)
lr = LinearRegression()
lr.fit(x[:,np.newaxis],y) #线性回归中x需要是二维的

#绘制结果

segments = [[[i, y[i]], [i, y_[i]]] for i in range(n)]
lc = LineCollection(segments, zorder=0)
lc.set_array(np.ones(len(y)))
lc.set_linewidths(0.5 * np.ones(n))

plt.plot(x,y,"r.",markersize=12)
plt.plot(x,y_,"g.-",markersize=12)
plt.plot(x,lr.predict(x[:,np.newaxis]),"b-")
plt.gca().add_collection(lc)

myfont = matplotlib.font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")
mpl.rcParams['axes.unicode_minus'] = False
plt.legend((u"数据",u"保序拟合",u"线性拟合"),loc="lower right",prop=myfont)
plt.title(u'保存回归',fontproperties=myfont)

plt.show()
'''
Created on 2018年11月29日

@author: Administrator
'''
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

import numpy as np      #科学计算包
import matplotlib.pyplot as plt  


'''
make_blobs函数是为聚类产生数据集
产生一个数据集和相应的标签
n_samples:表示数据样本点个数,默认值100
n_features:表示数据的维度，默认值是2
centers:产生数据的中心点，默认值3
cluster_std：数据集的标准差，浮点数或者浮点数序列，默认值1.0
center_box：中心确定之后的数据边界，默认值(-10.0, 10.0)
shuffle ：洗乱，默认值是True
random_state:官网解释是随机生成器的种子
更多参数即使请参考：http://scikit-learn.org/dev/modules/generated/sklearn.datasets.make_blobs.html#sklearn.datasets.make_blobs
'''
n_samples = 1500
random_state = 170
X, y = make_blobs(n_samples=n_samples, random_state=random_state,n_features=3)
print(X)


'''
1) n_clusters: 即我们的k值，和KMeans类的n_clusters意义一样。
2）max_iter：最大的迭代次数， 和KMeans类的max_iter意义一样。
3）n_init：用不同的初始化质心运行算法的次数。这里和KMeans类意义稍有不同，KMeans类里的n_init是用同样的训练集数据来跑不同的初始化质心从而运行算法。而MiniBatchKMeans类的n_init则是每次用不一样的采样数据集来跑不同的初始化质心运行算法。
4）batch_size：即用来跑Mini Batch KMeans算法的采样集的大小，默认是100.如果发现数据集的类别较多或者噪音点较多，需要增加这个值以达到较好的聚类效果。
5）init： 即初始值选择的方式，和KMeans类的init意义一样。
6）init_size: 用来做质心初始值候选的样本个数，默认是batch_size的3倍，一般用默认值就可以了。
7）reassignment_ratio: 某个类别质心被重新赋值的最大次数比例，这个和max_iter一样是为了控制算法运行时间的。这个比例是占样本总数的比例，乘以样本总数就得到了每个类别质心可以重新赋值的次数。如果取值较高的话算法收敛时间可能会增加，尤其是那些暂时拥有样本数较少的质心。默认是0.01。如果数据量不是超大的话，比如1w以下，建议使用默认值。如果数据量超过1w，类别又比较多，可能需要适当减少这个比例值。具体要根据训练集来决定。
8）max_no_improvement：即连续多少个Mini Batch没有改善聚类效果的话，就停止算法， 和reassignment_ratio， max_iter一样是为了控制算法运行时间的。默认是10.一般用默认值就足够了。
'''
y_pred = KMeans(n_clusters=3, random_state=random_state,max_iter=1000).fit_predict(X)
print(y_pred)
plt.scatter(X[:, 0], X[:, 2], c=y_pred) #scatter绘制散点
plt.title("Incorrect Number of Blobs") 
plt.show()
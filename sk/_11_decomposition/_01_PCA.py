'''
Created on 2019年1月1日
pca的主要作用是降维
https://www.cnblogs.com/zy230530/p/7074215.html
'''
from sklearn.decomposition import PCA
import numpy as np
from numpy import *
import matplotlib.pyplot as plt

data = np.array([[ 1.  ,  1.  ],
       [ 0.9 ,  0.95],
       [ 1.01,  1.03],
       [ 2.  ,  2.  ],
       [ 2.03,  2.06],
       [ 1.98,  1.89],
       [ 3.  ,  3.  ],
       [ 3.03,  3.05],
       [ 2.89,  3.1 ],
       [ 4.  ,  4.  ],
       [ 4.06,  4.02],
       [ 3.97,  4.01]])

def skpca():
    plt.scatter(data[:,0], data[:,1],vmin=-10,  # 行的跨度
                        vmax=10,)
    
    '''
    1）n_components：这个参数可以帮我们指定希望PCA降维后的特征维度数目。最常用的做法是直接指定降维到的维度数目，此时n_components是一个大于等于1的整数。
                    当然，我们也可以指定主成分的方差和所占的最小比例阈值，让PCA类自己去根据样本特征方差来决定降维到的维度数，此时n_components是一个（0，1]之间的数。
                    当然，我们还可以将参数设置为"mle", 此时PCA类会用MLE算法根据特征的方差分布情况自己去选择一定数量的主成分特征来降维。我们也可以用默认值，即不输入n_components，此时n_components=min(样本数，特征数)。

　　　　2）whiten ：判断是否进行白化。所谓白化，就是对降维后的数据的每个特征进行归一化，让方差都为1.对于PCA降维本身来说，一般不需要白化。
                            如果你PCA降维后有后续的数据处理动作，可以考虑白化。默认值是False，即不进行白化。

　　　　3）svd_solver：即指定奇异值分解SVD的方法，由于特征分解是奇异值分解SVD的一个特例，一般的PCA库都是基于SVD实现的。
                            有4个可以选择的值：{‘auto’, ‘full’, ‘arpack’, ‘randomized’}。randomized一般适用于数据量大，数据维度多同时主成分数目比例又较低的PCA降维，它使用了一些加快SVD的随机算法。
          full则是传统意义上的SVD，使用了scipy库对应的实现。arpack和randomized的适用场景类似，区别是randomized使用的是scikit-learn自己的SVD实现，而arpack直接使用了scipy库的sparse SVD实现。
                          默认是auto，即PCA类会自己去在前面讲到的三种算法里面去权衡，选择一个合适的SVD算法来降维。一般来说，使用默认值就够了。

　　　　除了这些输入参数外，有两个PCA类的成员值得关注。第一个是explained_variance_，它代表降维后的各主成分的方差值。方差值越大，则说明越是重要的主成分。
                第二个是explained_variance_ratio_，它代表降维后的各主成分的方差值占总方差值的比例，这个比例越大，则越是重要的主成分。
    '''
    pca = PCA(n_components=2, copy=True, whiten=False, svd_solver='auto', tol=0.0, iterated_power='auto', random_state=None)
    pcadata = pca.fit_transform(data)
    print(np.dot(pcadata[:,0].T,pcadata[:,1]))
    plt.scatter(pcadata[:,0], np.array([1 for i in range(12)]))
    plt.show()

#pca特征维度压缩函数
#@dataMat 数据集矩阵
#@topNfeat 需要保留的特征维度，即要压缩成的维度数，默认4096    
def pca(dataMat,topNfeat=4096):
    #求数据矩阵每一列的均值
    meanVals=mean(dataMat,axis=0)
    #数据矩阵每一列特征减去该列的特征均值
    meanRemoved=dataMat-meanVals
    #计算协方差矩阵，除数n-1是为了得到协方差的无偏估计
    #cov(X,0) = cov(X) 除数是n-1(n为样本个数)
    #cov(X,1) 除数是n
    covMat=cov(meanRemoved,rowvar=0)
    #计算协方差矩阵的特征值及对应的特征向量
    #均保存在相应的矩阵中
    eigVals,eigVects=linalg.eig(mat(covMat))
    #sort():对特征值矩阵排序(由小到大)
    #argsort():对特征值矩阵进行由小到大排序，返回对应排序后的索引
    eigValInd=argsort(eigVals)
    #从排序后的矩阵最后一个开始自下而上选取最大的N个特征值，返回其对应的索引
    eigValInd=eigValInd[:-(topNfeat+1):-1]
    #将特征值最大的N个特征值对应索引的特征向量提取出来，组成压缩矩阵
    redEigVects=eigVects[:,eigValInd]
    #将去除均值后的数据矩阵*压缩矩阵，转换到新的空间，使维度降低为N
    lowDDataMat=meanRemoved*redEigVects
    #利用降维后的矩阵反构出原数据矩阵(用作测试，可跟未压缩的原矩阵比对)
    reconMat=(lowDDataMat*redEigVects.T)+meanVals
    #返回压缩后的数据矩阵即该矩阵反构出原始数据矩阵
    print('lowDDataMat:',lowDDataMat)
    print('reconMat:',reconMat)
    return lowDDataMat,reconMat

# pca(data)

test()
'''
    谱聚类
    https://blog.csdn.net/songbinxu/article/details/80838865

'''

import sys
sys.path.append("..")

from utils.similarity import calEuclidDistanceMatrix
from utils.knn import myKNN
from utils.laplacian import calLaplacianMatrix
from utils.dataloader import genTwoCircles
from utils.ploter import plot
from sklearn.cluster import KMeans
import numpy as np
np.random.seed(1)

data, label = genTwoCircles(n_samples=200)
print('data:',data.shape)
# 1.欧氏距离的矩阵 对角是0
Similarity = calEuclidDistanceMatrix(data)  # D
print('Similarity:',Similarity.shape)
# 2.权重矩阵 正常情况下对角不是零 其余都是零
Adjacent = myKNN(Similarity, k=5)          # W
print('Adjacent:',Adjacent)
# 3.拉普拉斯矩阵
Laplacian = calLaplacianMatrix(Adjacent)
print('Laplacian:',Laplacian.shape)
# 矩阵分解 特征值
x, V = np.linalg.eig(Laplacian)
print('特征值：',x.shape)
x = zip(x, range(len(x)))
x = sorted(x, key=lambda x:x[0])
print('x:',np.array(x).shape)
H = np.vstack([V[:,i] for (v, i) in x[:100]]).T
print('H:',H.shape)
sp_kmeans = KMeans(n_clusters=2).fit(H)

pure_kmeans = KMeans(n_clusters=2).fit(data)

plot(data, sp_kmeans.labels_, pure_kmeans.labels_)

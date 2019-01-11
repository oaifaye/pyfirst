'''
    顾名思义，linalg=linear+algebralinalg=linear+algebra，线性代数
'''
import numpy as np

#normnorm则表示范数，首先需要注意的是范数是对向量（或者矩阵）的度量，是一个标量
#x表示要度量的向量，ord表示范数的种类(一范数、二范数...、np.inf无穷范数max(|xi|))
x = np.array([[1,1,1],[1,1,1]])
print("默认参数(矩阵2范数，不保留矩阵二维特性)：",str(np.linalg.norm(x,ord=2)))
print("矩阵每个行向量求向量的2范数：",str(np.linalg.norm(x,ord=2,axis=1,keepdims=True)))

#逆矩阵：inv
x = np.array([[1,2,3], [4,5,6],[7,8,9]])
print("逆矩阵：:",str(np.linalg.inv(x)))

#广义逆矩阵：inv
x = np.array([[1,2,3], [4,5,6],[7,8,9]])
print("广义逆矩阵：:",str(np.linalg.pinv(x)))

#解形如AX=b的线性方程组：np.linalg.solve(A,b)
A = np.array([[1,2], [3,4]])
b = np.array([6,7])
print("解线性方程组：:",str(np.linalg.solve(A,b)))

#行列式：det
print("行列式：:",str(np.linalg.det(x)))

#估计线性模型中的系数。返回元组，元组中四个元素，第一元素表示所求的最小二乘解，第二个元素表示残差总和，第三个元素表示X矩阵秩，第四个元素表示X的奇异值
x = np.array([[1, 6, 2,1,3], [1, 8, 1,1,5], [1, 10, 0,1,4], [1, 14, 2,1,3], [1, 18, 0,1,3]])
b= np.array([[7], [9], [13], [17.5], [18]])
print(np.linalg.lstsq(x, b))

#特征向量特征值
def testeig():
    data = [
            [1,1,1],
            [2,2,2],
            [3,3,3]
            ]
    eigVals,eigVects=np.linalg.eig(np.mat(data))
    print('eigVals:',eigVals)
    print('eigVects:',eigVects)

testeig()

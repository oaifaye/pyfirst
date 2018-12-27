'''
Created on 2018年12月15日

@author: Administrator
'''

from sklearn.linear_model import LarsCV
from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model.ridge import Ridge
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

#普通最小二乘法的线性回归
def linearregression():
#     LinearRegression(copy_X=False, fit_intercept=True, n_jobs=1, normalize=True)
    reg = LinearRegression()
    X = [[0, 0], [1, 1], [2, 2]]
    reg.fit (X, [0, 1, 2])
    print(reg.coef_)
    print(X)

#岭回归
def ridge():
    reg = Ridge (alpha = .5)
    reg.fit ([[0, 0], [0, 0], [1, 1]], [0, .1, 1])
    Ridge(alpha=0.5, copy_X=True, fit_intercept=True, max_iter=None,
          normalize=False, random_state=None, solver='auto', tol=0.001)
    print('coef_:',reg.coef_)
    print('intercept_:',reg.intercept_)

def larscv():
    X, y = make_regression(n_samples=200,n_features=10, noise=4.0, random_state=0)
    reg = LarsCV(cv=2).fit(X, y)
    print(reg.score(X, y) )
    print(X[:,0].shape,y.shape)
    plt.plot(X[:,0], y)
    plt.scatter(X[:,0], y)
    plt.show()

linearregression()


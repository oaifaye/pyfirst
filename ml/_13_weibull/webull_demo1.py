# coding=utf-8
#================================================================
#
#   File name   : webull_demo1.py
#   Author      : Faye
#   Created date: 2020/9/1 10:24 
#   Description : 韦伯分布  weibull distribution
#               https://www.cnblogs.com/mrcharles/p/11879765.html
#
#================================================================



import scipy.stats as s
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import exponweib
from scipy.stats import beta
from scipy.stats import norm
from scipy.stats import weibull_min


def make_weib_file():
    np.set_printoptions(suppress=False)
    n = 5
    a = 1
    content = ''
    for i in range(1, 500):
        x = i / 100
        print(x)
        content += str(np.round(x, 4)) + " " + str(np.round(weib(x, n, a), 4)) + '\n'
    with open("stack_data.csv", 'w+') as f:
        f.write(content)

# def weib(x,n,a):
#     return (a / n) * (x / n)**(a - 1) * np.exp(-(x / n)**a)

def weib(x, a, c) :
    return a * c * (1-np.exp(-x**c))**(a-1) * np.exp(-x**c)*x**(c-1)

def fit_weib():
    data = np.loadtxt("stack_data.csv")

    # shape, loc, scale = weibull_min.fit(data, loc=2, scale=1)
    a, c, loc, scale = s.exponweib.fit(data, loc=0, scale=1)
    print(a, c, loc, scale)

    x = np.linspace(0.001, 5, 500)
    y = s.exponweib.pdf(x, a=a, c=c, scale=1, loc=0)
    plt.plot(data[:, 0], data[:, 1])
    plt.plot(x, y, 'r--')
    print('data.max():', data.max())
    # plt.hist(data, int(data.max()), normed=True)
    plt.show()

'''
    真正的demo方法
'''
def fit_weib2():
    # 生成韦伯分布数据
    sample = exponweib.rvs(a=10, c=1, scale=3, loc=0, size=1000)

    x = np.linspace(0, np.max(sample), 100)
    #拟合
    a, c, loc, scale = exponweib.fit(sample, floc=0, fa=1)
    print(a, c, loc, scale)
    y = exponweib.pdf(x, a, c, loc, scale)
    for x1, y1 in zip(x, y):
        print(x1, y1)
    plt.plot(x, y)
    plt.show()

# make_weib_file1()
fit_weib2()
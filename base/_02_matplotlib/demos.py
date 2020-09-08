#utf-8
# https://blog.csdn.net/Notzuonotdied/article/details/77876080
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def line():
    # 从[-1,1]中等距去50个数作为x的取值
    x = np.linspace(-1, 1, 50)
    y = 2*x+5
    # 第一个是横坐标的值，第二个是纵坐标的值
    plt.plot(x, y)
    # 必要方法，用于将设置好的figure对象显示出来
    plt.show()

#显示多个图像
def duogetu():
    # 多个figure
    x = np.linspace(-1, 1, 50)
    y1 = 2*x + 1
    y2 = 2**x + 1
    
    # 使用figure()函数重新申请一个figure对象
    # 注意，每次调用figure的时候都会重新申请一个figure对象
    plt.figure(num = 2, figsize=(8, 5))
    # 第一个是横坐标的值，第二个是纵坐标的值
    plt.plot(x, y1)
    
    # 第一个参数表示的是编号，第二个表示的是图表的长宽
    plt.figure(num = 3, figsize=(8, 5))
    # 当我们需要在画板中绘制两条线的时候，可以使用下面的方法：
    plt.plot(x, y2)
    plt.plot(x, y1, 
             color='red',   # 线颜色
             linewidth=1.0,  # 线宽 
             linestyle='--',  # 线样式
             label='bbb' #标签
            )
    plt.show()
    
    
#散点图
def sandian():
    x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    y = [43,9,11,17,11,44,1041,1659,2034,2285,1976,2422,2332,2324,2124,1861,1993,2144,2419,1190,2970,1244,787,349]
    y1 = [7,7,8,7,3,14,321,14,22,23,1,998,23,114,1,1,2,4,142,2,6,5,7,6,]
    x = np.array(x)
    y = np.array(y)
    y1 = np.array(y1)
    # 第一个是横坐标的值，第二个是纵坐标的值
    #线
    plt.plot(x, y)
    plt.plot(x, y1)
    #散点
    plt.scatter(x, y)
    plt.show()
    
# Subplot多合一显示
def subplotMuch():
    plt.figure()
    # 将整个figure分成两行两列
    plt.subplot(2,2,1)
    # 第一个参数表示X的范围，第二个是y的范围
    plt.plot([0, 1], [0, 1])
    
    plt.subplot(2,2,2)
    plt.plot([0, 1], [0, 2])
    
    plt.subplot(2,2,3)
    plt.plot([0, 1], [0, 3])
    
    plt.subplot(2,2,4)
    plt.plot([0, 1], [0, 4])
    
    plt.show()
    
#3D数据图
def threedd():
    fig = plt.figure(figsize=(12, 8))
    ax = Axes3D(fig)
    
    # 生成X，Y
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    #从一个坐标向量中返回一个坐标矩阵
    X,Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    
    # height value
    Z = np.sin(R)
    
    # 绘图
    # rstride（row）和cstride(column)表示的是行列的跨度
    ax.plot_surface(X, Y, Z, 
                    rstride=1,  # 行的跨度
                    cstride=1,  # 列的跨度
                    cmap=plt.get_cmap('rainbow')  # 颜色映射样式设置
                   )
    
    # offset 表示距离zdir的轴距离
    ax.contourf(X, Y, Z, zdir='z', offest=-2, cmap='rainbow')
    ax.set_zlim(-2, 2)
    
    plt.show()
    
#二次函数
def erci():
    # 从[-1,1]中等距去50个数作为x的取值
    x = np.linspace(-100, 100, 50)
    y = x**3-2*x+5
    # 第一个是横坐标的值，第二个是纵坐标的值
    plt.plot(x, y)
    plt.scatter(x, y)
    plt.show()
    
subplotMuch()
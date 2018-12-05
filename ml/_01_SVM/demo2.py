# -*- coding: utf-8 -*-

import numpy as np
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report

def iris_type(s):
    it = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
    return it[str(s, encoding = "utf8")]  

path = 'demo1_Iris.txt'  # 
data = np.loadtxt(path, dtype=float, delimiter=',', converters={4: iris_type})

x, y = np.split(data, (4,), axis=1)
x = x[:, :4]#所有行，每行0到4列的数（不包括4列）
print(x)
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, train_size=0.6)
print(x.shape)
'''
参数：
C：C-SVC的惩罚参数C，也就是优化函数中松弛变量的系数，默认值是1.0。 C越大，相当于惩罚松弛力度越强，（由于惩罚项是加在后面的而且求的是函数最小值），
    对训练集分类要求更严格，这样对训练集测试时准确率很高，但泛化能力弱。C值小，对误分类的惩罚减小，允许容错，将他们当成噪声点，泛化能力较强。
kernel： 
核函数，默认是rbf，可以是‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’ 

linear – 线性：u'v
poly – 多项式：(gamma*u'*v + coef0)^degree
rbf – RBF函数：exp(-gamma|u-v|^2)
sigmoid –sigmoid：tanh(gamma*u'*v + coef0)
precomputed-自定义

degree ：多项式poly函数的维度，默认是3，选择其他核函数时会被忽略。
gamma：‘rbf’,‘poly’ 和‘sigmoid’的核函数参数。默认是’auto’，则会选择1/n_features
coef0 ：核函数的常数项。对于‘poly’和 ‘sigmoid’有用。
max_iter ：最大迭代次数。-1为无限制。
decision_function_shape ：‘ovo’, ‘ovr’ or None, default=None3
'''
clf = SVC(C=0.8, kernel='linear',degree=8, gamma=20, decision_function_shape='ovo')
clf.fit(x_train, y_train.ravel())

y_pred = clf.predict(x_test)
print(classification_report(y_test,y_pred))
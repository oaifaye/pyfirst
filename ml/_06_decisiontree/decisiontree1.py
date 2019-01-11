'''
Created on 2019年1月4日

决策树
'''
import numpy as np
from sklearn.model_selection._split import train_test_split
from sklearn.metrics.classification import classification_report
from sklearn.tree.tree import DecisionTreeClassifier


def iris_type(s):
    it = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
    return it[str(s, encoding = "utf8")]  

path = 'demo1_Iris.txt'  # 
data = np.loadtxt(path, dtype=float, delimiter=',', converters={4: iris_type})

x, y = np.split(data, (4,), axis=1)
x = x[:, :4]
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, train_size=0.6)
clf = DecisionTreeClassifier(criterion='entropy',random_state=0)
clf.fit(x, y.ravel())

print('feature_importances_',clf.feature_importances_)

y_pred = clf.predict(x_test)
print(classification_report(y_test,y_pred))
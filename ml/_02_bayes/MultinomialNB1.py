#utf-8
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report

def iris_type(s):
    it = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
    return it[str(s, encoding = "utf8")]  

path = 'demo1_Iris.txt'  # 
data = np.loadtxt(path, dtype=float, delimiter=',', converters={4: iris_type})

x, y = np.split(data, (4,), axis=1)
x = x[:, :4]
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1, train_size=0.6)
clf = MultinomialNB()
clf.fit(x_train, y_train.ravel())

y_pred = clf.predict(x_test)
print(classification_report(y_test,y_pred))


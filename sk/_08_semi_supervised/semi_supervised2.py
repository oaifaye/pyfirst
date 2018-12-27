'''
Created on 2018年12月26日

半监督学习的简单实践
'''
import numpy as np
from sklearn import datasets
from sklearn.semi_supervised import label_propagation
from sklearn.metrics.classification import confusion_matrix,\
    classification_report
# 再加下面这个，不然会报错
from scipy.sparse.csgraph import *

train_num=100       #训练验本总数
train_labeled=30    # 总训练样本中有多少已标记数据
test_num=100        #测试样本数

digits = datasets.load_digits()
data = digits.data[:train_num]
target = digits.target[:train_num]

X=data
y_train = np.copy(target)
#从31开始，把后面的target都变成-1
y_train[train_labeled:]=-1
#     print('y_train:',y_train)
lp_model = label_propagation.LabelSpreading(gamma=0.25,max_iter=5) # 训练模型
lp_model.fit(X,y_train)

predicted_labels = lp_model.transduction_[train_labeled:] # 预测的标签
#     print('predicted_labels:',predicted_labels)
true_labels = target[train_labeled:] # 真实的标签
#     print('true_labels:',true_labels)

# cm = confusion_matrix(true_labels,predicted_labels,labels = lp_model.classes_)
print('train report:\n',classification_report(true_labels,predicted_labels))

test_X = digits.data[train_num:(train_num+test_num)]
test_y = digits.target[train_num:(train_num+test_num)]
print('test_y:',test_y)
predict_y = lp_model.predict(test_X)
print('predict_y:',predict_y)
print('test report:\n',classification_report(test_y,predict_y))

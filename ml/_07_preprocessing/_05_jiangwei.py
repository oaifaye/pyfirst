'''
数据降维
'''

import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.decomposition import PCA

def iris_type(s):
    it = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
    return it[str(s, encoding = "utf8")]  

# 读取数据文件
data = np.loadtxt('demo1_Iris.txt',delimiter=',', converters={4: iris_type}) # 读取文本数据文件
x = data[:, :-1] # 获得输入的x
y = data[:, -1] # 获得目标变量y
print (x[0], y[0]) # 打印输出x和y的第一条记录
# 使用sklearn的DecisionTreeClassifier判断变量重要性
model_tree = DecisionTreeClassifier(random_state=0) # 建立分类决策树模型对象
model_tree.fit(x, y) # 将数据集的维度和目标变量输入模型
feature_importance = model_tree.feature_importances_ # 获得所有变量的重要性得分
print ('feature_importance:\n',feature_importance) # 打印输出
# 使用sklearn的PCA进行维度转换
model_pca = PCA() # 建立PCA模型对象
model_pca.fit(x) # 将数据集输入模型
model_pca.transform(x) # 对数据集进行转换映射
components = model_pca.components_ # 获得转换后的所有主成分
components_var = model_pca.explained_variance_ # 获得各主成分的方差
components_var_ratio = model_pca.explained_variance_ratio_ # 获得各主成分的方差占比
print ('前2个主成分：',components[:2]) # 打印输出前2个主成分
print ('前2个主成分的方差：',components_var[:2]) # 打印输出前2个主成分的方差
print ('所有主成分的方差占比：',components_var_ratio) # 打印输出所有主成分的方差占比
'''
Created on 2019年1月5日

离散化，对运营数据做逻辑分层
'''

import pandas as pd
from sklearn.cluster import KMeans
from sklearn import preprocessing
import numpy as np

# 读取数据
df = pd.read_table('demo3.txt', names=['id', 'amount', 'income', 'datetime', 'age'],delimiter=' ') # 读取数据文件
print (df.head(5)) # 打印输出前5条数据
# 针对时间数据的离散化
for i, signle_data in enumerate(df['datetime']): # 循环得到索引和对应值
    single_data_tmp = pd.to_datetime(signle_data) # 将时间转换为datetime格式
    df['datetime'][i] = single_data_tmp.weekday() # 离散化为周几
print (df.head(5)) # 打印输出前5条数据
# 针对多值离散数据的离散化
map_df = pd.DataFrame([['0-10', '0-40'], ['10-20', '0-40'], ['20-30', '0-40'], ['30-40', '0-40'], ['40-50', '40-80'], ['50-60', '40-80'], ['60-70', '40-80'], ['70-80', '40-80'], ['80-90', '>80'], ['>90', '>80']],
columns=['age', 'age2']) # 定义一个要转换的新区间
df_tmp = df.merge(map_df, left_on='age', right_on='age', how='inner') # 数据框关联匹配
df = df_tmp.drop('age', 1) # 丢弃名为age的列
print (df.head(5)) # 打印输出前5条数据
# 针对连续数据的离散化
# 方法1：自定义分箱区间实现离散化
bins = [0, 200, 1000, 5000, 10000] # 自定义区间边界
df['amount1'] = pd.cut(df['amount'], bins) # 使用边界做离散化
print (df.head(5)) # 打印输出前5条数据
# 方法2 使用聚类法实现离散化
data = np.array(df['amount']) # 获取要聚类的数据，名为amount的列
data_reshape = data.reshape((data.shape[0], 1)) # 转换数据形状
model_kmeans = KMeans(n_clusters=4, random_state=0) # 创建KMeans模型并指定要聚类的数量
keames_result = model_kmeans.fit_predict(data_reshape) # 建模聚类
df['amount2'] = keames_result # 新离散化的数据合并到原数据框
print (df.head(5)) # 打印输出前5条数据
# 方法3：使用4分位数实现离散化
df['amount3'] = pd.qcut(df['amount'], 4, labels=
['bad', 'medium', 'good', 'awesome']) # 按4分位数进行分隔
df = df.drop('amount', 1) # 丢弃名为amount的列
print (df.head(5)) # 打印输出前5条数据
# 针对连续数据的二值化
binarizer_scaler = preprocessing.Binarizer(threshold=df['income'].mean()) # 建立Binarizer模型对象
print('df[\'income\']:',np.array(df['income']).reshape(-1,1))
income_tmp = binarizer_scaler.fit_transform(np.array(df['income']).reshape(-1,1)) # Binarizer标准化转换
income_tmp.resize(df['income'].shape) # 转换数据形状
df['income'] = income_tmp # Binarizer标准化转换
print (df.head(5)) # 打印输出前5条数据
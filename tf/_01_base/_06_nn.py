'''
Created on 2018年11月19日
用10层隐层的神经网络解决线性或曲线回归
'''

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 特征数
featurenum = 1
#数据条数
datano = 100

train_X = np.linspace(-1, 1, datano)[:,np.newaxis]
print(train_X.shape)
#线性y
# train_Y = (3 * train_X  + 2)+np.random.ranf(datano).T.reshape(datano,1)
#曲线y
train_Y = np.square(train_X) + np.random.normal(0,0.1,train_X.shape)
print(train_Y.shape)

#x---100:1
x = tf.placeholder(tf.float32,[None,featurenum])
y = tf.placeholder(tf.float32,[None,featurenum])

#全连接，之后 100:10
w1 = tf.Variable(tf.random_normal([featurenum, 10])) #十层隐层
b1 = tf.Variable(tf.zeros([1, featurenum]))
y1 = tf.matmul(x, w1)+b1
prediction1 = tf.nn.relu(y1)#预测结果  

#输出层 10:1
wout = tf.Variable(tf.random_normal([10,featurenum]))
bout = tf.Variable(tf.zeros([1,1]))
yout = tf.matmul(prediction1,wout)+bout

# loss = tf.reduce_mean(tf.square(y - yout))
loss = tf.losses.mean_squared_error(y, yout)

train_op = tf.train.GradientDescentOptimizer(0.01).minimize(loss) 

with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    for i in range(100000):
        _ ,lossout,prediction1_out= sess.run([train_op,loss,yout],feed_dict={x:train_X,y:train_Y})
        if i % 10000 == 0:
            print(lossout)
    plt.scatter(train_X,train_Y)
    plt.plot(train_X,prediction1_out)
    plt.show()
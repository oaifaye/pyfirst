'''
Created on 2018年11月19日
简单的优化器例子,线性回归
'''

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

train_X = np.linspace(-1, 1, 100)
train_Y = (3 * train_X  + 2)

y = tf.placeholder("float")
x = tf.placeholder("float")
w = tf.Variable(0.0)
b = tf.Variable(0.0)

loss = tf.square(y - (w * x + b))

train_op = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    for i in range(10):
        _,res_w,res_b = sess.run([train_op,w,b],feed_dict={x:train_X,y:train_Y})
#         for t_x ,t_y in zip(train_X,train_Y):
#             _,res_w,res_b = sess.run([train_op,w,b],feed_dict={x:t_x,y:t_y})
        print(res_w,res_b)
    plt.plot(train_X,train_X*(res_w)+res_b)
    plt.show()
'''
Created on 2018年11月19日
简单的逻辑回归
'''

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

num_samples=400

def train(train_X,train_Y):
    y = tf.placeholder("float")
    x = tf.placeholder("float")
    w = tf.Variable(0.0)
    b = tf.Variable(0.0)
    y_predict=tf.sigmoid(w * x + b)
    loss=tf.reduce_sum(tf.pow(y_predict-y,2.0))/num_samples
    
    train_op = tf.train.AdamOptimizer(0.01).minimize(loss)
    
    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())
        for i in range(10000):
            _,res_loss,res_w,res_b = sess.run([train_op,loss,w,b],feed_dict={x:train_X,y:train_Y})
            print(res_loss)
    return res_w,res_b

def prediction(test_X,w,b):
    y_predict=tf.sigmoid(w * test_X + b)
    
    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())
        y = sess.run(y_predict)
        plt.plot(test_X,y)
        plt.show()

train_X = np.linspace(-1, 1, num_samples)
train_Y = np.sin(train_X)+np.random.normal(0,0.01,num_samples)
res_w,res_b = train(train_X, train_Y)
prediction(train_X, res_w, res_b)

plt.plot(train_X,train_Y)
# plt.show()
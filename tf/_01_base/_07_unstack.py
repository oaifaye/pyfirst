'''
Created on 2019年1月17日

矩阵拼接、分解
'''

import tensorflow as tf

a = tf.constant([1,2,3])
b = tf.constant([4,5,6])
c = tf.stack([a,b],axis=0)
d = tf.stack([a,b],axis=1)
with tf.Session() as sess:
    print('c:',sess.run(c))
    print('d:',sess.run(d))
    
e=[[1,2,3],[4,5,6]]
f = tf.unstack(e, axis=1)
with tf.Session() as sess:
    print('f:',sess.run(f))
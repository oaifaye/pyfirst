'''
Created on 2018年11月19日
1.先用assign给a赋值，然后运算loss
2.再次用assign给a赋值
3.执行sess.run(loss)，sess.run(net['x'])是第二次赋值之前的值；net['x']是第二次赋值之后的值
'''
import tensorflow as tf

net = {}
net['a'] = tf.Variable([[0.0,0.0]])
net['x'] = tf.add(net['a'], [[1.0,1.0]])

with tf.Session() as sess:
    init_op = tf.initialize_all_variables()
    sess.run(init_op)
    #1.先用assign给a赋值，然后运算
    sess.run([net['a'].assign([[5.0,5.0]])])
    #sess.run(net['x'])是第二次赋值之前的值
    x1 = sess.run(net['x'])
    #net['x']是第二次赋值之后的值
    x2 = net['x']
    loss = tf.reduce_sum(tf.pow((x1 - x2), 2))
    #2.再次用assign给a赋值
    sess.run([net['a'].assign([[10.0,10.0]])])
    #3.执行sess.run(loss)，sess.run(net['x'])是第二次赋值之前的值；net['x']是第二次赋值之后的值
    print(sess.run(loss))
    

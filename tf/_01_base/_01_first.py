#coding:utf-8
'''
    第一个tf
'''
import tensorflow as tf

x = tf.Variable([[2,3]])
y = tf.Variable([[4],[5]])

z = tf.multiply(x, y)

#e的幂
ex = tf.exp(tf.constant([5.,6.,10.]))

#除法
div = tf.div([48.0,403,22026],22477)

#幂函数
pow = tf.pow(x, 2)

add = tf.add(x, y)

reduce_sum = tf.reduce_sum(x)

loss = -tf.log(0.97993505)

print(help(tf.contrib.losses.absolute_difference ))

init_op = tf.initialize_all_variables()
with tf.Session() as sess:
    sess.run(init_op)
    print(z.eval())
    print(sess.run((z,ex)))
    print(sess.run(ex))
    print('div:',sess.run(div))
    print('loss:',sess.run(loss))
    print('pow:',sess.run(pow))
    print('add:',sess.run(add))
    print('reduce_sum:',sess.run(reduce_sum))

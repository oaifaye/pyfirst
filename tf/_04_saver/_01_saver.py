'''
Created on 2019年1月21日

'''
import tensorflow as tf
x = tf.Variable([[2,3]])
y = tf.Variable([[4],[5]])

init_op = tf.initialize_all_variables()
with tf.Session() as sess:
    sess.run(init_op)
    #在创建这个Saver对象的时候，有一个参数我们经常会用到，就是 max_to_keep 参数，这个是用来设置保存模型的个数，默认为5，即 max_to_keep=5，保存最近的5个模型。
    saver=tf.train.Saver(max_to_keep=1)
    #第一个参数sess。第二个参数设定保存的路径和名字，第三个参数将训练的次数作为后缀加入到模型名字中。
    saver.save(sess,'ckpt/mnist.ckpt',global_step=111)

    #模型的恢复用的是restore()函数，它需要两个参数restore(sess, save_path)，save_path指的是保存的模型路径。
    #我们可以使用tf.train.latest_checkpoint()来自动获取最后一次保存的模型。如：
    model_file=tf.train.latest_checkpoint('ckpt/')
    saver.restore(sess,model_file)

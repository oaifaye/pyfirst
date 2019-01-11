import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#input就是输入数据，输入矩阵，in_size就是输入矩阵的列数（数据属性数量），out_size输出矩阵列数
#activation_function就是激活函数
def add_layer(input,in_size,out_size,activation_function):
    Weight=tf.Variable(tf.random_normal([in_size,out_size]))
    biases=tf.Variable(tf.zeros([1,out_size]))+0.1
    Wx_plus_b=tf.matmul(input,Weight)+biases
    if activation_function is None:
        outputs=Wx_plus_b
    else:
        outputs=activation_function(Wx_plus_b)
    return outputs

#####create data#####
#x_data 300x1,np.newaxis 增加维度
x_data=np.linspace(-1,1,300)[:,np.newaxis]
#noise是均值为0，方差为0.05的高斯随机数
noise=np.random.normal(0,0.05,x_data.shape)
#noise就是数据中的干扰成分，噪点，数据是非线性变化的
y_data=np.square(x_data)-0.5+noise
print(x_data.shape)
print(y_data.shape)

# data = np.linspace(-1, 1, 300)
# x_data = data
# # print(train_X)
# y_data = (3 * data  + 2)+np.random.ranf(300)*0.1

xs=tf.placeholder(tf.float32,[None,1])
ys=tf.placeholder(tf.float32,[None,1])

#隐藏层有十个神经元
l1=add_layer(xs,1,10,activation_function=tf.nn.relu)
predition=add_layer(l1,10,1,activation_function=None)
#计算代价函数，reduction_indices是指在哪一维度上进行求解
loss=tf.reduce_mean(tf.reduce_sum(tf.square(ys-predition),
                                  reduction_indices=[1]))
#使用梯度下降的方法使loss达到最小
train_step=tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init=tf.global_variables_initializer()
sess=tf.Session()
sess.run(init)

for _ in range(100):
    _,losout,preditionout = sess.run((train_step,loss,predition),feed_dict={xs:x_data,ys:y_data})
#     if _%50==0:
#         print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))

plt.scatter(x_data,y_data)
plt.plot(x_data,preditionout)
plt.show()
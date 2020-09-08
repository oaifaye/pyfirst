# coding=utf-8
#================================================================
#
#   File name   : backpropagation.py
#   Author      : Faye
#   Created date: 2020/7/31 10:50 
#   Description : numpy实现反向传播  主要看这个文件
#
#================================================================
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_derivationx(y):
    return y * (1 - y)

def back():
    input = np.array([0.9, 0.1], dtype='float')
    weight_1 = np.array([[0.15, 0.20], [0.25, 0.30]], dtype='float')
    weight_2 = np.array([[0.40, 0.45], [0.50, 0.55]], dtype='float')
    target_output = np.array([0.11, 0.89], dtype='float')
    learning_rate = 0.5
    steps = 1000
    while steps > 0:
        steps -= 1
        # 正向传播
        # layer-1
        net_h1, net_h2 = np.dot(input, weight_1)  # 第一层的计算结果
        out_h1, out_h2 = [1 / (1 + np.exp(-net_h1)), 1 / (1 + np.exp(-net_h2))]  # sigmoid激活后的输出
        # layer-2
        layer_2_input = np.array([out_h1, out_h2], dtype='float')
        net_o1, net_o2 = np.dot(layer_2_input, weight_2)  # 第二层的计算结果
        out_o1, out_o2 = [1 / (1 + np.exp(-net_o1)), 1 / (1 + np.exp(-net_o2))]  # sigmoid激活后的输出
        # 计算梯度,反向传播
        total_loss = sum([pow(target_output-real_output, 2)/2 for target_output, real_output in zip(target_output, [out_o1, out_o2])])
        print('网络的输出：step:%d loss=%f out_o1=%f out_o2=%f ' % (steps, total_loss, out_o1, out_o2))
        # gradient for layer-2
        gradient_w5 = -1 * (target_output[0] - out_o1) * out_o1 * (1 - out_o1) * out_h1
        gradient_w6 = -1 * (target_output[0] - out_o1) * out_o1 * (1 - out_o1) * out_h2
        gradient_w7 = -1 * (target_output[1] - out_o2) * out_o2 * (1 - out_o2) * out_h1
        gradient_w8 = -1 * (target_output[1] - out_o2) * out_o2 * (1 - out_o2) * out_h2

        # gradient for layer-1
        gradient_w1 = -1 * (target_output[0] - out_o1) * out_o1 * (1 - out_o1) * weight_2[0][0] * out_h1 * \
                      (1 - out_h1)*input[0] - (target_output[1] - out_o2) * out_o2 * (1 - out_o2) * weight_2[1][0] * \
                      out_h1 * (1 - out_h1)*input[0]

        gradient_w2 = -1 * (target_output[0] - out_o1) * out_o1 * (1 - out_o1) * weight_2[0][0] * out_h1 * \
                      (1 - out_h1) * input[1] - (target_output[1] - out_o2) * out_o2 * (1 - out_o2) * weight_2[1][0] * \
                      out_h1 * (1 - out_h1)*input[1]

        gradient_w3 = -1 * (target_output[0] - out_o1) * out_o1 * (1 - out_o1) * weight_2[0][1] * out_h2 * \
                      (1 - out_h2) * input[0] - (target_output[1] - out_o2) * out_o2 * (1 - out_o2) * weight_2[1][1] * \
                      out_h2 * (1 - out_h2)*input[0]

        gradient_w4 = -1 * (target_output[0] - out_o1) * out_o1 * (1 - out_o1) * weight_2[0][1] * out_h2 * \
                      (1 - out_h2) * input[1] - (target_output[1] - out_o2) * out_o2 * (1 - out_o2) * weight_2[1][1] * \
                      out_h2 * (1 - out_h2)*input[1]

        # update weight
        # layer -1
        weight_1[0][0] = weight_1[0][0] - learning_rate * gradient_w1
        weight_1[1][0] = weight_1[1][0] - learning_rate * gradient_w2
        weight_1[0][1] = weight_1[0][1] - learning_rate * gradient_w3
        weight_1[1][1] = weight_1[1][1] - learning_rate * gradient_w4

        # layer-2
        weight_2[0][0] = weight_2[0][0] - learning_rate * gradient_w5
        weight_2[1][0] = weight_2[1][0] - learning_rate * gradient_w6
        weight_2[0][1] = weight_2[0][1] - learning_rate * gradient_w7
        weight_2[1][1] = weight_2[1][1] - learning_rate * gradient_w8
        # print('weight_1:', weight_1)
        # print('weight_2:', weight_2)
        if steps == 1:
            print('网络的输出：loss=%f out_o1=%f out_o2=%f ' % (total_loss, out_o1, out_o2))
            break

def back_matrix():
    input = np.array([0.9, 0.1], dtype='float')
    weight_1 = np.array([[0.5, 0.5],
                         [0.5, 0.5]], dtype='float')
    weight_2 = np.array([[0.5, 0.5],
                         [0.5, 0.5]], dtype='float')
    target_output = np.array([0.11, 0.89], dtype='float')
    learning_rate = 0.5
    steps = 1000
    while steps > 0:
        steps -= 1
        # 正向传播
        # layer-1
        net_h = np.dot(input, weight_1)  # 第一层的计算结果
        out_h = sigmoid(net_h)  # sigmoid激活后的输出
        # layer-2
        layer_2_input = np.array(out_h, dtype='float')
        net_o = np.dot(layer_2_input, weight_2)  # 第二层的计算结果
        out_o = sigmoid(net_o)  # sigmoid激活后的输出
        # 计算梯度,反向传播
        total_loss = sum([pow(target_output-real_output, 2)/2 for target_output, real_output in zip(target_output, out_o)])
        print('网络的输出：step:%d loss=%f out_o1=%f out_o2=%f ' % (steps, total_loss, out_o[0], out_o[0]))

        gradient_weight_2 = np.zeros_like(weight_2)
        for i in range(gradient_weight_2.shape[1]):
            gradient_weight_2[:, i] = (out_o[i] - target_output[i]) * sigmoid_derivationx(out_o[i]) * out_h

        gradient_weight_1 = np.zeros_like(weight_1)
        for i in range(gradient_weight_1.shape[1]):
            dot1 = -1 * (target_output - out_o) * out_o * sigmoid_derivationx(out_h)
            dot2 = np.reshape(weight_2[:, i], (-1, 1))
            gradient_weight_1[:, i] = np.dot([dot1], dot2) * input

        # update weight
        # layer -1
        weight_1 = weight_1 - learning_rate * gradient_weight_1

        # layer-2
        weight_2 = weight_2 - learning_rate * gradient_weight_2
        if steps == 1:
            print('网络的输出：loss=%f out_o1=%f out_o2=%f ' % (total_loss, out_o[0], out_o[1]))
            break

# back()
back_matrix()
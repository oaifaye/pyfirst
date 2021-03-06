# coding:utf-8
'''
    卷积的计算
'''

import tensorflow as tf
import cv2
import numpy as np

def demo1():
    input = [[
              [[1,1,1],[1,1,1],[1,1,1],[1,2,3],[1,2,3],[1,2,3]],
              [[2,2,2],[2,2,2],[2,2,2],[1,2,3],[1,2,3],[1,2,3]],
              [[3,3,3],[3,3,3],[3,3,3],[1,2,3],[1,2,3],[1,2,3]],
              [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]],
              [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]],
              [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]],
              [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]],
              [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]],
              [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]],
              ],
             [
              [[1,1,1],[1,1,1],[1,1,1],[1,2,3],[1,2,3],[1,2,3]],
              [[2,2,2],[2,2,2],[2,2,2],[1,2,3],[1,2,3],[1,2,3]],
              [[3,3,3],[3,3,3],[3,3,3],[1,2,3],[1,2,3],[1,2,3]],
              [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]],
              [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]],
              [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]],
              [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]],
              [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]],
              [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]],
              ]
             ]
    input = tf.Variable(input,dtype='float32')
    print('input:',input.shape)
    filter = [
              [[[1,2,3],[1,2,3],[1,2,3]],
               [[1,2,3],[1,2,3],[1,2,3]],
               [[1,2,3],[1,2,3],[1,2,3]]],
    #           [[[1,2],[1,2],[1,2]],
    #            [[1,2],[1,2],[1,2]],
    #            [[1,2],[1,2],[1,2]]],
    #           [[[1,2],[1,2],[1,2]],
    #            [[1,2],[1,2],[1,2]],
    #            [[1,2],[1,2],[1,2]]],
              ]
    
    filter = tf.Variable(filter,dtype='float32')
    print('filter:',filter.shape)
    
    con = tf.nn.conv2d(input, filter,[1,1,1,1],'SAME')
    
    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())
        print(sess.run(con))
        print(sess.run(con).shape)
        
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.05)
    return tf.Variable(initial)

def demo2():
    img_size = 30

    img = cv2.imread('_05.jpg')
    print(type(img))
    img = cv2.resize(img,(img_size,img_size))
#     print(img)
    cv2.imshow('i',img)
    
    print(img.shape)
    img = img.reshape([1,img_size,img_size,3])
    print(img.shape)
    img = tf.Variable(img,dtype='float32')
    #图片输入 [图片张数,高,宽,通道数]
    #图片的卷积，filter[核高,核宽,通道数,featureMap的个数]
    #卷积结果 [图片张数,高,宽,featureMap的个数]
    filter = [
              [
               [[0.01,0.02,0.03,0.03],[0.01,0.02,0.03,0.03],[0.01,0.02,0.03,0.03]],
               [[0.01,0.02,0.03,0.03],[0.01,0.02,0.03,0.03],[0.01,0.02,0.03,0.03]],
               [[0.01,0.02,0.03,0.03],[0.01,0.02,0.03,0.03],[0.01,0.02,0.03,0.03]],
               ],
              [
               [[0.01,0.02,0.03,0.03],[0.01,0.02,0.03,0.03],[0.01,0.02,0.03,0.03]],
               [[0.01,0.02,0.03,0.03],[0.01,0.02,0.03,0.03],[0.01,0.02,0.03,0.03]],
               [[0.01,0.02,0.03,0.03],[0.01,0.02,0.03,0.03],[0.01,0.02,0.03,0.03]],
               ],
              [
               [[0.01,0.02,0.03,0.03],[0.01,0.02,0.03,0.03],[0.01,0.02,0.03,0.03]],
               [[0.01,0.02,0.03,0.03],[0.01,0.02,0.03,0.03],[0.01,0.02,0.03,0.03]],
               [[0.01,0.02,0.03,0.03],[0.01,0.02,0.03,0.03],[0.01,0.02,0.03,0.03]],
               ],
              ]
    # filter = [
    #           [[[1],[1],[1]],
    #            [[1],[1],[1]],
    #            [[1],[1],[1]]],
    #           ]
    print('filter:',np.array(filter).shape)
    con = tf.nn.conv2d(img, filter, [1,1,1,1],'SAME')
    con = tf.nn.relu(con)
    
    print('con.shape[3]:',con.shape[3])
    #第二次卷积，filter的通道数和上一次卷积的结果通道数得一样;做卷积时，每个channel算完会相加
    filter2= weight_variable([5,5,int(con.shape[3]),10])
    con = tf.nn.conv2d(con, filter2, [1,1,1,1],'SAME')
    con = tf.nn.relu(con)
    print('con shape:',con.shape)
    
    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())
        con1 = sess.run(con)
        print('np.array(con).shape[3]:',np.array(con1).shape[3])
        #结果的图片数量
        picNum = np.array(con1).shape[3]
        for i in range(picNum):
            coni = con1[:,:,:,i]
            coni = coni.reshape([img_size, img_size, 1])
            coni = coni.repeat(3,axis=2)
            coni = coni.astype(np.int)
            print('shape:',coni.shape,type(coni))
            cv2.imshow(str(i+1),coni.astype(np.uint8))
        
        cv2.waitKey(0)
        
demo2()
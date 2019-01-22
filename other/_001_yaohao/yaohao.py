'''
Created on 2019年1月21日

'''

import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt  

class yaohao():
    def __init__(self,begin_index = 3,cvs_path="",minloss=0.001,ckptpath='',maxdefpath=''):
        self.begin_index=begin_index
        self.cvs_path=cvs_path
        self.featurenum = 17
        self.layernum = 10
        self.minloss = minloss
        self.ckptpath = ckptpath
        self.maxdefpath = maxdefpath
        
    def getData(self,savemaxdef=False):
        df = pd.read_csv(filepath_or_buffer=self.cvs_path ,sep='\t')
        if savemaxdef:
            maxdef = df.max() #返回每一列的最大值
            np.savetxt(self.maxdefpath, np.array(maxdef)) 
        maxdef = np.loadtxt(self.maxdefpath) 
        #归一化数据
        df['time1']= df['time1']/maxdef[1]
        df['time2']= df['time1']/maxdef[2]
        df['b1']= df['b1']/maxdef[15]
        df['b2']= df['b2']/maxdef[16]
        df['b3']= df['b3']/maxdef[17]
        df['result']= df['result']/maxdef[18]
        X = df.values[:,1:-1]
        X = X.astype(np.float32)
        y = df.values[:,-1]
        y = y[:,np.newaxis] #行向量变列向量
        print('X:',X.shape)
        print('y:',y.shape)
        return X,y
    
    def getRealY(self,y):
        maxdef = np.loadtxt(self.maxdefpath)  #返回每一列的最大值
        return y*maxdef[18]
        
    def train(self,showplt=True,count=3):  
        X = tf.placeholder(dtype=tf.float32,shape=[None,self.featurenum])
        y = tf.placeholder(dtype=tf.float32,shape=[None,1])
        
        #定义神经网络中间层权值  
        w1 = tf.Variable(tf.random_normal([self.featurenum,self.layernum]))
        b1 = tf.Variable(tf.zeros([1,self.layernum]))
        p1 = tf.add(tf.matmul(X, w1), b1)
        logic1 = tf.sigmoid(p1)
        
        #输出层
        w2 = tf.Variable(tf.random_normal([self.layernum,1]))
        b2 = tf.Variable(tf.zeros([1,1]))
        p2 = tf.add(tf.matmul(logic1, w2), b2)

        tf.add_to_collection(tf.GraphKeys.WEIGHTS, w1)
        tf.add_to_collection(tf.GraphKeys.WEIGHTS, w2)
        regularizer = tf.contrib.layers.l2_regularizer(scale=5.0/50000)
        reg_term = tf.contrib.layers.apply_regularization(regularizer) 
        
        loss = tf.losses.mean_squared_error(labels=y, predictions=p2)
        #使用梯度下降  
        train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)#学习率设置为0.1  
        
        #训练count次，生成count个ckpt
        for j in range(count):
            with tf.Session() as sess:
                X_data,y_data = self.getData(savemaxdef=True)
                sess.run(tf.global_variables_initializer())
                losses = []
                i = 0;
                while True:
                    _loss,_p2,_ = sess.run([loss,p2,train_step],feed_dict={X:X_data, y:y_data})
                    losses.append(_loss);
                    if i%5000 == 0:
                        print(i,"---",_loss)
                    i = i + 1
                    if(_loss < self.minloss):
                        break;
                #存模型
                saver=tf.train.Saver()
                saver.save(sess,self.ckptpath.replace('{i}',str(j)))
                
                #转成真实的输出
                y_data = self.getRealY(y_data)
                _p2 = self.getRealY(_p2)
                
                #画图
                if showplt:
                    x_plt = [ i for i in range(y_data.shape[0])]
                    plt.scatter(x_plt, y_data)#画散点图  
                    plt.plot(x_plt, _p2, 'r-', lw = 5)#画预测的实线，红色  
                    plt.show()
                print('完成第',str(j),'个模型的训练')
            
    def predict(self,showplt=False,count=3):
        X = tf.placeholder(dtype=tf.float32,shape=[None,self.featurenum])
        
        #定义神经网络中间层权值  
        w1 = tf.Variable(tf.random_normal([self.featurenum,self.layernum]))
        b1 = tf.Variable(tf.zeros([1,self.layernum]))
        p1 = tf.add(tf.matmul(X, w1), b1)
        logic1 = tf.sigmoid(p1)
        
        #输出层
        w2 = tf.Variable(tf.random_normal([self.layernum,1]))
        b2 = tf.Variable(tf.zeros([1,1]))
        p2 = tf.add(tf.matmul(logic1, w2), b2)

        p2s = []
        #预测count次求平均值
        for j in range(3):
            with tf.Session() as sess:
                X_data,y_data = self.getData(savemaxdef=False)
                sess.run(tf.global_variables_initializer())
                
                #读取模型数据
                saver=tf.train.Saver()
                print('读取模型:',self.ckptpath+str(j))
                model_file=tf.train.latest_checkpoint(self.ckptpath.replace('{i}',str(j)))
                saver.restore(sess,model_file)
                _p2 = sess.run(p2,feed_dict={X:X_data})
                
                #转成真实的输出
                y_data = self.getRealY(y_data)
                _p2 = self.getRealY(_p2)
                
                
                print('_p2:',_p2)
                p2s.append(_p2)
                
        #画图
        if showplt:
            x_plt = [ i for i in range(y_data.shape[0])]
            plt.scatter(x_plt, y_data)#画散点图  
            plt.plot(x_plt, np.mean(p2s,axis=0), 'r-', lw = 5)#画预测的实线，红色  
            plt.show()
            
        return p2s,np.mean(p2s,axis=0)

type = 'test'  
# type = 'train'  
if type == 'train'  :
    #train-mean
    y = yaohao(cvs_path="data1/yaohao-train-mean.txt",minloss=0.0018,ckptpath='ckpt/mean{i}/mean.ckpt',maxdefpath='ckpt/mean/mean.maxdef')
    y.train(showplt=False,count=10)
     
    #train-min
    y = yaohao(cvs_path="data1/yaohao-train-min.txt",minloss=0.0018,ckptpath='ckpt/min{i}/min.ckpt',maxdefpath='ckpt/min/min.maxdef')
    y.train(showplt=False,count=10)
 
else:
    #predict-mean
    yao = yaohao(cvs_path="data1/yaohao-test-mean1.txt",ckptpath='ckpt/mean{i}',maxdefpath='ckpt/mean/mean.maxdef')
    pmeans = yao.predict(showplt=False,count=10)
     
    #predict-min
    y = yaohao(cvs_path="data1/yaohao-test-min1.txt",ckptpath='ckpt/min{i}',maxdefpath='ckpt/min/min.maxdef')
    pmins = y.predict(showplt=False,count=10)
    
    print('pmeans:',pmeans[0],'--',pmeans[1])
    print('pmins:',pmins[0],'--',pmins[1])

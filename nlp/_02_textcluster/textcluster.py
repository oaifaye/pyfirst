# utf-8
'''
Created on 2018年11月30日
文本聚类
'''

import jieba
import os
import pickle
from nlp._02_textcluster.utils import removeHTML
from nlp._02_textcluster import utils
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer,CountVectorizer
import numpy as np
import pymysql
from sklearn.cluster import KMeans
from util import DateUtil
from sklearn.decomposition import PCA

'''
01.创建分词文件
'''
class Cluster():
    '''
    '''
    def __init__(self, stopword_path = None):
        self.stopword_path = stopword_path
        pass
    
    '''执行分词'''
    def wordcut(self):
        pageSize = 1000
        db = pymysql.connect("10.0.251.50","root","1234qwer","cms_ju",charset='utf8' )
        cursor = db.cursor(pymysql.cursors.DictCursor)
        curpage = 0
        while(True):
            start = curpage * pageSize
            cursor.execute("select * from tj_news_clob order by news_id desc limit %s,%s",(start,pageSize))
            rows = cursor.fetchall()
            for row in rows:
                news_id = row['news_id']
                content = row['attribute_value']
                content = removeHTML(content)
                #内容长度超过50，可用
                if(len(content) > 50):
                    content_seg = jieba.cut(content)
                    seg = " ".join(content_seg)
                    sql = "UPDATE tj_news_clob SET available=1, seg='"+seg+"' WHERE  news_id='"+news_id+"'"
                    cursor.execute(sql)
            print('创建词向量：',curpage)
            if len(rows) < pageSize:
                break
            curpage = curpage + 1
        db.close()   
        print('中文预料分词结束')
        
    def getAllSeg(self):
        pageSize = 1000
        db = pymysql.connect("10.0.251.50","root","1234qwer","cms_ju",charset='utf8' )
        cursor = db.cursor(pymysql.cursors.DictCursor)
        curpage = 0
        segs = []
        newsids = []
        segstrs = []
        while(True):
            start = curpage * pageSize
            cursor.execute("select * from tj_news_clob where available=1 order by news_id desc limit %s,%s",(start,pageSize))
            rows = cursor.fetchall()
            for row in rows:
                news_id = row['news_id']
                newsids.append(news_id)
                seg = row['seg']
                segs.append(seg.split(" "))
                segstrs.append(seg)
            print('获取词向量：',curpage)
            if len(rows) < pageSize:
                break
            curpage = curpage + 1
        db.close()   
        print('获取词向量结束')
        return np.array(newsids),np.array(segstrs)
    
    def wordvector (self,sql = False):
        #1.读取停用词
        stpwrdlst = utils.readfile(self.stopword_path,encoding='UTF-8').splitlines()
        
        #2.取出分词后的词向量bunch对象
        newsids,content_segs = self.getAllSeg()
#         print('content_segs:',content_segs)
        
        #3.用TfidfVetorizer初始化向量空间模型
        #max_df：这个给定特征可以应用在 tf-idf 矩阵中，用以描述单词在文档中的最高出现率。假设一个词（term）在 80% 的文档中都出现过了，那它也许（在剧情简介的语境里）只携带非常少信息。
        #min_df：可以是一个整数（例如5）。意味着单词必须在 5 个以上的文档中出现才会被纳入考虑。设置为 0.2；即单词至少在 20% 的文档中出现 。
        vectorizer = TfidfVectorizer(stop_words=stpwrdlst,
                                     sublinear_tf=True,min_df=0.005,max_df=0.8)
#         vectorizer=CountVectorizer(stop_words=stpwrdlst)
        
        #文本转换为词频矩阵，单独保存字典文字
        transformer=TfidfTransformer()
        #tfidfspace其实是tf-idf权重
        tdm=transformer.fit_transform(vectorizer.fit_transform(content_segs))
        print('tdm:',tdm.shape)
        print("创建tf-idf词袋成功")
        '''
        #降维n_components：这个参数可以帮我们指定希望PCA降维后的特征维度数目。最常用的做法是直接指定降维到的维度数目，
                    此时n_components是一个大于等于1的整数。当然，我们也可以指定主成分的方差和所占的最小比例阈值，让PCA类自己去根据样本特征方差来决定降维到的维度数，
                    此时n_components是一个（0，1]之间的数。当然，我们还可以将参数设置为"mle", 此时PCA类会用MLE算法根据特征的方差分布情况自己去选择一定数量的主成分特征来降维。
                    我们也可以用默认值，即不输入n_components，此时n_components=min(样本数，特征数)。
        '''
#         pca = PCA()
#         print(vectorizer.fit_transform(content_segs))
#         print(np.array(tdm.toarray()))
#         tdm = pca.fit_transform(np.array(tdm.toarray()))
        
        #5.创建持久化词袋
        db = pymysql.connect("10.0.251.50","root","1234qwer","cms_ju",charset='utf8' )
        cursor = db.cursor(pymysql.cursors.DictCursor)
        wvDict = vectorizer.vocabulary_
        #key value互换
        wvDict = dict(zip(wvDict.values(), wvDict.keys()))
        print('wvDict.keys()',wvDict.keys())
        print('wvDict.values()',wvDict.values())
        if sql:
            for i in range(tdm.shape[0]):
                l = tdm[i]
                newsid = newsids[i]
                index = l.indices
                wv = self.getOneWv(l, wvDict)
                sql = "UPDATE tj_news_clob SET wv1='"+wv+"' ,wv_count="+str(len(index))+" WHERE  news_id='"+newsid+"'"
                cursor.execute(sql)
        db.close()  
        print('数据库插入词向量完成')
        return newsids,tdm
    
    def getOneWv(self,tdmline,wvDict):
        index = tdmline.indices
        data = tdmline.data
        #词向量组成的字符串
        wv = {}
        for j in range(len(index)):
            inx = index[j]
            #按照value找key
            zhongwen = wvDict[inx]
            da = data[j]
            wv[zhongwen] = str(da)
        wv = sorted(wv.items(),key = lambda x:x[1],reverse = True)
        wxstr = ''
        for i in range(len(wv)):
            wvlint = wv[i]
            if(i != 0):
                wxstr += ','
            wxstr += wvlint[0] +':'+wvlint[1]
        return wxstr
            
    def dokmeans(self,newsids,tdm,n_clusters,max_iter):
        km = KMeans(n_clusters=n_clusters,max_iter=max_iter)
        y_pred = km.fit_predict(tdm)
        print("kmeans完成")
#         print('km.cluster_centers_:',km.cluster_centers_)
        print('km.cluster_centers_size:',km.cluster_centers_.shape)
#         return
        db = pymysql.connect("10.0.251.50","root","1234qwer","cms_ju",charset='utf8' )
        cursor = db.cursor(pymysql.cursors.DictCursor)
        countdict = {}
        for i in range(len(y_pred)):
            group = y_pred[i]
            newsid = newsids[i]
            sql = "UPDATE tj_news_clob SET news_group="+str(group)+" WHERE  news_id='"+newsid+"'"
            cursor.execute(sql)
            if y_pred[i] in countdict.keys():
                countdict[y_pred[i]] = countdict[y_pred[i]]+1
            else:
                countdict[y_pred[i]]=1
        print('修改新闻类别成功')
        print('km.cluster_centers_.shape[0]:',km.cluster_centers_.shape[0])
        for k in range(km.cluster_centers_.shape[0]):
            sql1 = "INSERT INTO tj_cluster_centers (group_id, wv,count) VALUES ("+str(k)+", '"+str(km.cluster_centers_[k])+"',"+str(countdict[k])+")"
            cursor.execute(sql1)
        db.close()   
        print("修改类别成功")

np.set_printoptions(threshold=np.NaN)
start = DateUtil.nowToStrNormal()
print(start)
c = Cluster(stopword_path='hlt_stop_words.txt')
#分词
# c.wordcut()
#词向量
newsids, tdm = c.wordvector(sql=False)
print('tdm:',tdm.shape)
#kmeans
c.dokmeans(newsids, tdm,200,400)
print("start:",start,"  end:",DateUtil.nowToStrNormal())


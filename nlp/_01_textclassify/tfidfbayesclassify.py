# utf-8
'''
Created on 2018年11月12日

@author: Administrator
'''
import jieba
import os
import pickle
from nlp._01_textclassify.utils import removeHTML
from nlp._01_textclassify import utils
from sklearn.datasets.base  import Bunch
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer,CountVectorizer
from nlp._01_textclassify.utils import readfile, readbunchobj, writebunchobj
from sklearn.naive_bayes import  MultinomialNB,GaussianNB
from sklearn.metrics import classification_report
import numpy as np

'''
01.创建分词文件
'''
class Wordbag():
    '''
                建立分词之后的词袋
        corpus_path:初始分类文本的路径
        seg_path:分词后分类语料库路径
        wordbag_path:词袋存储目录
        wordbag_file_name:词袋文件名
    '''
    
    def __init__(self, corpus_path,seg_path,wordbag_path,wordbag_file_name):
        self.corpus_path = corpus_path
        self.seg_path = seg_path #分词后分类语料库路径
        self.wordbag_path = wordbag_path
        self.wordbag_file = self.wordbag_path + wordbag_file_name #分析语料Bunch对象持久化文件路径
    
    def savefile(self,savepath,content,encoding='utf-8'):
        fp = open(savepath,'w',encoding=encoding)
        fp.write(content)
        fp.close()
        
    def readfile(self,savepath,encoding='utf-8'):
        fp = open(savepath,'r',encoding=encoding)
        content = fp.read()
        fp.close()
        return content
    
    '''执行分词'''
    def wordcut(self):
        catelist = os.listdir(self.corpus_path)
        for mydir in catelist:
            class_path = self.corpus_path + mydir+"/"
            seg_dir = self.seg_path + mydir+"/"
            if not os.path.exists(seg_dir) :
                os.makedirs(seg_dir)
            file_list = os.listdir(class_path)
            for file_path in file_list:
                fullname = class_path + file_path 
                content = utils.readfile(fullname).strip()
                content = removeHTML(content)
                content  = content.replace("\r\n","").strip()
                content_seg = jieba.cut(content)
                utils.savefile(seg_dir+file_path," ".join(content_seg))
        print('中文预料分词结束:',self.corpus_path)
    
    '''将分词后的结果转换成对象本地化'''
    def wordbunch(self):
        #Bunch类提供一种key,value的对象形式，每个key的含义：
        #target_name :所有分类集名称列表
        #label：每个文件的分类标签列表
        #filenames：文件路径
        #contents：分词后文件词向量形式
        bunch = Bunch(target_name=[],label=[],filenames=[],contents=[])
        catelist = os.listdir(self.seg_path)
        bunch.target_name.extend(catelist)
        for mydir in catelist:
            class_path = self.seg_path + mydir + '/'
            file_list = os.listdir(class_path)
            for file_path in file_list:
                fullname = class_path + file_path
                bunch.label.append(mydir) #保存当前文件的标签
                bunch.filenames.append(fullname)#保存当前文件路径
                print(fullname)
                bunch.contents.append(utils.readfile(fullname).strip())
        if not os.path.exists(self.wordbag_path):
            os.makedirs(self.wordbag_path)
        file_obj = open(self.wordbag_file,'wb')
        pickle.dump(bunch,file_obj)
        file_obj.close()
        print("构建文本对象结束：",self.seg_path)


class TrainWordVector():
    '''2.生成训练词向量'''
    
    def __init__(self,stopword_path,bunch_path,space_path):
        self.stopword_path = stopword_path
        self.bunch_path = bunch_path
        self.space_path = space_path
    
    def wordvector (self):
        np.set_printoptions(threshold=np.NaN)
        #1.读取停用词
        stpwrdlst = utils.readfile(self.stopword_path,encoding='UTF-8').splitlines()
            
        #2.导入分词后的词向量bunch对象
        bunch = utils.readbunchobj(self.bunch_path)
        
        #3.构建TF-IDF词向量空间对象
        #    vocabulary:词汇表
        tfidfspace = Bunch(target_name=bunch.target_name,
                           label=bunch.label,
                           filenames = bunch.filenames,
                           tdm = [],vocabulary={})
        
        #4.用TfidfVetorizer初始化向量空间模型
        #max_df：这个给定特征可以应用在 tf-idf 矩阵中，用以描述单词在文档中的最高出现率。假设一个词（term）在 80% 的文档中都出现过了，那它也许（在剧情简介的语境里）只携带非常少信息。
        #min_df：可以是一个整数（例如5）。意味着单词必须在 5 个以上的文档中出现才会被纳入考虑。设置为 0.2；即单词至少在 20% 的文档中出现 。
#         vectorizer1 = TfidfVectorizer(stop_words=stpwrdlst,
#                                      sublinear_tf=True)
        vectorizer=CountVectorizer(stop_words=stpwrdlst)
        
        #文本转换为词频矩阵，单独保存字典文字
        transformer=TfidfTransformer()
        #tfidfspace其实是tf-idf权重
        tfidfspace.tdm=transformer.fit_transform(vectorizer.fit_transform(bunch.contents))
#         print(vectorizer.fit_transform(bunch.contents))
#         print(np.array(tfidfspace.tdm.toarray()))
        tfidfspace.vocabulary = vectorizer.vocabulary_
        #5.创建持久化词袋
        writebunchobj(self.space_path, tfidfspace)
        print("创建tf-idf词袋成功")

class TestWordVector():
    '''3.生成测试词向量'''
    
    def __init__(self,stopword_path,bunch_path,train_space_path,test_space_path):
        self.stopword_path = stopword_path
        self.bunch_path = bunch_path
        self.train_space_path = train_space_path
        self.test_space_path = test_space_path
    
    def wordvector (self):
        #1.读取停用词
        stpwrdlst = readfile(self.stopword_path).splitlines()
            
        #2.导入分词后的词向量bunch对象
        bunch = readbunchobj(self.bunch_path)
        
        #3.构建TF-IDF词向量空间对象
        #    vocabulary:词汇表
        testspace = Bunch(target_name=bunch.target_name,
                           label=bunch.label,
                           filenames = bunch.filenames,
                           tdm = [],vocabulary={})
        #4.导入训练集词袋
        trainbunch  =readbunchobj(self.train_space_path)
        
        #5.用TfidfVetorizer初始化向量空间模型
        #max_df：这个给定特征可以应用在 tf-idf 矩阵中，用以描述单词在文档中的最高出现率。假设一个词（term）在 80% 的文档中都出现过了，那它也许（在剧情简介的语境里）只携带非常少信息。
        #min_df：可以是一个整数（例如5）。意味着单词必须在 5 个以上的文档中出现才会被纳入考虑。设置为 0.2；即单词至少在 20% 的文档中出现 。
#         vectorizer = TfidfVectorizer(stop_words=stpwrdlst,
#                                      sublinear_tf=True,max_df=1,min_df=1,
#                                      vocabulary=trainbunch.vocabulary)
        vectorizer=CountVectorizer(stop_words=stpwrdlst,vocabulary=trainbunch.vocabulary)
        transformer=TfidfTransformer()
        #文本转换为词频矩阵，单独保存字典文字
        testspace.tdm=transformer.fit_transform(vectorizer.fit_transform(bunch.contents))
        testspace.vocabulary = vectorizer.vocabulary_
        
        #5.创建持久化词袋
        space_path = self.test_space_path
        writebunchobj(space_path, testspace)
        
        print("创建test词袋成功")
        
class Predict():
    '''
        train_word_bag训练向量对象的路径
        test_word_bag测试 向量对象的路径
    '''
    
    def predictbyfile(self,trainpath,testpath):
        train_set = readbunchobj(trainpath)
        test_set = readbunchobj(testpath)
        self.predictbybunch(train_set, test_set)
        
    def predictbybunch(self,train_set,test_set):
        #朴素贝叶斯多项式算法
        #alpha越小，迭代次数越多，精度越高
        clf = MultinomialNB(alpha=0.1).fit(train_set.tdm, train_set.label)
        #预测
        predicted = clf.predict(test_set.tdm)
        print(predicted)
        print(classification_report(test_set.label,predicted))
    
    '''模型训练好后，直接根据一段文本判断类型'''
    def fastpredict(self,content,stopword_path,train_space_path):
        #1.读取停用词
        stpwrdlst = readfile(stopword_path).splitlines()
        #2.content转换成词向量
        content = removeHTML(content)
        content  = content.replace("\r\n","").strip()
        content_seg = jieba.cut(content)
        #3.导入训练集词袋
        trainbunch  =readbunchobj(train_space_path)
        vectorizer = TfidfVectorizer(stop_words=stpwrdlst,
                                     sublinear_tf=True,max_df=1,min_df=1,
                                     vocabulary=trainbunch.vocabulary)
        tdm = vectorizer.fit_transform([" ".join(content_seg)])
        #4.预测，alpha越小，迭代次数越多，精度越高
        clf = MultinomialNB(alpha=0.001).fit(trainbunch.tdm, trainbunch.label)
        predicted1 = clf.predict_proba(tdm)
        predicted2 = clf.predict(tdm)
        print(predicted1,predicted2)
        return predicted1,predicted2

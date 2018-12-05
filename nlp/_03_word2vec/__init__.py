#utf-8
'''
https://www.cnblogs.com/Lin-Yi/p/9007259.html
'''

from gensim.models import word2vec
from gensim.models.word2vec import LineSentence
import jieba
import pymysql

class MyWord2vec():
    '''
    # 配置词向量的维度
    num_features = 1000
    # 保证被考虑的词汇的频度
    min_word_count = 5
    # 并行计算使用cpu核心数量
    num_workers = 2
    # 定义训练词向量的上下文窗口大小
    context = 5
    downsapling = 1e-3
    '''
    def __init__(self,num_features = 1000,min_word_count = 5,num_workers = 2,context = 5,
                 downsapling = 1e-3,stop_words='hlt_stop_words.txt',model_path=None,txt_path = None):
        # 配置词向量的维度
        self.num_features = num_features
        # 保证被考虑的词汇的频度
        self.min_word_count = min_word_count
        # 并行计算使用cpu核心数量
        self.num_workers = num_workers
        # 定义训练词向量的上下文窗口大小
        self.context = context
        # 下采样
        self.downsapling = downsapling
        self.stop_words = stop_words
        self.txt_path = txt_path
        self.model_path = model_path
        
    #获取停用词
    def getstopwords(self):
        # step 1 读取停用词
        stop_words = []
        with open(self.stop_words,encoding='utf-8') as f:
            line = f.readline()
            while line:
                stop_words.append(line[:-1])
                line = f.readline()
        stop_words = set(stop_words)
        return stop_words
        
    def train(self):
        stop_words = self.getstopwords()
        sentences = []
        with open(self.txt_path,encoding='utf-8') as f:
            line = f.readline()
            while line:
                nostopwords = list(jieba.cut(line,cut_all=False))
                line_words = []
                for word in nostopwords:
                    if word not in stop_words:
                        line_words.append(word)
                sentences.append(line_words)
                line = f.readline()
        print('开始word2vec...')
        # 训练词向量模型
        model = word2vec.Word2Vec(sentences=sentences,
                                  workers=self.num_workers,
                                  size=self.num_features,
                                  min_count=self.min_word_count,
                                  window=self.context,
                                  sample=self.downsapling)
        # 这个设定代表当前训练好的词向量为最终版, 也可以加速模型训练的速度
        # model.init_sims(replace=True)
        print('开始保存模型...')
        model.save(self.model_path)
        print('训练完成...')
        
    def test(self,words,topn=10):
        model = word2vec.Word2Vec.load(self.model_path)
        wordslink = []
        for w in words:
#             print(w,':',model.wv.similar_by_word(w, topn = topn))
            link = model.wv.similar_by_word(w, topn = topn)
            wordslink.append(link)
        return wordslink
    
    #生成词频的排名 wordcount_file:生成的词频文件
    def wordsorder(self,wordcount_file,insert2mysql=False):
        # step 1 读取停用词
        stop_words = self.getstopwords()
        word_lst = []
        with open(self.txt_path,encoding='utf-8') as f:
            line = f.readline()
            while line:
                nostopwords = list(jieba.cut(line,cut_all=False))
                for word in nostopwords:
                    if word not in stop_words:
                        word_lst.append(word)
                line = f.readline()
        word_dict= {}
        with open(wordcount_file,'w') as wf2: #打开文件
            for item in word_lst:
                if item not in word_dict: #统计数量
                    word_dict[item] = 1
                else:
                    word_dict[item] += 1
            orderList=list(word_dict.values())
            orderList.sort(reverse=True)
            if insert2mysql:
                db = pymysql.connect("10.0.251.50","root","1234qwer","real_calc_20180410",charset='utf8' )
                cursor = db.cursor(pymysql.cursors.DictCursor)
            for i in range(len(orderList)):
                for key in word_dict:
                    if word_dict[key]==orderList[i] and key != '\n':
                        try:
                            wf2.write(key+' '+str(word_dict[key])+'\n') #写入txt文档
                            if insert2mysql:
                                cursor.execute("INSERT INTO tj_words (word, count, list_order, canshow) VALUES ('%s', %s, 1, -1);" % (key,str(word_dict[key])))
                        except Exception as e:
                            print(e)
                        word_dict[key]=0
            if insert2mysql:  
                cursor.close()   
                
    def insertWordsLinkByNum(self,limit,wordscount = 20):    
        db = pymysql.connect("10.0.251.50","root","1234qwer","real_calc_20180410",charset='utf8' )
        cursor = db.cursor(pymysql.cursors.DictCursor)
        sql = "select * from tj_words a order by a.count desc limit %s" % (limit)
        cursor.execute(sql)
        rows = cursor.fetchall()
        words = []
        for row in rows:
            words.append(row['word'])
        self.insertWordsLinkByWords(words,wordscount)
    
    def insertWordsLinkByWords(self,words,wordscount= 20):
        wordslinks = self.test(words, wordscount)
        print('开始插入数据库...')
        print(wordslinks)
        db = pymysql.connect("10.0.251.50","root","1234qwer","real_calc_20180410",charset='utf8' )
        cursor = db.cursor(pymysql.cursors.DictCursor)
        for i in range(len(words)):
            print(i)
            word = words[i]
            wordslink = wordslinks[i]
            for j in range(len(wordslink)):
                wl = wordslink[j]
                sql = "INSERT INTO tj_words_link (word, link_word, weight, list_order) VALUES ('%s', '%s', %s, %s)" % (word,wl[0],wl[1],str(j+1))
                cursor.execute(sql)
        cursor.close()    
        
myWord2vec = MyWord2vec(model_path='model_file/word2vec.model',txt_path = 'news-all.txt')
#生成词频的排名
# myWord2vec.wordsorder('wordCount1.txt',True)
#执行训练
# myWord2vec.train()
words = ['习近平','总书记','政府','公司','天津','北方网','中国','服务','天津','建设',
         '文化','创新','孩子','平台','建设','经济','科技','智能','数据','城市',
         '未来','北京','社会','健康','学习','未来','集团','环境','社区','产业']
#测试
# myWord2vec.test(words,15)
#插入词关系
myWord2vec.insertWordsLinkByNum(1000,40)
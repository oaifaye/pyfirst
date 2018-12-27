'''
Created on 2018年12月7日
'''
#coding=utf-8
'''
Created on 2017-12-12
文章地址：https://blog.csdn.net/u011311291/article/details/78836535

gensim API地址:
https://radimrehurek.com/gensim/apiref.html

本篇对gensim讲解分为3大类
1.gensim字典的基本使用，其中和jieba结合使用
2.gensim模型的使用,比如tf-idf模型，lsi模型（用于求文本相似度）等
3.gensim的数据类型和Numpy，Scipy的转换
'''
import jieba
from gensim import corpora, models, similarities
# 一.gensim字典的基本使用
# 加载数据
# 从文件加载
# files = []
# f1 = open("demo1/01.txt", "r").read()
# f2 = open("demo1/02.txt", "r").read()
# files.append(f1)
# files.append(f2)
# 
# # 文件数据切词
# text1 = [[word for word in jieba.cut(f1)]]
# text2 = [[word for word in jieba.cut(f2)]]
# texts = [[word for word in jieba.cut(file)] for file in files]

# 生成字典,prune_at的作用为控制向量的维数，也就是说最多能为2000000个词语进行向量化
# dictionary = corpora.Dictionary(texts,prune_at=2000)
# # 可以这样分开添加使用
# dictionary = corpora.Dictionary(text1,prune_at=2000)
# # 对字典进行扩容
# dictionary.add_documents(text2, prune_at=2000)
# 或者手动设置一次词语，但这个方法一般用来打印所有的词语和编号print dictionary.token2id或者print dictionary.id2token
# dictionary.token2id = {'computer': 0, 'human': 1, 'response': 2, 'survey': 3}
# 合并字典
# dict1 = corpora.Dictionary(some_documents)
# dict2 = corpora.Dictionary(other_documents)
# dict2_to_dict1 = dict1.merge_with(dict2)


# 加载数据
wordslist = ["我在玉龙雪山","我喜欢玉龙雪山","我还要去玉龙雪山"] 
# 切词
textTest = [[word for word in jieba.cut(words)] for words in wordslist]
# 生成字典
dictionary = corpora.Dictionary(textTest,prune_at=2000)
# 保存生成的字典
dictionary.save('demo1/dict1.dict')
dictionary.save_as_text('demo1/text_dict1.dict',  sort_by_word=True)
#dictionary.save_as_text保存的形式：
# 1 在 1
# 5 还要 1
# 0 我 3
# 2 玉龙雪山 3
# 3 喜欢 1
# 4 去 1
# 加载字典
dictionary.load('demo1/dict1.dict')
# dictionary.load_from_text('D:\\machinetest\\gensim\\dict.dict')

# 遍历字典
print ('dictionary.keys():',dictionary.keys())    #返回所有词语的编号
print ('dictionary.dfs:',dictionary.dfs)    #{单词id，在多少文档中出现}
print ('dictionary.get(5):',dictionary.get(5)) #返回编号对应的词语，例如这里5->特性。
print ('dictionary.compactify():',dictionary.compactify()) #压缩词语向量，如果使用了filter_extremes，filter_n_most_frequent，filter_tokens等删除词典元素的操作，可以使用该方法进行压缩
print ('dictionary.num_docs:',dictionary.num_docs) #所有文章数目
print ('dictionary.num_nnz:',dictionary.num_nnz) #每个文件中不重复词个数的和
print ('dictionary.num_pos:',dictionary.num_pos) #所有词的个数
for key in dictionary.iterkeys():
    print (key,dictionary.get(key),dictionary.dfs[key])
# 1 在 1
# 5 还要 1
# 0 我 3
# 2 玉龙雪山 3
# 3 喜欢 1
# 4 去 1

# 过滤字典
# dictionary.filter_extremes(no_below=2, no_above=0.8,keep_n=3 ) #过滤字典,过滤词的出现数量小于2，词频>0.8,且只取前3项
# dictionary.filter_n_most_frequent(2) #过滤出现次数最多的前两个词语
# dictionary.filter_tokens(good_ids=[0]) #good_ids=[0,2]表示仅保留编号为0,2的词语，bad_ids=[1,3]表示要删除编号为1,3的词语
# # 如果想要过滤掉出现次数为1的词，可以使用以下代码
# ids=[]
# for key in dictionary.iterkeys():
#     if dictionary.dfs[key]==1:
#         ids.append(key)
# dictionary.filter_tokens(bad_ids=ids)
# print "过滤后:"
# for key in dictionary.iterkeys():
#     print key,dictionary.get(key),dictionary.dfs[key]

# 向量化
# 将要向量化的数据,注意test是list<list>
wordstest = "我去玉龙雪山并且喜欢玉龙雪山"
# 切词
test = [word for word in jieba.cut(wordstest)]
# 将数据向量化doc2bow(document, allow_update=False, return_missing=False)，其实这一步生成了向量化词袋
corpus,missing = dictionary.doc2bow(test,return_missing=True)
print (corpus,missing)
# [(0, 1), (2, 2), (3, 1), (4, 1)] {u'\u5e76\u4e14': 1}
print (type(corpus))
# <type 'list'>,返回的是list类型
# 将test变成词汇编号list,但我这个gensim版本还不支持
# test_idx = dictionary.doc2idx(test, unknown_word_index=-1)
# print test_idx
# [0,4,2,-1,3,2]

# # 保存语料库，保存的格式有多种形式， Market Matrix，Joachim’s SVMlight、Blei’s LDA-C、GibbsLDA++
# # 将向量化后的词典保存,保存后生成两个文件，一个corpora.mm，分别(文章序号(从1开始),词向量编号，次出现的次数)，一个corpora.mm.index
# corpus_list = [corpus]
# corpora.MmCorpus.serialize('D:\\machinetest\\gensim\\corpora.mm', corpus_list)
# # corpora.SvmLightCorpus.serialize('D:\\machinetest\\gensim\\corpora.svmlight', corpus_list)
# # corpora.BleiCorpus.serialize('D:\\machinetest\\gensim\\corpora.lda-c', corpus_list)
# # corpora.LowCorpus.serialize('D:\\machinetest\\gensim\\corpora.low', corpus_list)

# # 加载语料库
# corpus_2 = corpora.MmCorpus('D:\\machinetest\\gensim\\corpora.mm')
# # corpus_2 = corpora.MmCorpus('D:\\machinetest\\gensim\\corpora.svmlight')
# # corpus_2 = corpora.MmCorpus('D:\\machinetest\\gensim\\corpora.lda-c')
# # corpus_2 = corpora.MmCorpus('D:\\machinetest\\gensim\\corpora.low')
# print type(corpus_2)
# # <class 'gensim.corpora.mmcorpus.MmCorpus'>
# # 需要转换成list
# corpus_list_2 =  list(corpus_2)
# print corpus_list_2
# # [[(0, 1.0), (2, 2.0), (3, 1.0), (4, 1.0)]]
# # 合并语料库
# merged_corpus = itertools.chain(corpus1, corpus2)

# 二.gensim的模型model模块，可以对corpus进行进一步的处理，比如tf-idf模型，lsi模型，lda模型等
wordstest_model = ["我去玉龙雪山并且喜欢玉龙雪山玉龙雪山","我在玉龙雪山并且喜欢玉龙雪山"]
test_model = [[word for word in jieba.cut(words)] for words in wordstest_model]
corpus_model= [dictionary.doc2bow(test) for test in test_model]
print (corpus_model)
# [[(0, 1), (2, 3), (3, 1), (4, 1)], [(0, 1), (1, 1), (2, 2), (3, 1)]]
# 目前只是生成了一个模型,并不是将对应的corpus转化后的结果,里面存储有各个单词的词频，文频等信息
tfidf_model = models.TfidfModel(corpus_model)
#使用测试文本来测试模型，提取关键词,test_bow提供当前文本词频，tfidf_model提供idf计算
testword = "我去玉龙雪山"
test_bow = dictionary.doc2bow([word for word in jieba.cut(testword)])
print (tfidf_model[test_bow])
# [(4, 1.0)]，可见'去'字成为关键词
# print tfidf_model.dfs #{单词id，在多少文档中出现}
# # 通过gensim.models.tfidfmodel.df2idf(docfreq, totaldocs, log_base=2.0, add=0.0)方法计算idf值
# # 即idf = add + log(totaldocs / doc_freq),这种算法可能会出现0值
# print tfidf_model.idfs #{单词id，idf值}，
# print tfidf_model.id2word
# print tfidf_model.num_docs #所有文章数目
# print tfidf_model.normalize #是否规范化处理
# print tfidf_model.num_nnz #每个文件中不重复词个数的和4+4 =8
# # {0: 2, 1: 1, 2: 2, 3: 2, 4: 1}
# # {0: 0.0, 1: 1.0, 2: 0.0, 3: 0.0, 4: 1.0}
# # None
# # 2
# # True
# # 8
# # 将文档转化成tf-idf模式表示的向量
# 保存模型和加载模型
# tfidf_model.save('/tmp/foo.tfidf_model',)
# tfidf_model = models.TfidfModel.load('/tmp/foo.tfidf_model',mmap=None)


# # 三.gensim和NumPy,SciPy高效相互转换
# # NumPy转gensim,可以看出numpy的列代表字典中向量编号，列值代表字典中的词语次数，且numpy类型不受限制
# import gensim
# import numpy as np
# numpy_matrix = np.mat([[1,5],[3,4]])
# numpy_array = np.array([[1,5],[3,4]])
# corpus_matrix = gensim.matutils.Dense2Corpus(numpy_matrix)
# print list(corpus_matrix)
# # [[(0, 1.0), (1, 3.0)], [(0, 5.0), (1, 4.0)]]
# corpus_array = gensim.matutils.Dense2Corpus(numpy_array)
# print list(corpus_array)
# # [[(0, 1.0), (1, 3.0)], [(0, 5.0), (1, 4.0)]]
# # gensim转Numpy,num_terms为n_feature维数（一般numpy矩阵都为(n_sample,n_feature)形式)
# numpy_matrix2 = gensim.matutils.corpus2dense(corpus_matrix, num_terms=3)
# print type(numpy_matrix2)
# print numpy_matrix2
# # <type 'numpy.ndarray'>
# # [[ 1.  5.]
# #  [ 3.  4.]
# #  [ 0.  0.]]

# 在处理文本数据中的一般使用
# import jieba
# from gensim import corpora
# f1 = "我在玉龙雪山,我喜欢玉龙雪山,我还要去玉龙雪山"
# text1 = [[word for word in jieba.cut(f1)]]
# dictionary = corpora.Dictionary(text1,prune_at=2000000)
# f2 = ["我在吃东西","我在玉龙雪山,我喜欢玉龙雪山,我还要去玉龙雪山"]
# text2 = [[word for word in jieba.cut(f)] for f in f2]
# corpus = [dictionary.doc2bow(text,return_missing=False) for text in text2]
# print corpus
# [[(0, 1), (3, 1)], [(0, 1), (1, 1), (2, 2), (3, 3), (4, 3), (5, 1), (6, 1)]]
# import gensim
# numpy_matrix2 = gensim.matutils.corpus2dense(corpus, num_terms=len(dictionary.keys()))
# 由原来的稀疏矩阵变成正常的矩阵了
# print numpy_matrix2
# [[ 1.  1.]
#  [ 0.  1.]
#  [ 0.  2.]
#  [ 1.  3.]
#  [ 0.  3.]
#  [ 0.  1.]
#  [ 0.  1.]]
# # 记住这里需要对矩阵进行转置
# print numpy_matrix2.T
# [[ 1.  0.  0.  1.  0.  0.  0.]
#  [ 1.  1.  2.  3.  3.  1.  1.]]

# # SciPy也可以用同样的方式进行转换
# # corpus = gensim.matutils.Sparse2Corpus(scipy_sparse_matrix)
# # scipy_csc_matrix = gensim.matutils.corpus2csc(corpus)
# # 使用拿来训练的时候记得scipy_csc_matrix.T进行转置

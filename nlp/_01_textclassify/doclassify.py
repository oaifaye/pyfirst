#utf-8
'''
Created on 2018年11月12日

@author: Administrator
'''
from nlp._01_textclassify.tfidfbayesclassify import Wordbag, TrainWordVector,\
    TestWordVector, Predict
from nlp._01_textclassify import utils

def train():
    corpus_path = 'train_corpus_small/'
    seg_path = 'train_corpus_seg/' #分词后分类语料库路径
    wordbag_path = 'train_word_bag/'
    wordbag_file = "train_set.dat" #分析语料Bunch对象持久化文件路径 
    wordbag = Wordbag(corpus_path,seg_path,wordbag_path,wordbag_file)
    wordbag.wordcut()
    wordbag.wordbunch()
    
    stopword_path = "hlt_stop_words.txt"
    bunch_path = "train_word_bag/train_set.dat"
    space_path = "train_word_bag/tfidfspace.dat"
    trainWordVector = TrainWordVector(stopword_path,bunch_path,space_path)
    trainWordVector.wordvector()
    
def test():
    corpus_path = 'test_corpus_small/'
    seg_path = 'test_corpus_seg/' #分词后分类语料库路径
    wordbag_path = 'test_word_bag/'
    wordbag_file = "test_set.dat" #分析语料Bunch对象持久化文件路径
    wordbag = Wordbag(corpus_path,seg_path,wordbag_path,wordbag_file)
    wordbag.wordcut()
    wordbag.wordbunch()
    
    stopword_path = "hlt_stop_words.txt"
    bunch_path = "test_word_bag/test_set.dat"
    train_space_path = "train_word_bag/tfidfspace.dat"
    test_space_path = "test_word_bag/testspace.dat"
    testWordVector = TestWordVector(stopword_path,bunch_path,train_space_path,test_space_path)
    testWordVector.wordvector()

def predict():
    trainpath = 'train_word_bag/tfidfspace.dat'
    testpath = 'test_word_bag/testspace.dat'
    p = Predict()
    p.predictbyfile(trainpath, testpath)
    
# def initfastpredict():
    
    
def fastpredict():
    p = Predict()
    content = utils.readfile('fastpredict/content.txt')
    stopword_path = "hlt_stop_words.txt"
    train_space_path = 'train_word_bag/tfidfspace.dat'
    return p.fastpredict(content, stopword_path,train_space_path)
    
train()
test()
predict()

# fastpredict()
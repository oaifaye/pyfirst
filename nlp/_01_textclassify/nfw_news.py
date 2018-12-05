'''
Created on 2018年11月11日

@author: Administrator
'''
#utf-8

import pymysql
import os
from nlp._01_textclassify.utils import removeHTML,savefile

def makeOneType(root_path,channel_id,start,end,size):
    print(root_path)
    db = pymysql.connect("10.0.252.201","root","1234qwer","go_cms6_20171109" ,charset='utf8')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute("select * from tn_news_clob b where b.attribute_name='content' and b.news_id in (select a.news_id from tn_news a where a.channel_id="+str(channel_id)+" and a.state=2000 ) order by b.news_id desc limit "+str(start)+", "+str(end)+"  ")
    rows = cursor.fetchall()
    i= 0
    for row in rows:
        try:
            content = row['attribute_value']
            content = removeHTML(content)
            if len(content) < 200:
                continue
            if i == size:
                continue
            if i < 10:
                file_name = '00'+str(i)
            elif i <100:
                file_name = '0'+str(i)
            elif i <size:
                file_name = str(i)
            else:
                break
            if not os.path.exists(root_path):
                os.makedirs(root_path)
            
            savefile(root_path+file_name+".txt", content)
            i = i + 1
        except :
            print(row['news_id'])
    db.close()   

trainstart = 0
trainend=150
trainsize=120
makeOneType('train_corpus_small/001_it/','15000000000000000',trainstart,trainend,trainsize)
makeOneType('train_corpus_small/002_tiyu/','16004000000000000',trainstart,trainend,trainsize)
makeOneType('train_corpus_small/003_caijing/','14014000000000000',trainstart,trainend,trainsize)
makeOneType('train_corpus_small/004_qiche/','24037000000000000',trainstart,trainend,trainsize)
makeOneType('train_corpus_small/005_jiaoyu/','19001000000000000',trainstart,trainend,trainsize)
makeOneType('train_corpus_small/006_lvyou/','6041002000000000',trainstart,trainend,trainsize)
makeOneType('train_corpus_small/007_zhengmin/','59002000000000000',trainstart,trainend,trainsize)
makeOneType('train_corpus_small/008_wenyu/','21008000000000000',trainstart,trainend,trainsize)
#test
teststart = 601
testend=80
testsize=40
makeOneType('test_corpus_small/001_it/','15000000000000000',teststart,testend,testsize)
makeOneType('test_corpus_small/002_tiyu/','16004000000000000',teststart,testend,testsize)
makeOneType('test_corpus_small/003_caijing/','14014000000000000',teststart,testend,testsize)
makeOneType('test_corpus_small/004_qiche/','24037000000000000',teststart,testend,testsize)
makeOneType('test_corpus_small/005_jiaoyu/','19001000000000000',teststart,testend,testsize)
makeOneType('test_corpus_small/006_lvyou/','6041002000000000',teststart,testend,testsize)
makeOneType('test_corpus_small/007_zhengmin/','59002000000000000',teststart,testend,testsize)
makeOneType('test_corpus_small/008_wenyu/','21008000000000000',teststart,testend,testsize)
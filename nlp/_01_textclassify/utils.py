# -*- coding: utf-8 -*-
import pickle
import re

def readbunchobj(path):
    file_obj = open(path,'rb')
    bunch = pickle.load(file_obj)
    file_obj.close()
    return bunch

def writebunchobj(path,bunchobj):
    file_obj = open(path,'wb')
    pickle.dump(bunchobj,file_obj)
    file_obj.close()
    
def readfile(savepath,encoding='UTF-8'):
    fp = open(savepath,'r',encoding=encoding )
    content = fp.read()
    fp.close()
    return content

def savefile(savepath,content,encoding='UTF-8'):
    fp = open(savepath,'w',encoding=encoding)
    fp.write(content)
    fp.close()

def removeHTML(content):
    content = re.sub('<\s*head[^>]*>[^<]*<\s*/\s*head\s*>','',content)
    content = re.sub('<\s*style[^>]*>[^<]*<\s*/\s*style\s*>','',content)
    content = re.sub('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>','',content)
    content = re.sub('<\s*HEAD[^>]*>[^<]*<\s*/\s*HEAD\s*>','',content)
    content = re.sub('<\s*STYLE[^>]*>[^<]*<\s*/\s*STYLE\s*>','',content)
    content = re.sub('<\s*SCRIPT[^>]*>[^<]*<\s*/\s*SCRIPT\s*>','',content)
    content = re.sub('<[^>]+>','',content)
    content = re.sub('%!.*!%','',content)
    content = content.replace("\r\n","").strip()
    content = content.replace("\n","").strip()
    content = content.replace("\t","").strip()
    content = content.replace(" ","").strip()
    content = content.replace("　","").strip()
    content = content.replace("&nbsp;","").strip()
    content = content.replace("&ldquo;","").strip()
    content = content.replace("&bull;","").strip()
    content = content.replace("&rdquo;","").strip()
    content = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）：《》「」•●]+", "",content)
    return content

# str = readfile("D:\\pythonCode\\First\\nlp\\_01_textclassify\\fastpredict\\content.txt")
# print(removeHTML(str))
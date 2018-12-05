# -*- coding: utf-8 -*-

import numpy as np

#将数组写进文件
def writeArray(arr=[],fileName='',append=False):
    narr = np.array(arr);
    print(narr)
    print(narr.shape)

def readfile(savepath,encoding='UTF-8'):
    fp = open(savepath,'r',encoding=encoding )
    content = fp.read()
    fp.close()
    return content

def savefile(savepath,content,encoding='UTF-8'):
    fp = open(savepath,'w',encoding=encoding)
    fp.write(content)
    fp.close()
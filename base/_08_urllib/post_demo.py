# coding=utf-8
#================================================================
#
#   File name   : post_demo.py
#   Author      : Faye
#   Created date: 2020/9/24 13:18 
#   Description :
#
#================================================================

#post 请求
import urllib.request
import urllib.parse
base_url="http://www.iqianyue.com/mypost/"
data={
    "name":"ceo@iqianyue.com",
    "pass":"aA123456"
}
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"}
postdata=urllib.parse.urlencode(data).encode('utf-8')
req=urllib.request.Request(url=base_url,headers=headers,data=postdata,method='POST')
response=urllib.request.urlopen(req)
html=response.read()
# html=response.read().decode('utf-8')  #这里讲解一下decode()是把bytes转化解码为了 str ,
# 但是写入文本的话，是不需要解码的，解码了str写不进去，
print(html)

#把文件写入G盘
text=open('G:/post.html',"wb")
text.write(html)
text.close()
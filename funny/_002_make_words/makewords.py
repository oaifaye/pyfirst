from urllib.request import urlopen
from random import randint
from bs4 import BeautifulSoup
import re
import pymysql
import jieba

def getdata():
    db = pymysql.connect("127.0.0.1", "root", "123456", "makewords", charset='utf8')
    cursor = db.cursor(pymysql.cursors.DictCursor)
    cursor.execute("select * from tm_news ")
    rows = cursor.fetchall()
    data = rows[0]['content']
    db.close()
    return data

def wordListSum(wordList):
    sum = 0
    for word, value in wordList.items():
        sum = sum + value
    return sum


def retrieveRandomWord(wordList):
    randomIndex = randint(1, wordListSum(wordList))
    for word, value in wordList.items():
        randomIndex -= value
        if randomIndex <= 0:
            return word

def buildWordDict(text):
    text = re.sub('(\n|\r|\t)+', " ", text)
    text = re.sub('\"', "", text)

    punctuation = [',', '.', ';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, " " + symbol + " ")

    text = " ".join(jieba.lcut(text))
    words = text.split(' ')

    words = [word for word in words if word != ""]
    wordDict = {}
    for i in range(1, len(words)):
        if words[i-1] not in wordDict:
            wordDict[words[i-1]] = {}
        if words[i] not in wordDict[words[i-1]]:
            wordDict[words[i-1]][words[i]] = 0
        wordDict[words[i-1]][words[i]] = wordDict[words[i-1]][words[i]] + 1

    return wordDict

def randomFirstWord(wordDict):
    randomIndex = randint(0, len(wordDict))
    return list(wordDict.keys())[randomIndex]

content = getdata()
#print('content:',content)
wordDict = buildWordDict(content)

length = 100
chain = ""
currentWord = randomFirstWord(wordDict)
for i in range(0, length):
    chain += currentWord + " "
    currentWord = retrieveRandomWord(wordDict[currentWord])

print(chain)

from urllib.request import urlopen
from random import randint
from bs4 import BeautifulSoup
import re

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

html = urlopen("http://www.guancha.cn/america/2017_01_21_390488_s.shtml")
bsObj = BeautifulSoup(html, "lxml")
ps = bsObj.find("div", {"id": "cmtdiv3523349"}).find_next_siblings("p");
content = ""
for p in ps:
    content = content + p.get_text()
text = bytes(content, "UTF-8")
text = text.decode("ascii", "ignore")
wordDict = buildWordDict(text)

length = 100
chain = ""
currentWord = randomFirstWord(wordDict)
for i in range(0, length):
    chain += currentWord + " "
    currentWord = retrieveRandomWord(wordDict[currentWord])

print(chain)

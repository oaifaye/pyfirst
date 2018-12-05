# -*- coding: UTF-8 -*-
'''
https://blog.csdn.net/smalltankpy/article/details/53616053
'''

from flask_sqlalchemy import SQLAlchemy  
from flask import Flask, redirect, url_for, request, flash, render_template  
from flask_login import LoginManager, login_user, login_required, logout_user  
from nlp._01_textclassify.tfidfbayesclassify import Predict
  
  
app = Flask(__name__)  
app.debug = True  
  
@app.route('/')  
def index():  
    return render_template('index.html')  
 
@app.route('/a/',methods = ['POST'])
def gettype(): 
    print('获取类型..') 
    q = request.form.get('q')
    print(q)
    stopword_path = "hlt_stop_words.txt"
    train_space_path = 'train_word_bag/tfidfspace.dat'
    predict = Predict()
    predicted1,predicted2 = predict.fastpredict(q,stopword_path,train_space_path)
    return predicted2[0]

@app.route('/jquery')
def jquery():
    return render_template('jquery.min.js')
 
if __name__ == '__main__':
    app.run( host="0.0.0.0",port=int("2333"))

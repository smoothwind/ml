# -*- coding: utf-8 -*-
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import logging
import os
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def my_function():
    path = 'D:/Repos/ml/dataset/sina/fundviews/C00001'
    files = os.listdir(path)
    text = []
    for file in files:
        f = open(path+"/"+file, encoding="utf-8")
        text.append(f.readlines())
        f.close()
    return text


if __name__ == '_ '';_main__':
    txt = my_function()
    print(txt)
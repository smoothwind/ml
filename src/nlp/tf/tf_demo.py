import glob
import random
import jieba

import common.fo as fo
from common import stop_words


""" 高频词提取一般☞Term Frequency策略
其主要干扰项：
  （1）. 标点符号
  （2）. 停用词: 即一些无意义的词，例如：的、是、了
"""



def get_TF(words, topK=10):
    tf_dic = {}
    for w in words:
        tf_dic[w] = tf_dic.get(w, 0) + 1
    return sorted(tf_dic.items(), key= lambda x: x[1], reverse=True)[:topK]

if __name__ == '__main__':
    files = glob.glob(r'..\data\news\C000013\*.txt')
    corpus = [fo.FileUtils.get_content(x) for x in files]
    sample_inx = random.randint(0, len(corpus))
    # split_words = list(jieba.cut(corpus[sample_inx]))
    # 过滤停用词
    split_words = [x for x in jieba.cut(corpus[sample_inx]) \
                   if x not in stop_words('../data/stop_words.utf8')]
    print('样本之一：' + corpus[sample_inx])
    print('样本分词效果：' + '/ '.join(split_words))
    print('样本的topK(10)词' + str(get_TF(split_words)))
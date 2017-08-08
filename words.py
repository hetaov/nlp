#-*- coding:utf-8 -*-
import jieba
import jieba.analyse
import jieba.posseg as pseg
def cut_words(sentence):
    #print sentence
    return " ".join(jieba.cut(sentence)).encode('utf-8')

f = open("docs/wiki.ch.text.jian")
target = open("docs/wiki.zh.text.jian.seg", 'a+')
print 'open files'
line = f.readlines(100000)
while line:
    curr = []
    for oneline in line:
    #print(oneline)
        curr.append(oneline)
        after_cut = map(cut_words, curr)

        target.writelines(after_cut)
        print 'saved 100000 articles'

        line = f.readlines(100000)

f.close()
target.close()

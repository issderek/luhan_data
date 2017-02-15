#coding:utf-8
import re

import jieba
import pandas as pd
import numpy as np
import jieba.analyse
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def generate_qa_from_lyric(file_name):
    contents = pd.read_csv(file_name, header=None, sep=',', error_bad_lines=False)
    #print contents
    q_list = []
    a_list = []
    for i in range(0,len(contents[0])-1):
        q_list.append(contents[0][i])
    for i in range(1,len(contents[0])):
        a_list.append((contents[0][i]))
    return pd.DataFrame({'query':pd.Series(q_list),'answer':pd.Series(a_list)},columns=['query','answer'])




result = generate_qa_from_lyric('lyric1.csv')
for i in range(2,9):
    file_name = "lyric%d.csv"%i
    temp_result = generate_qa_from_lyric(file_name)
    result = result.append(temp_result)
#print len(result)
#result.to_csv('lyric_qa.csv',sep=',')

print pd.read_csv("qa2.csv",header=None,sep='\t')

test_str = "糊鹿娃"
tags = jieba.analyse.extract_tags(test_str,2)
cut = jieba.cut(test_str)
print "-".join(tags)
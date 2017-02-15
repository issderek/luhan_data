#coding:utf-8
import re

import jieba
import pandas as pd
import numpy as np
import jieba.analyse
import sys
reload(sys)
sys.setdefaultencoding('utf8')

contents = pd.read_csv("qa2.csv",header=None,sep='\t')

query_list = contents[0]
print ("ok")
print query_list

kw_list = []
for i in range(0,len(query_list)):
    tags = jieba.analyse.extract_tags(query_list[i], 3)
    str = '|'.join(tags)
    str = str.replace('鹿晗','$you')
    str = str.replace('鹿哥', '$you')
    kw_list.append(str)
contents['kw'] = kw_list

keyword_list = contents['kw']
answer_list = contents[1]

#替换所有的称谓
for i in range(0,len(keyword_list)):
    keyword_list[i] = keyword_list[i].replace("$you","[@you:call_you]")

#拆query的string成list用于后续处理
querys_list = []
for item in keyword_list:
    l = item.split("|")
    querys_list.append([l])

# 乱序排序,把结果放到result
def permutation(result, str, list):
    """
        取一个数组的全排列
        list：为输入列表
        str：传空字符串
        result： 为结果列表
    """
    if len(list) == 1:
        result.append(str + "[w:0-10]" + list[0] + "[w:0-10]")
    else:
        for temp_str in list:
            temp_list = list[:]
            temp_list.remove(temp_str)
            permutation(result, str + "[w:0-10]" + temp_str, temp_list)


#扩展子串
query_expanded_list = []
answer_expanded_list = []
for i in range(0,len(querys_list)):
#for i in range(0, 2):
    ori_query = querys_list[i]
    ori_expanded = ori_query
    concat_result = []
    for each_expanded in ori_expanded:
        permutation(concat_result, "", each_expanded)

    query_expanded_list += concat_result
    for j in range(0,len(concat_result)):
        answer_expanded_list.append(answer_list[i])

result = pd.DataFrame({'query':pd.Series(query_expanded_list),'answer':pd.Series(answer_expanded_list)},columns=['query','answer'])
result.to_csv("kw_qa.csv",sep=",")
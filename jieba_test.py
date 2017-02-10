# encoding=utf-8
import jieba
import re

import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def clean(str):
    unimportant_list = ["《","》"," ","\t","【","】","—","-","/","～","+","』","『"]
    r1 = re.compile('\(.*\)' )
    r2 = re.compile('（.*）' )
    for item in unimportant_list:
        str = str.replace(item,"")
    str = r1.sub('',str)
    str = r2.sub('', str)
    return str

def extend_sentence(l):
    extended_l = []
    for i in range(0,len(l)):
        for j in range(i+1,len(l)+1):
            extended_l.append("".join(l[i:j]))
    return extended_l

def getFinalDict(file_name):
    f_dict = {}
    #获取所有句子,清洗并去重
    contents = pd.read_csv(file_name,header=None, sep=',')[1].map(lambda x:clean(x)).drop_duplicates()
    min_cnt = len(contents)
    cnt = 0
    for item in contents:
        cnt += 1
        print cnt
        #第一次分词list
        l = list(jieba.cut(item))
        #扩展
        e_ls = extend_sentence(l)
        #入词典
        for each_e_l in e_ls:
            if each_e_l in f_dict.keys():
                f_dict[each_e_l]+=1
            else:
                f_dict[each_e_l] = 1

    pd.Series(f_dict).to_csv('f_dict.csv')


    #消除
    for each_key in f_dict.keys():
        #if f_dict[each_key] > min_cnt:
        if True:
            print "+%s+%d" % (each_key,f_dict[each_key])
            if len(list(jieba.cut(each_key))) > 1:
                for item in extend_sentence(each_key):
                    print "\t%s,%d减去%d"%(item,f_dict[item],f_dict[each_key])
                    f_dict[item] -= f_dict[each_key]

    final_result = pd.Series(f_dict)
    print final_result
    final_result[final_result>0].to_csv("cut_test_result.csv")

#getFinalDict("test_all_sing.csv")

test = "白色白色的天空"
print "|".join(list(jieba.cut(test)))
print "|".join(extend_sentence(list(jieba.cut(test))))
e = extend_sentence(list(jieba.cut(test)))
t_dict = {}
for t_item in e:
    if t_item in t_dict.keys():
        t_dict[t_item]+=1
    else:
        t_dict[t_item] = 1

print pd.Series(t_dict)


t_r =  pd.DataFrame({"content":pd.Series(t_dict.keys()),"cnt":pd.Series(t_dict.values())},index=range(0,len(t_dict)))
t_r['content_len']=t_r['content'].apply(lambda x:len(x))
t_d = t_r.set_index('content')['content_len'].to_dict()
the_dict= sorted(t_d.items(), key=lambda d:d[1], reverse = True)

print the_dict
for each_key in the_dict:
    # if f_dict[each_key] > min_cnt:
    if True:
        each_key = each_key[0]
        print "+%s : %d" % (each_key, t_d[each_key])
        if len(list(jieba.cut(each_key))) > 1:
            print each_key
            for item in extend_sentence(list(jieba.cut(each_key))):
                print "\t%s,%d减去%d" % (item, t_d[item], t_d[each_key])
                t_d[item] -= t_d[each_key]
                if t_d[item]==0:
                    del t_d[item]

final_result = pd.Series(dict)
print final_result













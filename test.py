#coding:utf-8
import re
import pandas as pd
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf8')

df = pd.read_csv('luhan.txt', header=None, sep='\t')
contents = df[0]
contents.to_csv('re_result.csv')
p = re.compile(r'^@.*(\?\?|:)')
movie_info = ['长城','摆渡人','盗墓笔记','我是证人','重返20岁']

contents2 = contents.map(lambda x: re.subn(p, '', x)[0])

contents2 = contents2.map(lambda x: x.replace("??",""))
contents2 = contents2.map(lambda x: x.replace(".",""))
contents2 = contents2.map(lambda x: x.replace("…",""))
contents2.dropna()

ori_content = contents2[contents2 != ""]

ori_content = ori_content[ori_content.str.contains("鹿晗")]
#ori_content.to_csv('result.csv')
dance = ori_content[ori_content.str.contains("舞")]
#dance.to_csv('result_dance.csv')
sing = ori_content[ori_content.str.contains("歌")]
#sing.to_csv('result_sing.csv')
handsome = ori_content[ori_content.str.contains("帅")]
like1 = ori_content[ori_content.str.contains("喜欢鹿晗")]
like2 = ori_content[ori_content.str.contains("爱鹿晗")]
#handsome.to_csv('handsome.csv')
star_info = pd.read_csv('star_info.csv',header=None, sep='\t')
song_info = pd.read_csv('song_info.csv',header=None, sep=',')
song_names = song_info[0].values

print "1 OK"

def has_songname(x):
    for item in song_names:
        if item in x:
            return True
    return False

sing2 = ori_content[ori_content.map(lambda x: has_songname(x))]
print "2 OK"
#song2.to_csv('result_sing2.csv')
all_sing = pd.concat([sing2,sing],ignore_index=False).drop_duplicates()
print "3 OK"
#all_sing.to_csv('all_sing.csv')
#other_sing = sing[sing.map(lambda x:x not in sing2.values)]
#other_sing.to_csv('other_sing.csv')

def has_sth(x,sth):
    print "process.."
    for item in sth:
        if item in x:
            return True
    return False


mid_content = pd.concat([dance,handsome,like1,like2,all_sing],ignore_index=False).drop_duplicates()
else_content = ori_content.drop(pd.concat([dance,handsome,like1,like2,all_sing],ignore_index=False).drop_duplicates().index)

print star_info[0].values[0]
all_singer_related = else_content[else_content.map(lambda x: has_sth(x,star_info[0].values))]
all_singer_related.to_csv('all_singer_related.csv')

print "4 OK"

else_content2 = ori_content.drop(pd.concat([mid_content,all_singer_related],ignore_index=False).drop_duplicates().index)
else_content2.to_csv('else_content.csv')







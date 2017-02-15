# encoding=utf-8
import jieba
import re

import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def clean(str):
    unimportant_list = ["《","》"," ","\t","【","】","—","-","/","～","+","』","『",",","\"","!","#",".","。","，"]
    r1 = re.compile('\(.*\)' )
    r2 = re.compile('（.*）' )
    for item in unimportant_list:
        str = str.replace(item,"")
    str = r1.sub('',str)
    str = r2.sub('', str)
    return str


star_info = pd.read_csv('star_info.csv',header=None, sep='\t')
song_info = pd.read_csv('song_info.csv',header=None, sep=',')
song_names = song_info[0].values
for i in range(0,len(song_names)):
    song_names[i] = clean(song_names[i])
star_names = star_info[0].values
movie_names = ['长城', '摆渡人', '盗墓笔记', '我是证人', '重返20岁']

def replaceSth(str):
    for a_song in song_names:
        str = str.replace(a_song,"$songName$")
    for a_star in star_names:
        str = str.replace(a_star,"$starName$")
    for a_movie in movie_names:
        str = str.replace(a_movie,"$movieName$")
    str = clean(str)
    return str


def replace_sth():
    movie_info = ['长城', '摆渡人', '盗墓笔记', '我是证人', '重返20岁']

def extend_sentence(l):
    extended_l = []
    for i in range(0,len(l)):
        for j in range(i+1,len(l)+1):
            extended_l.append("".join(l[i:j]))
    return extended_l

def getFinalDict(file_name):
    final_dict = {}
    #获取所有句子,清洗并去重
    contents = pd.read_csv(file_name,header=None, sep=',')[1].map(lambda x:replaceSth(x)).drop_duplicates()
    min_cnt = len(contents)/100
    cnt = 0
    for item in contents:
        cnt += 1
        print "****** %s ******"%cnt
        #扩展
        l = []
        for item in jieba.cut(item):
            l.append(item)
        e_ls = extend_sentence(l)
        #入词典
        for each_e_l in e_ls:
            if each_e_l in final_dict.keys():
                final_dict[each_e_l]+=1
            else:
                final_dict[each_e_l] = 1
        """
        for each_d in final_dict.keys():
            print "%s : %s"%(each_d,final_dict[each_d])
       """

    #获得完整的f_dict
    #将f_dict中的key按长短排成处理指针
    frame_len_added = pd.DataFrame({"content": pd.Series(final_dict.keys()), "cnt": pd.Series(final_dict.values())},
                       index=range(0, len(final_dict)))
    frame_len_added['content_len'] = frame_len_added['content'].apply(lambda x: len(x))
    sorted_dict = frame_len_added.set_index('content')['content_len'].to_dict()
    sorted_list = sorted(sorted_dict.items(), key=lambda d: d[1], reverse=True)
    the_dict_list = []
    #print "*****************排序后********************"
    for longer_one in sorted_list:
        the_dict_list.append(longer_one[0])
        #print longer_one[0]


    #print "***************************************"
    for each_key in the_dict_list:
        #print "*************each_key: %s***********"%each_key
        #print final_dict[each_key]
        if final_dict[each_key] > min_cnt:
            #print min_cnt
            #print "len: %s; each_key: %s" % (len(list(jieba.cut(each_key))), each_key)
            if len(list(jieba.cut(each_key))) > 1:
                cuted_list = extend_sentence(list(jieba.cut(each_key)))
                #print ",".join(cuted_list)
                for item in cuted_list:
                    if item != each_key:
                        #print "item: %s"%item
                        try:
                            #print "**** %s ****  %s  ***** %s  ***"%(item, final_dict[item], final_dict[each_key])
                            final_dict[item] -= final_dict[each_key]
                        except:
                            pass
                for item in cuted_list:
                    try:
                        if final_dict[item] <= 0:
                            del final_dict[item]
                            the_dict_list.remove(item)
                    except:
                        pass
        else:
            del final_dict[each_key]

    return final_dict


"""
final_result = pd.Series(getFinalDict("all_sing.csv"))
final_result.to_csv("cut_all_sing.csv")
final_result = pd.Series(getFinalDict("handsome.csv"))
final_result.to_csv("cut_handsome.csv")

"""

final_result = pd.Series(getFinalDict("all_singer_related.csv"))
final_result.to_csv("cut_all_singer_related.csv")

final_result = pd.Series(getFinalDict("else_content.csv"))
final_result.to_csv("else_content.csv")









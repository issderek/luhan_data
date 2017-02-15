#coding:utf-8
import pandas as pd
import sys
reload(sys)
sys.setdefaultencoding('utf8')

ori_qa = pd.read_csv("qa3.csv",header=None, sep="\t")
querys = list(ori_qa[0])
answers = list(ori_qa[1])
you_str = "#".join(list(pd.read_csv("you.csv",header=None, sep=",")[0]))

#替换所有的称谓
for i in range(0,len(querys)):
    querys[i] = querys[i].replace("$you","[@you:call_you]")

#拆query的string成list用于后续处理
querys_list = []
for item in querys:
    l = item.split("|")
    querys_list.append([l])



def cut(list):
    r_list = []
    for a_list in list:
        for item in a_list:
            if "#" in item:
                mid_list = item.split("#")
                for each_one in mid_list:
                    l = a_list[:]
                    l.remove(item)
                    l.append(each_one)
                    r_list.append(l)
                break
    return r_list

def is_finish(list):
    for a in list:
        for b in a:
            if "#" in b:
                return False
    return True

# 根据#把内容展开
def expand_list(list):
    while not is_finish(list):
        list = cut(list)
    return list

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
    ori_expanded = expand_list(ori_query)
    concat_result = []
    for each_expanded in ori_expanded:
        permutation(concat_result, "", each_expanded)

    query_expanded_list += concat_result
    for j in range(0,len(concat_result)):
        answer_expanded_list.append(answers[i])


result = pd.DataFrame({'query':pd.Series(query_expanded_list),'answer':pd.Series(answer_expanded_list)},columns=['query','answer'])
result.to_csv("result_qa3.csv",sep=",")
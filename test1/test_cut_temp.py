#coding: utf-8
list = [["a","b1#b2","c","d1#d2"]]
total_list = []

def cut(list):
    r_list = []
    for a_list in list:
        #print a_list
        for item in a_list:
            #print item
            if "#" in item:
                mid_list = item.split("#")
                for each_one in mid_list:
                    l = a_list[:]
                    l.remove(item)
                    l.append(each_one)
                    r_list.append(l)
                break
    return r_list

#print cut(list)

def is_finish(list):
    for a in list:
        for b in a:
            if "#" in b:
                return False
    return True

while not is_finish(list):
    list = cut(list)
print list



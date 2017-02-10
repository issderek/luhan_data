# coding:utf-8
import requests
import json
import sys

import time

reload(sys)
sys.setdefaultencoding('utf8')
import pandas as pd

#歌曲爬取
"""
output = open('song_info.csv', 'w')
for i in range(0,10):
    url = "https://c.y.qq.com/soso/fcgi-bin/search_cp?remoteplace=sizer.yqq.song_next&searchid=153597707068002851&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=%d"%i
    append_url = "&n=20&w=%E9%B9%BF%E6%99%97&g_tk=449421411&jsonpCallback=searchCallbacksong5577&loginUin=53200690&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0"
    url += append_url
    html_content = requests.get(url)
    j = json.loads(html_content.text[23:-1])
    info_list = list(j['data']['song']['list'])
    for item in info_list:
        str = ""
        album_name = item['albumname']
        singers = list(item['singer'])
        songname = item['songname']
        str += "%s\t"%songname
        str += "%s\t"%album_name
        #j_singer = json.loads(singers)
        for each_singer in singers:
            str += "%s\t"%each_singer['name']
        output.write(str)
        output.write('\n')
output.close()
"""

#明星名字爬取
"""
output = open('star_info.csv', 'w')
url = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?resource_id=28226&from_mid=1&&format=json&ie=utf-8&oe=utf-8&query=明星&sort_key=&sort_type=1&stat0=&stat1=&stat2=&stat3=&pn="
for i in range (0,1000):
    print "page: %d"%i
    a = i*12
    new_url = "%s%s"%(url,a)
    print new_url
    html_content = requests.get(new_url)
    try:
        result_list = json.loads(html_content.text)['data'][0]['result']
        for item in result_list:
            name = item['ename']

            try:
                diyu = item['diyu'][0]
            except:
                diyu = "-"

            try:
                gender = item['gender'][0]
            except:
                gender = "-"

            try:
                heightNumeric = item['heightNumeric'][0]
            except:
                heightNumeric = "-"

            try:
                zodiac = item['zodiac'][0]
            except:
                zodiac = "-"

            try:
                zodiacSign = item['zodiacSign'][0]
            except:
                zodiacSign = "-"

            str = "%s\t%s\t%s\t%s\t%s\t%s" % (name, diyu, gender, heightNumeric, zodiac, zodiacSign)
            output.write(str)
            output.write('\n')
    except:
        time.sleep(10)
        pass

output.close()
"""




#out = pd.read_csv("song_info.csv",header = None, sep = ',')
#print(out[1])



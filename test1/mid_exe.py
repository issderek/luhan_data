#coding:utf-8
import re
import pandas as pd
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf8')

result = pd.read_csv('mid.csv', header=None, sep='|')
str = ""
for item in result[0]:
    str += "%s|"%item.strip()
print str
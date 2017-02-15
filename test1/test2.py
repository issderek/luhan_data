#coding:utf-8
import re
import pandas as pd
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf8')
a="你好漂亮"
b="你好"
star_info = pd.read_csv('star_info.csv',header=None, sep=',')
print star_info.ix[0]
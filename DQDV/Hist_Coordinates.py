import unicodedata
from Num_Str.Numerical import *
from Num_Str.Strings_comp import *
from Num_Str.Numerical2 import *
from ListTable import *
from collections import Counter
from decimal import Decimal
from statistics import *
import math
import distance
import sys
import os
import sqlite3
from Database import *
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl


strDB = data()
conn = sqlite3.connect(strDB)
result= conn.execute('select * from mappingapp_sample')
cursor = conn.cursor()

cursor.execute('select * from mappingapp_coordinates')
allAttr = cursor.fetchall()
bng_ing = [attr[1] for attr in allAttr]

bng_diff = Strings_comp(bng_ing).num_diff()
keys = bng_diff.keys()
keyL = []
keyV = []
mytupleL = ()
mytupleV = ()
for key in keys:
    val = bng_diff.get(key)
    keyL.append(key)
    keyV.append(val)
mytupleL = tuple(keyL)
mytupleV = tuple(keyV)

N = 6
menMeans = mytupleV
menStd =(1,2,3,4,5,6)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots(figsize=(10,6))
rects1 = ax.bar(ind, menMeans, width, color='r', yerr=menStd)


# add some text for labels, title and axes ticks
ax.set_ylabel('Num of Diff Values')
ax.set_title('Different Values')
ax.set_xticks(ind+width)
k0 = str(keyL[0])
k1 = str(keyL[1])
k2 = str(keyL[2])
k3 = str(keyL[3])
k4 = str(keyL[4])
k5 = str(keyL[5])
         
ax.set_xticklabels( (k0, k1, k2, k3, k4, k5))

def autolabel(rects):
    # attach some text labels
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x()+rect.get_width(), height, '%d'%int(height),
                ha='center', va='bottom')

autolabel(rects1)

file_path = (os.path.abspath(__file__)).replace('Hist_Coordinates.py', "")
plt.savefig(file_path+"IMGS\\bng_ing_hist.png")
#plt.show()

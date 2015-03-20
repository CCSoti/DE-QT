import matplotlib.pyplot as plt
import math
import sys
import os
import sqlite3
from Num_Str.Numerical import *
from Num_Str.Strings_comp import *
from Num_Str.Numerical2 import *
from collections import Counter
from Database import *
import distance
import numpy as np

strDB = data()
conn = sqlite3.connect(strDB)
result= conn.execute('select * from mappingapp_sample')
cursor = conn.cursor()

cursor.execute('select * from mappingapp_coordinates')
allAttr = cursor.fetchall()
bng_ing = [attr[1] for attr in allAttr]
bng_diff = Strings_comp(bng_ing).num_diff()


points = bng_diff.keys()
vals = bng_diff.values()
x = []
x_labels = []
y = []
for p in range(0,len(points)):
    x.append(p)
for p in points:
    x_labels.append(p)
for v in vals:
    y.append(v)

area = (np.array(y))**2
f, ax = plt.subplots()
ax.scatter(x, y, s=area, c=area, alpha=0.5)
for l in x_labels:
    ind = x_labels.index(l)
    ax.text(x[ind], y[ind], l, va='center',  ha='left')
#ax.set_xticklabels(x_labels)
file_path = (os.path.abspath(__file__)).replace('BubbleChart_Coord.py', "")
plt.savefig(file_path+"IMGS\\bng_ing_bubble.png")
#plt.show()

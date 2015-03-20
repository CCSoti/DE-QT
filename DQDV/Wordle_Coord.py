from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts
import networkx as nx
import matplotlib.pyplot as plt

import os
import sys
import sqlite3
from Num_Str.Numerical import *
from Num_Str.Strings_comp import *
from Num_Str.Numerical2 import *
from collections import Counter
from Database import *
import distance


#strDB = data()
strDB = data()
conn = sqlite3.connect(strDB)
result= conn.execute('select * from mappingapp_sample')
cursor = conn.cursor()

cursor.execute('select * from mappingapp_coordinates')
allAttr = cursor.fetchall()
bng_ing = [attr[1] for attr in allAttr]
bng_str = ""
for i in bng_ing:
    if(i != None):
        bng_str += i + " "


file_path = (os.path.abspath(__file__)).replace('Wordle_Coord.py', "")
tags = make_tags(get_tag_counts(bng_str), maxsize=120)
create_tag_image(tags, file_path+'IMGS\\cloud_large.png', size=(900,700), fontname='Lobster')

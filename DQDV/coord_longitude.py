import unicodedata
from Num_Str.Numerical import *
from Num_Str.Strings_comp import *
from Num_Str.Numerical2 import *
from Num_Str.Num_not_List import *
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


# In[93]:

strDB = data()
conn = sqlite3.connect(strDB)
result= conn.execute('select * from mappingapp_sample')
cursor = conn.cursor()

cursor.execute('select * from mappingapp_coordinates')
allAttr = cursor.fetchall()
ids = [attr[0] for attr in allAttr]
bng_ing = [attr[1] for attr in allAttr]
grid_ref = [attr[2] for attr in allAttr]
easting = [attr[3] for attr in allAttr]
northing = [attr[4] for attr in allAttr]
lat = [attr[5] for attr in allAttr]
longs = [attr[6] for attr in allAttr]
elevation = [attr[7] for attr in allAttr]

titles = ["Id", "Longitude", "Precision"]
row1 = ListTable(titles).thead()
strAll = row1
for i in range(0,len(longs)-1):
    if(longs[i] is not None):
        nlong = Num_not_List(longs[i]).max_prec()
        long_prec = [ids[i], longs[i], nlong]
        row2 = ListTable(long_prec).simple_table()
        strAll += row2

file_path = (os.path.abspath(__file__)).replace('coord_longitude.py', "")
css_path = file_path + "CSS\\simple-style.css"

# Creating the HTML file
message = """<!DOCTYPE html>
<html>
<head>
<title>BRITICE-CHROMO PROJECT</title>
<link rel="stylesheet" href="""+css_path+""">
</head>
<body>
<div class="header">
    <div class="text">BRITICE-CHROMO PROJECT</div>
</div>
<div class="content">
<form>
 <fieldset class="first">
  <legend>Legend (Numerical):</legend>
  <text class="t1">Big Warning</text><br>
  <text class="t2">Small Warning</text><br>
  <text class="t11">Small2 Warning</text><br>
  <text class="t12">Small3 Warning</text><br>
  <text class="t13">Small4 Warning</text><br>
  <text class="t14">Small5 Warning</text><br>
 </fieldset>
</form>

<table class="tableMAXP">
<caption>Specific values analysis</caption>
"""+strAll+"""</table>

</div>
</body>
</html>"""

f = open(file_path+'\\HTMLFiles\\coordinates_longitude.html','w')
f.write(message)
f.close()

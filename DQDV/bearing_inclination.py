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


strDB = data()
conn = sqlite3.connect(strDB)
result= conn.execute('select * from mappingapp_sample')
cursor = conn.cursor()

cursor.execute('select * from mappingapp_bearing_inclination')
allAttr = cursor.fetchall()
bearing = [attr[1] for attr in allAttr]
inclination = [attr[2] for attr in allAttr]

titles = ["Field", "Max Value", "Min Value", "Avg Value", "Max Precission", "Min Precission", "Avg Precission", "Std Deviation"]
bear = Numerical2(bearing)
inclin = Numerical2(inclination)
bears = ["Bearing", bear._max_value_(), bear._min_value_(), bear._mean_(), bear.max_prec_integers(), bear.min_prec_integers(), bear.mean_prec_integers(), bear._strd_dev_()]
inclins = ["Inclination", inclin._max_value_(), inclin._min_value_(), inclin._mean_(), inclin.max_prec_integers(), inclin.min_prec_integers(), inclin.mean_prec_integers(), inclin._strd_dev_()]

row1 = ListTable(titles).thead()
row2 = ListTable(bears).simple_table()
row3 = ListTable(inclins).simple_table()

file_path = (os.path.abspath(__file__)).replace('bearing_inclination.py', "")
css_path = file_path + "CSS\\simple-style.css"

# Creating the HTML file
f = open(file_path+'HTMLFiles\\bearing_inclination.html','w')
strAll = row1+row2+row3

message = """<!DOCTYPE html>
<html>
<head>
<title>BRITICE-CHRONO PROJECT</title>
<link rel="stylesheet" href="""+css_path+""">
</head>
<body>
<div class="header">
    <div class="text">BRITICE-CHRONO PROJECT</div>
</div>
<div class="content">

<form>
 <fieldset class="first">
  <legend>Legend (Numerical):</legend>
  <text class="t1">Max Precision</text><br>
  <text class="t2">Min Precision</text><br>
 </fieldset>
 <fieldset class="second">
  <legend>Legend (Text):</legend>
  <text class="t1">Average Similarity</text><br>
  <text class="t2">Most Similar Pair</text><br>
  <text class="t3">Special Characters</text><br>
 </fieldset>
</form>

<table class="tableBear">
<caption>Numerical analysis</caption>
"""+strAll+"""</table>
</div>
</body>
</html>"""

f.write(message)
f.close()

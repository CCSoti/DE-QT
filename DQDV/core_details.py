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

cursor.execute('select * from mappingapp_core_details')
allAttr = cursor.fetchall()
exposure_core = [attr[1] for attr in allAttr]
core_number = [attr[2] for attr in allAttr]

titlesS = ["Field", "Average Similarity", "Most Similar", "Least Similar", "Most Similar Pair", "Least Similar Pair", "No-Diff.Values", "Longest String", "Shortest String"]
titlesS2 = ["Field", "Most Common Value(Reference value)", "Common Value(%)", "Reference", "Special Characters"]
strs = Strings_comp(exposure_core)
sGrid = Strings_comp(core_number)
bng = ["Exposure Core", strs.jacc_diff_values(), strs.jacc_maxR(), strs.jacc_minR(), strs.jacc_high_pair(), strs.jacc_least_pair(), strs.num_diff_values(), strs.long_str(), strs.short_str()]
grid = ["Core Number", sGrid.jacc_diff_values(), sGrid.jacc_maxR(), sGrid.jacc_minR(), sGrid.jacc_high_pair(), sGrid.jacc_least_pair(), sGrid.num_diff_values(), sGrid.long_str(), sGrid.short_str()]
bng2 = ["Exposure Core", strs.most_com_value(), strs.com_value_perc(), strs.ref_one(), strs.special_char()]
grid2 = ["Core Number", sGrid.most_com_value(), sGrid.com_value_perc(), sGrid.ref_one(), sGrid.special_char()]


row1 = ListTable(titlesS).thead()
row2 = ListTable(bng).simple_table()
row3 = ListTable(grid).simple_table()
row4 = ListTable(titlesS2).thead()
row5 = ListTable(bng2).simple_table()
row6 = ListTable(grid2).simple_table()


file_path = (os.path.abspath(__file__)).replace('core_details.py', "")
css_path = file_path + "CSS\\simple-style.css"

# Creating the HTML file
f = open(file_path+'\\HTMLFiles\\core_details.html','w')
strAll = row1+row2+row3
strAll2 = row4+row5+row6

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

<table class="tableCore">
<caption>Text analysis</caption>
"""+strAll+"""</table>
<table class="tableCore2">
<caption>Text analysis(continue)</caption>
"""+strAll2+"""</table>
</div>
</body>
</html>"""

f.write(message)
f.close()

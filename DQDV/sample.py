import unicodedata
import os
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
import sqlite3
from Database import *
import numpy as np
import matplotlib.pyplot as plt


strDB = data()
conn = sqlite3.connect(strDB)
result= conn.execute('select * from mappingapp_sample')
cursor = conn.cursor()

cursor.execute('select * from mappingapp_sample')
allAttr = cursor.fetchall()
sample_code = [attr[1] for attr in allAttr]
sample_location_name = [attr[2] for attr in allAttr]
collection_date = [attr[3] for attr in allAttr]
collector = [attr[4] for attr in allAttr]
sample_notes = [attr[5] for attr in allAttr]
dating_priority = [attr[6] for attr in allAttr]
age = [attr[7] for attr in allAttr]
age_error = [attr[8] for attr in allAttr]
calendar_age = [attr[9] for attr in allAttr]
calendar_error = [attr[10] for attr in allAttr]
lab_code = [attr[11] for attr in allAttr]

strs = Strings_comp(sample_code)
sGrid = Strings_comp(sample_location_name)
burial = Strings_comp(collection_date)
gamma = Strings_comp(collector)
equip = Strings_comp(sample_notes)

titlesS = ["Field", "Average Similarity", "Most Similar", "Least Similar", "Most Similar Pair", "Least Similar Pair", "No-Diff.Values", "Longest String", "Shortest String"]
titlesS2 = ["Field", "Most Common Value(Reference value)", "Common Value(%)", "Reference", "Special Characters"]
bng = ["Sample Code", strs.jacc_diff_values(), strs.jacc_maxR(), strs.jacc_minR(), strs.jacc_high_pair(), strs.jacc_least_pair(), strs.num_diff_values(), strs.long_str(), strs.short_str()]
grid = ["Sample Location Name", sGrid.jacc_diff_values(), sGrid.jacc_maxR(), sGrid.jacc_minR(), sGrid.jacc_high_pair(), sGrid.jacc_least_pair(), sGrid.num_diff_values(), sGrid.long_str(), sGrid.short_str()]
bur = ["Collection Date", burial.jacc_diff_values(), burial.jacc_maxR(), burial.jacc_minR(), burial.jacc_high_pair(), burial.jacc_least_pair(), burial.num_diff_values(), burial.long_str(), burial.short_str()]
gam = ["Collector", gamma.jacc_diff_values(), gamma.jacc_maxR(), gamma.jacc_minR(), gamma.jacc_high_pair(), gamma.jacc_least_pair(), gamma.num_diff_values(), gamma.long_str(), gamma.short_str()]
# equ = ["Sample Notes", equip.jacc_diff_values(), equip.jacc_maxR(), equip.jacc_minR(), equip.jacc_high_pair(), equip.jacc_least_pair(), equip.num_diff_values(), equip.long_str(), equip.short_str()]

bng2 = ["Sample Code", strs.most_com_value(), strs.com_value_perc(), strs.ref_one(), strs.special_char()]
grid2 = ["Sample Location Name", sGrid.most_com_value(), sGrid.com_value_perc(), sGrid.ref_one(), sGrid.special_char()]
bur2 = ["Collection Date", burial.most_com_value(), burial.com_value_perc(), burial.ref_one(), burial.special_char()]
gam2 = ["Collector", gamma.most_com_value(), gamma.com_value_perc(), gamma.ref_one(), gamma.special_char()]
# equ2 = ["Sample Notes", equip.most_com_value(), equip.com_value_perc(), equip.ref_one(), equip.special_char()]

s_notes = ["Field", "Readability (0-100)"]
equ2 = ["Sample Notes", equip.readability()]

row1 = ListTable(titlesS).thead()
row2 = ListTable(bng).simple_table()
row3 = ListTable(grid).simple_table()
row4 = ListTable(bur).simple_table()
row5 = ListTable(gam).simple_table()
# row6 = ListTable(equ).simple_table()

row12 = ListTable(titlesS2).thead()
row22 = ListTable(bng2).simple_table()
row32 = ListTable(grid2).simple_table()
row42 = ListTable(bur2).simple_table()
row52 = ListTable(gam2).simple_table()
# row62 = ListTable(equ2).simple_table()

tS = ListTable(s_notes).thead()
rowS = ListTable(equ2).simple_table()

strAll = row1+row2+row3+row4+row5 #+row6
strAll2 = row12+row22+row32+row42+row52 #+row62
strAllS = tS + rowS


file_path = (os.path.abspath(__file__)).replace('sample.py', "")
css_path = file_path + "CSS\\simple-style.css"

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

<table class="tableSam1">
<caption>Text analysis</caption>
"""+strAll+"""</table>
<table class="tableSam2">
<caption>Text analysis(continue)</caption>
"""+strAll2+"""</table>
<table class="tableSNotes">
<caption>Text analysis(continue)</caption>
"""+strAllS+"""</table>
</div>
</body>
</html>"""

f = open(file_path+'\\HTMLFiles\\sample.html','w')
f.write(message)
f.close()



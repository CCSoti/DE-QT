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

cursor.execute('select * from mappingapp_tcn_sample')
allAttr = cursor.fetchall()
strat_position = [attr[1] for attr in allAttr]
lithofacies = [attr[2] for attr in allAttr]
burial_depth = [attr[3] for attr in allAttr]
lithology = [attr[4] for attr in allAttr]
gamma_spec = [attr[5] for attr in allAttr]
equip_num = [attr[6] for attr in allAttr]
probe_s = [attr[7] for attr in allAttr]
filename = [attr[8] for attr in allAttr]

titlesS = ["Field", "Average Similarity", "Most Similar", "Least Similar", "Most Similar Pair", "Least Similar Pair", "No-Diff.Values", "Longest String", "Shortest String"]
titlesS2 = ["Field", "Most Common Value(Reference value)", "Common Value(%)", "Reference", "Special Characters"]
strs = Strings_comp(strat_position)
sGrid = Strings_comp(lithofacies)
burial = Strings_comp(burial_depth)
gamma = Strings_comp(lithology)
equip = Strings_comp(gamma_spec)
probe_s = Strings_comp(equip_num)
filen = Strings_comp(probe_s)
s_time = Strings_comp(filename)
bng = ["Quartz Content", strs.jacc_diff_values(), strs.jacc_maxR(), strs.jacc_minR(), strs.jacc_high_pair(), strs.jacc_least_pair(), strs.num_diff_values(), strs.long_str(), strs.short_str()]
grid = ["Sample Setting", sGrid.jacc_diff_values(), sGrid.jacc_maxR(), sGrid.jacc_minR(), sGrid.jacc_high_pair(), sGrid.jacc_least_pair(), sGrid.num_diff_values(), sGrid.long_str(), sGrid.short_str()]
bur = ["Sample Material", burial.jacc_diff_values(), burial.jacc_maxR(), burial.jacc_minR(), burial.jacc_high_pair(), burial.jacc_least_pair(), burial.num_diff_values(), burial.long_str(), burial.short_str()]
gam = ["Boulder Dimensions", gamma.jacc_diff_values(), gamma.jacc_maxR(), gamma.jacc_minR(), gamma.jacc_high_pair(), gamma.jacc_least_pair(), gamma.num_diff_values(), gamma.long_str(), gamma.short_str()]
equ = ["S.Surface Strike Dip", equip.jacc_diff_values(), equip.jacc_maxR(), equip.jacc_minR(), equip.jacc_high_pair(), equip.jacc_least_pair(), equip.num_diff_values(), equip.long_str(), equip.short_str()]
prob = ["Sample Thickness", probe_s.jacc_diff_values(), probe_s.jacc_maxR(), probe_s.jacc_minR(), probe_s.jacc_high_pair(), probe_s.jacc_least_pair(), probe_s.num_diff_values(), probe_s.long_str(), probe_s.short_str()]
fil = ["Grain Size", filen.jacc_diff_values(), filen.jacc_maxR(), filen.jacc_minR(), filen.jacc_high_pair(), filen.jacc_least_pair(), filen.num_diff_values(), filen.long_str(), filen.short_str()]
sTime = ["Lithology", s_time.jacc_diff_values(), s_time.jacc_maxR(), s_time.jacc_minR(), s_time.jacc_high_pair(), s_time.jacc_least_pair(), s_time.num_diff_values(), s_time.long_str(), s_time.short_str()]

bng2 = ["Quartz Content", strs.most_com_value(), strs.com_value_perc(), strs.ref_one(), strs.special_char()]
grid2 = ["Sample Setting", sGrid.most_com_value(), sGrid.com_value_perc(), sGrid.ref_one(), sGrid.special_char()]
bur2 = ["Sample Material", burial.most_com_value(), burial.com_value_perc(), burial.ref_one(), burial.special_char()]
gam2 = ["Boulder Dimensions", gamma.most_com_value(), gamma.com_value_perc(), gamma.ref_one(), gamma.special_char()]
equ2 = ["S.Surface Strike Dip", equip.most_com_value(), equip.com_value_perc(), equip.ref_one(), equip.special_char()]
prob2 = ["Sample Thickness", probe_s.most_com_value(), probe_s.num_diff_values(), probe_s.long_str(), probe_s.short_str()]
fil2 = ["Grain Size", filen.most_com_value(), filen.num_diff_values(), filen.long_str(), filen.short_str()]
sTime2 = ["Lithology", s_time.most_com_value(), s_time.num_diff_values(), s_time.long_str(), s_time.short_str()]

row1 = ListTable(titlesS).thead()
row2 = ListTable(bng).simple_table()
row3 = ListTable(grid).simple_table()
row4 = ListTable(bur).simple_table()
row5 = ListTable(gam).simple_table()
row6 = ListTable(equ).simple_table()
row7 = ListTable(prob).simple_table()
row8 = ListTable(fil).simple_table()
row9 = ListTable(sTime).simple_table()

row12 = ListTable(titlesS2).thead()
row22 = ListTable(bng2).simple_table()
row32 = ListTable(grid2).simple_table()
row42 = ListTable(bur2).simple_table()
row52 = ListTable(gam2).simple_table()
row62 = ListTable(equ2).simple_table()
row72 = ListTable(prob2).simple_table()
row82 = ListTable(fil2).simple_table()
row92 = ListTable(sTime2).simple_table()

strAll = row1+row2+row3+row4+row5+row6+row7+row8+row9
strAll2 = row12+row22+row32+row42+row52+row62+row72+row82+row92


file_path = (os.path.abspath(__file__)).replace('tcn_sample.py', "")
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

<table class="tableTcn1">
<caption>Text analysis</caption>
"""+strAll+"""</table>
<table class="tableTcn2">
<caption>Text analysis(continue)</caption>
"""+strAll2+"""</table>
</div>
</body>
</html>"""

f = open(file_path+'\\HTMLFiles\\tcn_sample.html','w')
f.write(message)
f.close()

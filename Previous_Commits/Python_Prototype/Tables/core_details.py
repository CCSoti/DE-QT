import unicodedata
from Numerical import *
from Strings_comp import *
from Numerical2 import *
from ListTable import *
from collections import Counter
from decimal import Decimal
from statistics import *
import math
import distance
import sys
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

titlesS = ["Field", "No-Diff.Similarity", "Max Similarity", "Highest Pair", "No-Diff.Values", "Most Common Value(Reference value)", "Common Value(%)", "Reference"]
strs = Strings_comp(exposure_core)
sGrid = Strings_comp(core_number)
bng = ["Exposure Core", strs.jacc_diff_values(), strs.jacc_max(), strs.jacc_high_pair(), strs.num_diff_values(), strs.most_com_value(), strs.com_value_perc(), strs.ref_one()]
grid = ["Core Number", sGrid.jacc_diff_values(), sGrid.jacc_max(), sGrid.jacc_high_pair(), sGrid.num_diff_values(), sGrid.most_com_value(), sGrid.com_value_perc(), sGrid.ref_one()]

row1 = ListTable(titlesS).thead()
row2 = ListTable(bng).simple_table()
row3 = ListTable(grid).simple_table()

# Creating the HTML file
f = open('core_details.html','w')
str1 = ''.join(row1)
str2 = ''.join(row2)
str3 = ''.join(row3)
strAll = str1+str2+str3

message = """<html>
<head>
<link rel="stylesheet" href="simple-style.css">
</head>
<body><table>
"""+strAll+"""</table>
</body>
</html>"""

f.write(message)
f.close()

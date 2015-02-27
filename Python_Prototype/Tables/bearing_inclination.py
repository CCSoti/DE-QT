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

cursor.execute('select * from mappingapp_bearing_inclination')
allAttr = cursor.fetchall()
bearing = [attr[1] for attr in allAttr]
inclination = [attr[2] for attr in allAttr]

titles = ["Field", "Max Value", "Min Value", "Avg Value", "Max Precission", "Min Precission", "Avg Precission", "Std Deviation"]
bear = Numerical(bearing)
inclin = Numerical(inclination)
bears = ["Bearing", bear._max_value_(), bear._min_value_(), bear._mean_(), bear._max_precission_(), bear._min_precission_(), round(bear._mean_precission_()), bear._strd_dev_()]
inclins = ["Inclination", inclin._max_value_(), inclin._min_value_(), inclin._mean_(), inclin._max_precission_(), inclin._min_precission_(), round(inclin._mean_precission_()), inclin._strd_dev_()]

row1 = ListTable(titles).thead()
row2 = ListTable(bears).simple_table()
row3 = ListTable(inclins).simple_table()

# Creating the HTML file
f = open('bearing_inclination.html','w')
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

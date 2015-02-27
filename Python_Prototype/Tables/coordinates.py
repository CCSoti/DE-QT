# coding: utf-8
# In[92]:

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


# Numerical Table

titles = ["Field", "Max Value", "Min Value", "Avg Value", "Max Precision", "Min Precision", "Avg Precission", "Std Deviation"]
num = Numerical(lat)
nlong = Numerical(longs)
nEast = Numerical2(easting)
nNorth = Numerical2(northing)
latitude = ["Latitude", num._max_value_(), num._min_value_(), num._mean_(), num._max_precission_(), num._min_precission_(), num._mean_precission_(), num._strd_dev_()]
longitude = ["Longitude", nlong._max_value_(), nlong._min_value_(), nlong._mean_(), nlong._max_precission_(), nlong._min_precission_(), nlong._mean_precission_(), nlong._strd_dev_()]
east = ["Easting", nEast.en_max(), nEast.en_min(), nEast.en_avg(), nEast.max_prec_integers(), nEast.min_prec_integers(), nEast.mean_prec_integers(), nEast.en_strd()]
north = ["Northing", nNorth.en_max(), nNorth.en_min(), nNorth.en_avg(), nNorth.max_prec_integers(), nNorth.min_prec_integers(), nNorth.mean_prec_integers(), nNorth.en_strd()]
row1 = ListTable(titles).thead()
row2 = ListTable(latitude).simple_table()
row3 = ListTable(longitude).simple_table()
row4 = ListTable(east).simple_table()
row5 = ListTable(north).simple_table()

# Strings Table
titlesS = ["Field", "Average Similarity", "Most Similar", "Least Similar", "Most Similar Pair", "Least Similar Pair", "No-Diff.Values", "Longest String", "Shortest String"]
titlesS2 = ["Field", "Most Common Value(Reference value)", "Common Value(%)", "Reference", "Special Characters"]
strs = Strings_comp(bng_ing)
sGrid = Strings_comp(grid_ref)
sElev = Strings_comp(elevation)
bng = ["Bng Ing", strs.jacc_diff_values(), strs.jacc_maxR(), strs.jacc_minR(), strs.jacc_high_pair(), strs.jacc_least_pair(), strs.num_diff_values(), strs.long_str(), strs.short_str()]
grid = ["Grid Reference", sGrid.jacc_diff_values(), sGrid.jacc_maxR(), sGrid.jacc_minR(), sGrid.jacc_high_pair(), sGrid.jacc_least_pair(), sGrid.num_diff_values(), sGrid.long_str(), sGrid.short_str()]
elev = ["Elevation", sElev.jacc_diff_values(), sElev.jacc_maxR(), sElev.jacc_minR(), sElev.jacc_high_pair(), sElev.jacc_least_pair(), sElev.num_diff_values(), sElev.long_str(), sElev.short_str()]
bng2 = ["Bng Ing", strs.most_com_value(), strs.com_value_perc(), strs.ref_one(), strs.special_char()]
grid2 = ["Grid Reference", sGrid.most_com_value(), sGrid.com_value_perc(), sGrid.ref_one(), sGrid.special_char()]
elev2 = ["Elevation", sElev.most_com_value(), sElev.com_value_perc(), sElev.ref_one(), sElev.special_char()]


row6 = ListTable(titlesS).thead()
row7 = ListTable(bng).simple_table()
row8 = ListTable(grid).simple_table()
row9 = ListTable(elev).simple_table()
row10 = ListTable(titlesS2).thead()
row11 = ListTable(bng2).simple_table()
row12 = ListTable(grid2).simple_table()
row13 = ListTable(elev2).simple_table()


# Creating the HTML file
f = open('coordinates.html','w')

strAll = row1+row2+row3+row4+row5
strAllS = row6+row7+row8+row9
strAllS2 = row10+row11+row12+row13
message = """<!DOCTYPE html>
<html>
<head>
<title>BRITICE-CHROMO PROJECT</title>
<link rel="stylesheet" href="simple-style.css">
</head>
<body>
<div class="header">
    <div class="text">BRITICE-CHROMO PROJECT</div>
</div>
<div class="content">

<form>
 <fieldset>
  <legend>Legend:</legend>
  <text class="t1">Important</text><br>
  <text class="t2">Critical</text><br>
  <text class="t3">Check</text><br>
 </fieldset>
</form>

<table class="table">
<caption>Numerical analysis</caption>
"""+strAll+"""</table>
<table class="tableS1">
<caption>String analysis</caption>
"""+strAllS+"""</table>
<table class="tableS2">
<caption>String analysis(continue)</caption>
"""+strAllS2+"""</table>
<p>Bar-charts visualisations</p>
<figure>
<img src="IMGS/figure_1.png" alt="Figure_1">
<figcaption>Figure 1</figcaption>
</figure>
</div>
</body>
</html>"""


f.write(message)
f.close()


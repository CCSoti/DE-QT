from collections import Counter
from decimal import Decimal
from statistics import *
import math
import distance
import sys
import sqlite3

# In[90]:

class Num_not_List2(int):

    def clear_int(self):
        int1 = 0
        if(self is not None):                               
              int1 = self                    
        return int1

    def prec(self): 
        int1 = Num_not_List2(self).clear_int()
        dec = len(str(int1))
        return dec

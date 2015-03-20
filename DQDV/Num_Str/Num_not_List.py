from collections import Counter
from decimal import Decimal
from statistics import *
import math
import distance
import sys
import sqlite3

class Num_not_List(float):

    def clear_int(self):
        int1 = 0
        if(self is not None):                               
            if(self<500):
                int1 = self                    
        return int1
    
    def max_prec(self): 
        int1 = Num_not_List(self).clear_int()
        dec = abs(Decimal(str(int1)).as_tuple().exponent)
        return dec
    


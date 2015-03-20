from collections import Counter
from decimal import Decimal
from statistics import *
import math
import distance
import sys
import sqlite3

class Numerical(list):
    
    def clear_data(self):
        small_list = []
        for l in self:
            if(l is not None):                               
                if(l<500):
                  small_list.append(l)                    
        return small_list
    
    def _max_precission_(self): 
        decimals = []  
        small_list = Numerical(self).clear_data()
        for k in small_list:
            dec = abs(Decimal(str(k)).as_tuple().exponent)
            decimals.append(dec)
        return max(decimals)
    
    def _min_precission_(self): 
        decimals = []  
        small_list = Numerical(self).clear_data()
        for k in small_list:
            dec = abs(Decimal(str(k)).as_tuple().exponent)
            decimals.append(dec)
        return min(decimals)
    
    def _mean_precission_(self): 
        decimals = []  
        small_list = Numerical(self).clear_data()
        for k in small_list:
            dec = abs(Decimal(str(k)).as_tuple().exponent)
            decimals.append(dec)
        return round(mean(decimals))
        
    def _min_value_(self):
        small_list = Numerical(self).clear_data()
        min_value = min(small_list)
        return round(min_value)
        
    def _max_value_(self):
        small_list = Numerical(self).clear_data()
        return round(max(small_list))
        
    def _strd_dev_(self):
        small_list = Numerical(self).clear_data()
        return round(pstdev(small_list))
        
    def _mean_(self):
        small_list = Numerical(self).clear_data()
        return round(mean(small_list))


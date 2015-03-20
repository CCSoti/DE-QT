from collections import Counter
from decimal import Decimal
from statistics import *
import math
import distance
import sys
import sqlite3

# In[90]:

class Numerical2(list):
    
    def clear_data(self):
        small_list = []
        for l in self:
            if(l is not None):                      
                small_list.append(l)                    
        return small_list
    
    def _max_precission_(self): 
        decimals = []  
        small_list = Numerical2(self).clear_data()
        for k in small_list:
            dec = abs(Decimal(str(k)).as_tuple().exponent)
            decimals.append(dec)
        return max(decimals)
    
    def _min_precission_(self): 
        decimals = []  
        small_list = Numerical2(self).clear_data()
        for k in small_list:
            dec = abs(Decimal(str(k)).as_tuple().exponent)
            decimals.append(dec)
        return min(decimals)
    
    def _mean_precission_(self): 
        decimals = []  
        small_list = Numerical2(self).clear_data()
        for k in small_list:
            dec = abs(Decimal(str(k)).as_tuple().exponent)
            decimals.append(dec)
        return round(mean(decimals))
        
    def _min_value_(self):
        small_list = Numerical2(self).clear_data()
        return round(min(small_list))
        
    def _max_value_(self):
        small_list = Numerical2(self).clear_data()
        return round(max(small_list))
        
    def _strd_dev_(self):
        small_list = Numerical2(self).clear_data()
        return round(pstdev(small_list))
        
    def _mean_(self):
        small_list = Numerical2(self).clear_data()
        return round(mean(small_list))

    def max_prec_integers(self):
        small_list = Numerical2(self).clear_data()
        addit = []
        for k in small_list:
            lenK = len(str(k))
            addit.append(lenK)
        return max(addit)
    
    def min_prec_integers(self):
        small_list = Numerical2(self).clear_data()
        addit = []
        for k in small_list:
            lenK = len(str(k))
            addit.append(lenK)
        return min(addit)

    def mean_prec_integers(self):
        small_list = Numerical2(self).clear_data()
        addit = []
        for k in small_list:
            lenK = len(str(k))
            addit.append(lenK)
        return round(mean(addit))

    # min value of easting and northing values
    def en_min(self):
        small_list = Numerical2(self).clear_data()
        k = small_list[0]
        strK = str(k)
        first3 = strK[:2]
        intK = int(first3)
        minV = intK
        minInt = k
        for j in small_list:
            strJ = str(j)
            fir3 = strJ[:3]
            intJ = int(fir3)
            if(intK>intJ):
                minV = intJ
                minInt = j
        return minInt

    # max value of easting and northing values
    def en_max(self):
        small_list = Numerical2(self).clear_data()
        k = small_list[0]
        strK = str(k)
        first3 = strK[:3]
        intK = int(first3)
        maxV = intK
        maxInt = k
        for j in small_list:
            strJ = str(j)
            fir3 = strJ[:3]
            intJ = int(fir3)
            if(intK<intJ):
                maxV = intJ
                maxInt = j
        return maxInt

    # avg value of easting and northing values
    def en_avg(self):
        small_list = Numerical2(self).clear_data()
        min_V = Numerical2(self).en_min()
        max_V = Numerical2(self).en_max()
        intMin = int(str(min_V)[:3])
        intMax = int(str(max_V)[:3])
        intMin2 = int(str(min_V)[3:])
        intMax2 = int(str(max_V)[3:])
        avg_V = (round((intMin + intMax)/2))*1000 + (round((intMin2 + intMax2)/2))
        return avg_V

    # standard deviation of eating and northing
    def en_strd(self):
        small_list = Numerical2(self).clear_data()
        intL = []
        for j in small_list:
            strJ = str(j)
            fir3 = strJ[:3]
            intJ = int(fir3)*1000
            intL.append(intJ)
        return round(pstdev(intL))

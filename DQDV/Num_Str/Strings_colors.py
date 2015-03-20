from collections import Counter
from decimal import Decimal
from statistics import *
import math
import distance
import sys
import sqlite3


class Strings_colors(str):
    
    def clear_data(self):
        str1 = ""
        if(self is not None):  
            if(self!=""):
                str1 = self                   
        return str1

    

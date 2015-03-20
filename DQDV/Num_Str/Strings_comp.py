from collections import Counter
from decimal import Decimal
from TextStats.textstat import *
from statistics import *
import math
import distance
import sys
import sqlite3


class Strings_comp(list):
    
    def clear_data(self):
        small_list = []
        for l in self:
            if(l is not None):  
                if(l!=""):
                    small_list.append(l)                    
        return small_list
    
    def leven(self):
        all_dis = []
        small_list = Strings_comp(self).clear_data()
        for i in range(0, len(small_list)-1):
            cursor = small_list[i]
            for j in range(i+1, len(small_list)-1):
                dis = distance.levenshtein(cursor, small_list[j])
                all_dis.append(dis)
        return all_dis
    
#     normalized --> jaccard
    def jacc(self):
        all_dis = []
        small_list = Strings_comp(self).clear_data()
        for i in range(0, len(small_list)-1):
            cursor = small_list[i]          
            for j in range(i+1, len(small_list)-1):             
                dis = distance.jaccard(cursor, small_list[j])
                all_dis.append(dis)
        
        dict_v = Counter(all_dis).values()        
        return all_dis
    
    def jacc_diff_values(self):
        all_dis = Strings_comp(self).jacc()
        meanV = mean(all_dis)
        return round(meanV, 3)
    
        
    def jacc_max(self):
        all_dis = []
        small_list = Strings_comp(self).clear_data()
        for i in range(0, len(small_list)-1):
            cursor = small_list[i]          
            for j in range(i+1, len(small_list)-1):             
                dis = distance.jaccard(cursor, small_list[j])   
                if (dis!=0.0):
                    all_dis.append(dis)
        return min(all_dis)

    def jacc_maxR(self):
        all_dis = []
        small_list = Strings_comp(self).clear_data()
        for i in range(0, len(small_list)-1):
            cursor = small_list[i]          
            for j in range(i+1, len(small_list)-1):             
                dis = distance.jaccard(cursor, small_list[j])   
                if (dis!=0.0):
                    all_dis.append(dis)
        return round(min(all_dis), 3)

    def jacc_min(self):
        all_dis = []
        small_list = Strings_comp(self).clear_data()
        for i in range(0, len(small_list)-1):
            cursor = small_list[i]          
            for j in range(i+1, len(small_list)-1):             
                dis = distance.jaccard(cursor, small_list[j])   
                if (dis!=1.0):
                    all_dis.append(dis)
        return max(all_dis)
    
    def jacc_minR(self):
        all_dis = []
        small_list = Strings_comp(self).clear_data()
        for i in range(0, len(small_list)-1):
            cursor = small_list[i]          
            for j in range(i+1, len(small_list)-1):             
                dis = distance.jaccard(cursor, small_list[j])   
                if (dis!=1.0):
                    all_dis.append(dis)
        return round(max(all_dis), 3)
    
    def jacc_high_pair(self):
        all_dis = []
        pair = []
        max_jacc = Strings_comp(self).jacc_max()
        small_list = Strings_comp(self).clear_data()
        for i in range(0, len(small_list)-1):
            cursor = small_list[i]          
            for j in range(i+1, len(small_list)-1):             
                dis = distance.jaccard(cursor, small_list[j])
                if (dis == max_jacc):
                    pair.append(cursor)
                    pair.append(small_list[j])
                if (dis!=0.0):
                    all_dis.append(dis)
        return str(pair[:2]).strip('[]').replace("'", "")

    def jacc_least_pair(self):
        all_dis = []
        pair = []
        min_jacc = Strings_comp(self).jacc_max()
        small_list = Strings_comp(self).clear_data()
        for i in range(0, len(small_list)-1):
            cursor = small_list[i]          
            for j in range(i+1, len(small_list)-1):             
                dis = distance.jaccard(cursor, small_list[j])
                if (dis == min_jacc):
                    pair.append(cursor)
                    pair.append(small_list[j])
                if (dis!=1.0):
                    all_dis.append(dis)
        return str(pair[:2]).strip('[]').replace("'", "")
    
        
    def num_diff_values(self):
        all_diff = []
        small_list = Strings_comp(self).clear_data()
        dict_v = Counter(small_list).values()
        return len(dict_v)

    #method for the histogram
    def num_diff(self):
        all_diff = []
        small_list = Strings_comp(self).clear_data()
        dict_v = Counter(small_list)
        return dict_v
    
    def most_com_value(self):
        small_list = Strings_comp(self).clear_data()
        dict_v = Counter(small_list).values()
        return str(Counter(small_list).most_common(1)).strip('[]').strip('()').replace("'", "")

    # the ref value NOT as a string
    def ref_value(self):
        small_list = Strings_comp(self).clear_data()
        dict_v = Counter(small_list).values()
        return Counter(small_list).most_common(1)
    
    def com_value_perc(self):
        small_list = Strings_comp(self).clear_data()
        com_value = max(Counter(small_list).values())
        all_values = len(small_list)
        percentage = (com_value/all_values)*100
        return round(percentage)
    
    # the values that are most referenced to the most common value
    def ref_one(self):
        small_list = Strings_comp(self).clear_data()
        ref_value = Strings_comp(self).ref_value()
        ref_list = sorted(distance.ifast_comp(ref_value[0][0], small_list))
        first3 = []       
        for k in ref_list:
            if(k[0]!=0):
                first3.append(k)               
        return str(first3[:3]).strip('[]').replace("'", "").replace("(", "").replace(")", "")

    # special character in strings
    def special_char(self):
        small_list = Strings_comp(self).clear_data()
        strAll = ""
        chars = []
        for k in small_list:
            strAll += k
        for j in strAll:
            chars.append(j)
        dict_c = Counter(chars)
        return str(dict_c.keys()).strip('[]').replace("'", "").replace("dict_keys([", "").replace("])", "")
    
    # the longest string
    def long_str(self):
        small_list = Strings_comp(self).clear_data()
        strAll = ""
        lons = small_list[0]
        lenS = len(small_list[0])
        for k in small_list:
            lenK = len(k)
            if(lenK>lenS):
                lons = k
                lenS = lenK        
        return (lons, lenS)

    # the shortest string
    def short_str(self):
        small_list = Strings_comp(self).clear_data()
        strAll = ""
        lons = small_list[0]
        lenS = len(small_list[0])
        for k in small_list:
            lenK = len(k)
            if(lenK<lenS):
                lons = k
                lenS = lenK        
        return lons.replace("'", ""), lenS
    
    # the readability of a text
    def readability(self):
        small_list = Strings_comp(self).clear_data()
        values = []
        for i in small_list:            
            if(textstat.sentence_count(i)!=0):
                scale = textstat.flesch_reading_ease(i)
                values.append(scale)
        rou = round(mean(values))
        sca = ""
        if(rou<=29):
            sca = "Very Confusing"
        elif(rou<=49 and rou>=30):
            sca = "Difficult"
        elif(rou<=59 and rou>=50):
            sca = "Fairly Difficult"
        elif(rou<=69 and rou>=60):
            sca = "Standard"
        elif(rou<=79 and rou>=70):
            sca = "Fairly Easy"
        elif(rou<=89 and rou>=80):
            sca = "Easy"
        else:
            sca = "Very Easy"
        
        return str(rou)+ " " + sca

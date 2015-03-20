import unicodedata
from collections import Counter
from decimal import Decimal
from statistics import *
import math
import distance
import sys
import sqlite3

class ListTable(list):

    def _repr_html_(self):
        html = ["<table>\n"]
        for row in self:
            html.append("<tr>\n")
            
            for col in row:
                html.append("<td>{0}</td>\n".format(col))
            
            html.append("</tr>\n")
        html.append("</table>\n")
        return ''.join(html)

    def simple_table(self):
        html = ["<tr>\n"]
        warning = 7
        normal = 6
        small_warning = 3
        s2_warn = 4
        s3_warn = 2
        s4_warn = 1
        s5_warn = 5
        colclass = ""

        
        for col in self:
            col_index = self.index(col)
            if(col_index==2):
                if (col == warning):
                    colclass = "colwarning"
                elif(col == normal):
                    colclass = "colnormal"
                elif(col == small_warning):
                    colclass = "colsmall"
                elif(col == s2_warn):
                    colclass = "cols2"
                elif(col == s3_warn):
                    colclass = "cols3"
                elif(col == s4_warn):
                    colclass = "cols4"
                elif(col == s5_warn):
                    colclass = "cols5"
                    
            # for "table"
            if(col_index==4 or col_index==5):
                if (col == warning):
                    colclass = "t_warning"
                elif(col == normal):
                    colclass = "t_normal"
                elif(col == small_warning):
                    colclass = "t_small"
                
            html.append('<td class="{0}">{1}</td>\n'.format(colclass,col))
            colclass = ""
            #html.append("<td>{0}</td>\n".format(col))
            
        html.append("</tr>\n")
        return ''.join(html)
    
    def thead(self):
        html = ["<tr>\n"]
            
        for col in self:
            html.append("<th>{0}</th>\n".format(col))
            
        html.append("</tr>\n")
        return ''.join(html)


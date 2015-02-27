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
            
        for col in self:
            html.append("<td>{0}</td>\n".format(col))
            
        html.append("</tr>\n")
        return ''.join(html)
    
    def thead(self):
        html = ["<tr>\n"]
            
        for col in self:
            html.append("<th>{0}</th>\n".format(col))
            
        html.append("</tr>\n")
        return ''.join(html)

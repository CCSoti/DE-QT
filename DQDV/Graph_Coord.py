import networkx as nx
import matplotlib.pyplot as plt

import os
import sys
import sqlite3
from Num_Str.Numerical import *
from Num_Str.Strings_comp import *
from Num_Str.Numerical2 import *
from collections import Counter
from Database import *
import distance

strDB = data()
conn = sqlite3.connect(strDB)
result= conn.execute('select * from mappingapp_sample')
cursor = conn.cursor()

cursor.execute('select * from mappingapp_coordinates')
allAttr = cursor.fetchall()
bng_ing = [attr[1] for attr in allAttr]
bng_diff = Strings_comp(bng_ing).num_diff()
keys = bng_diff.keys()
keyL =[]
labels = {}
for key in keys:
    keyL.append(key)
for k in range(0,len(keyL)):
    labels[k] = keyL[k]

# creating the graph
G=nx.DiGraph()
nodelist = []
for key in keyL:
    nodelist.append(keyL.index(key))

G.add_nodes_from(nodelist)

# Fruchterman-Reingold algorithm

pos = nx.spring_layout(G, k=0.5)

#plt.clf()
fig = plt.figure()
ax = fig.add_subplot(111, axisbg='w',title="BNG_ING Force-Directed Graph", frame_on=False)
#nodes
nx.draw_networkx_nodes(G,pos,nodelist,node_color='b',node_size=500,alpha=0.3)
#nx.draw_networkx_nodes(G,pos,nodelist=[3,4,5],node_color='b',node_size=500,alpha=0.8)

#edges
edgelist = []
edge_labels = []
for i in range(0,len(keyL)):
    for j in range(i,len(keyL)):
        if(i!=j):
            edgelist.append((i,j))
            wei = distance.levenshtein(keyL[i], keyL[j])
            edge_labels.append(wei)
            G.add_edge(i,j,weight=wei)
            G[i][j]['weight'] = wei

#nx.draw_networkx_edges(G,pos, edgelist=[(0,1),(1,2),(2,0)],width=8,alpha=0.5,edge_color='r')
nx.draw_networkx_edges(G,pos, edgelist,width=5,alpha=0.3)

#labels
nx.draw_networkx_labels(G, pos, labels, ax=ax, font_size=12, alpha=0.3)

#edge labels
edge_weight=dict([((u,v,),int(d['weight'])) for u,v,d in G.edges(data=True)])
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weight,ax=ax, font_size=10, label_pos=0.3)

ax.axis('off')

file_path = (os.path.abspath(__file__)).replace('Graph_Coord.py', "")
plt.savefig(file_path+"IMGS\\labels_and_colors.png") # save as png

#plt.show() # display


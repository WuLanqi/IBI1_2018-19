#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:05:30 2019

@author: lanqi
"""

#give me a DNA string
s=input('Give me a DNA string : ')
#e.g. s = "ATGCTTCAGAAAGGTCTTACG"
#count the frequency table of the four nucleotides
s = list(s)
myDict= {}
for word in s:
    if word in myDict:
        myDict[word] += 1
    else:
        myDict[word] = 1        
print (myDict)
#construct a pie from the data
import matplotlib.pyplot as plt
labels = 'A', 'T', 'G', 'C'
sizes = [6,6,5,4]
explode = (0,0,0,0)
color= ['pink','lightsteelblue','ivory','orange']
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=False, startangle=90,colors=color)
## Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis =('equal') 
plt.show()
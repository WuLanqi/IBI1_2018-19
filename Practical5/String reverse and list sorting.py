#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:10:24 2019

@author: lanqi
"""

#a string of words
s = "but soft what light in yonder window breaks"
L = s.split(' ')
print(L)
for i in range (0,len(L)):
    l=list(L[i])
    l.reverse()
    j=''.join(l)
    L[i]=j
L=sorted(L, reverse=True)
print(L)
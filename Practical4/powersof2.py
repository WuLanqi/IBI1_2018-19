#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:10:03 2019

@author: lanqi
"""

x=2019
b=str(x)+' is '
a="2**"
while x!=0:
    for i in range(0,14):
        if 2**i > x:
            break
    i=i-1
    x=x - 2**i  
    if x!=0:
       b=b+a+str(i)+'+'
    else:
        b=b+a+str(i)
print(b)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 15:10:03 2019

@author: lanqi
"""
#give a number
x=2019
b=str(x)+' is '
a="2**"
#computes the powers of 2 that make up x
while x!=0:
#find the biggest i that satisfies 2**i<x
    for i in range(0,14):
        if 2**i > x:
            break
#the loop will plus 1 when output the i, so we should minus 1
    i=i-1
    x=x - 2**i  
    if x!=0:
       b=b+a+str(i)+'+'
    else:
#prevent the additional "+"
        b=b+a+str(i)
print(b)
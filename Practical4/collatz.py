#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:50:33 2019

@author: lanqi
"""

#a positive integer n
#ends when you reach 1 for the first time
n=23
while 1==1:
    if n%2 == 0:
       n=n/2
       print(n)
    elif n%2 == 1:
         n=n*3 + 1
         print(n) 
    if n==1:
     break
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:50:33 2019

@author: lanqi
"""

#a positive integer n
n=23
while 1==1:
#if n is even, dividing by 2
    if n%2 == 0: 
       n=n/2
       print(n)
#if n is odd, multiplying by 3 and adding 1
    elif n%2 == 1: 
         n=n*3 + 1
         print(n)
#ends when you reach 1 for the first time
    if n==1: 
     break
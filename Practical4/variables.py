#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 09:27:27 2019

@author: lanqi
"""
#variables
a = 909
b = 909909
if b%7==0:
    print('b can be divided by 7')
else:
    print('b cannot be divided by 7')
c = b/7
d = c/11
e = d/13
if a>e:
    print('a>e')
if a<e:
    print('a<e')
if a==e:
    print('a=e')

#booleans
x = True
y = False
z = (x and not y)or(y and not x)
print(z)
w = x!=y
print(w)
if z==w:
    print('z is the same as w')
else:
    print('z is not the same as w')
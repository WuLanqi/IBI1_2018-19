#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 10:23:20 2019

@author: lanqi
"""

import re
from fractions import Fraction
#intergers from 1 to 23    (1-9)    (10-19)    (20-23)
re_numtest=re.compile(r'(^[1-9]$)|(^1[0-9]$)|(^2[0-3]$)')
#i is used to control the loop
i = 1
#i.e. while i!=0
while i:
    i=0
    data=input("Please input numbers to computer 24:(use ',' to divide them)\n")
    #put the input number into a list
    numlist=data.split(',')
    #test the input number
    for char in numlist:
        if re_numtest.match(char):
            continue
        else:
            print('The input number must be intergers from 1 to 23')
            i=1
            break        
#transfer each element in list from string to integer
num=list(map(int,numlist))

'''
n is the length of the num
if n==2:
    merging them all available operands
    if result is 24:
        print
if n!=2:
    pick two numbers from the list and merge them all available operands
    delete the two picked numbers and put the result back to the list
    repeat picking two numbers from the new list and merging them all available operands
    repeat deleting the two picked numbers and put the result back to the list
    repeat until there is only one value left
'''
#recursion times
count=0
#way to get 24
solution=0

#n is len(num)
def dfs(n):
    global count
    global solution
    count = count +1
    
    if n==1:
        if(float(num[0])==24):
            solution = solution +1
            return 1
        else:
            return 0
    #select two different numbers
    for i in range(0,n):
        for j in range(i+1,n):
            #selecte the first two numbers
            a=num[i]
            b=num[j]
            #
            num[j]=num[n-1]
            
            num[i]=a+b
            if(dfs(n-1)):
                return 1
            
            if b > a:
                num[i]=b-a
                if(dfs(n-1)):
                    return 1
            if b < a:
                num[i]=a-b
                if(dfs(n-1)):
                    return 1
            
            num[i]=a*b
            if(dfs(n-1)):
                return 1
            #floats are not as precise as fraction
            if a:
                num[i]=Fraction(b,a)
                if(dfs(n-1)):
                    return 1
            if b:
                num[i]=Fraction(a,b)
                if(dfs(n-1)):
                    return 1
            #change back the number lsit
            num[i]=a
            num[j]=b
    return 0

if(dfs(len(num))):
    print('Yes')
else:
    print('No')
print('Recursion times:',count,',Solution:',solution)
    
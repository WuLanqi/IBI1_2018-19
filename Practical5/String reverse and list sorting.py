#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 10:10:24 2019

@author: lanqi
"""

#a string of words
s = input('Give me a string of words : ')
#e.g. s = "but soft what light in yonder window breaks"
#turn the string into list
L = s.split(' ')
###below is the way which I figured out since I knew [::-1]
l=[]
for i in range (0,len(L)):
    l.append(L[i][::-1])
l.sort(reverse=True)
print(l)
###below is the way which I figured out during practical by myself
#s = "but soft what light in yonder window breaks"
#L = s.split(' ')
#for i in range (0,len(L)):
#    l=list(L[i])
#    l.reverse()
#    j=''.join(l)
#    L[i]=j
#L=sorted(L, reverse=True)
#print(L)
###below is the way which is provided by teacher
#s = "but soft what light in yonder window breaks"
#words = s.split(' ')
#reverseWords = []
#for iWord in words:
#    reverseWords.append(iWord[::-1])
#reverseWords.sort(reverse=True)
#print(reverseWords)
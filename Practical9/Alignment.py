#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 10:07:20 2019

@author: lanqi
"""

import pandas as pd
data = pd.read_csv('/Users/lanqi/Desktop/IBI1_2018-19/Practical9/BLOSUM62.txt', sep=' +', engine='python')
BLOSUM = data.to_dict()
print(BLOSUM['A']['R'])
#users enter the file path of tested sequence
seq1p =input('Enter the file path of sequence1 : ')
#e.g. /Users/lanqi/Desktop/IBI1_2018-19/Practical9/human.txt
seq2p =input('Enter the file path of sequence2 : ')
#e.g. /Users/lanqi/Desktop/IBI1_2018-19/Practical9/mouse.txt
seq1 = open(seq1p)
seq1 = list(seq1.read())
seq2 = open(seq2p)
seq2 = list(seq2.read())

#set initial score as zero 
score = 0 
similarity=[]
#compare each amino acid
for i in range(len(seq1)):
    if seq1[i]==seq2[i]:
        similarity.append(seq1[i])
    if seq1[i]!= seq2[i]:
        if BLOSUM[seq1[i]][seq2[i]] >= 0:
            similarity.append('+')
        else:
            similarity.append('_')
    score= score+ BLOSUM[seq1[i]][seq2[i]]

seq1=''.join(seq1)
seq2=''.join(seq2)
similarity = ''.join(similarity)
count=0
for word in similarity:
    if word !='+' and word != '_':
        count=count +1

print('*******************sequence comparison*******************')
print('score: ',score,'    ','percentage:','{:.2%}'.format(count/len(similarity)))
print(seq1,'\n',similarity,'\n',seq2,sep='')


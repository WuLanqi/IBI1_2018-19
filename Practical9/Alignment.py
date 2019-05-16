#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 10:07:20 2019

@author: lanqi
"""

import pandas as pd
data = pd.read_csv('/Users/lanqi/Desktop/IBI1_2018-19/Practical9/BLOSUM62.txt', sep=' +', engine='python')
BLOSUM = data.to_dict()

#users enter the file path of tested sequence
seq1p =input('Enter the file path of sequence1 : ')
#e.g. /Users/lanqi/Desktop/IBI1_2018-19/Practical9/human.txt
seq2p =input('Enter the file path of sequence2 : ')
#e.g. /Users/lanqi/Desktop/IBI1_2018-19/Practical9/mouse.txt
seq1 = open(seq1p)
seq1 = list(seq1.read())
seq2 = open(seq2p)
seq2 = list(seq2.read())

#compare the length of the sequence
#following comparison is based on shorter length
if len(seq1) >= len(seq2):
    length = len (seq2)
else:
    length = len (seq1)

#set initial score as zero 
score = 0 
#the list of alignment
similarity=[]
#loop each amino acid
for i in range(length):
    #if they are the same, save the letter
    if seq1[i]==seq2[i]:
        similarity.append(seq1[i])
    if seq1[i]!= seq2[i]:
        #if the score is >= 0, use "+" to represent 
        if BLOSUM[seq1[i]][seq2[i]] >= 0:
            similarity.append('+')
        #if the score is < 0, use "_" to represent
        else:
            similarity.append('_')
    #compute the score according to BLOSUM
    score= score+ BLOSUM[seq1[i]][seq2[i]]

#trun the list into a single string
seq1=''.join(seq1)
seq2=''.join(seq2)
similarity = ''.join(similarity)

#compute the similarity percentage
count=0
for word in similarity:
    #i.e. they are the same
    if word !='+' and word != '_':
        count=count +1

# BLOSUM score is additionally normalised to sequence length
# because the length of the sequence can influence the BLOSUM score
# shorter length alwaya tends to have higher score
ns = score/length

print('*****************************sequence comparison*****************************')
print('score: ',score,'   ','normalised score: ',ns,'   ','percentage:','{:.2%}'.format(count/len(similarity)))
print(seq1,'\n','\n',similarity,'\n','\n',seq2,sep='')


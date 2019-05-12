#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:12:38 2019

@author: lanqi
"""

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

for p in range(0,110,10):
# define the basic variables of the model
    N=10000
    I=1
    R=0
    V=int(N*p*0.01)
    S=N-I-V-R
    beta=0.3
    gamma=0.05

# creat arrays for each variable
    S_list=[S]
    I_list=[I]
    R_list=[R]
# the following process is similar to SIR.py
    for i in range(0,1001):
# if p=100, which means all the people are not susceptible, they cannot become infected
        if S >= 1:
            proportion = I/N
            d1 = sum(np.random.choice(range(2),S,p=[1-beta * proportion, beta * proportion]))
            S = S-d1
            I = I+d1
# if no infected people, other people cannot be infected 
        if I >= 1:
            d2 = sum(np.random.choice(range(2),I,p=[1-gamma, gamma]))
            I = I-d2
            R = R+d2
        S_list.append(S)
        I_list.append(I)
        R_list.append(R)
        
    plt.plot(I_list,label=str(p)+'%')

plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.show()










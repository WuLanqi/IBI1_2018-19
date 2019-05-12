#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:12:38 2019

@author: lanqi
"""

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# define the basic variables of the model
N=10000
S=9999
I=1
R=0
beta=0.3
gamma=0.05

# creat arrays for each variable
S_list=[S]
I_list=[I]
R_list=[R]

"""
At each time point, we pick susceptible individuals at random to become infected. 
We pick infected individuals at random to become recovered. 
And we then keep track of the numbers of people in all three categories.

for each time point:
    
    for each susceptible people in S:
        d1=random.choice(0 or 1,time,[1-probabilities,probabilities])
        (0 means healthy, 1 means infected)
        time = S
        probabilities = beta * infected person(I)/population(N)
        d1=sum(d1)
        S = S-d1
        I = I+d1
    for each infected person in I:
        d2 =random.choice(0 or 1,time,[1-probabilities,probabilities])
        (0 means stay infected, 1 means recovered)
        time = I
        probabilities = gamma
        d2=sum(d2)
        I = I-d2
        R = R+d2     
"""

for i in range(0,1001):
    proportion = I/N
    d1 = sum(np.random.choice(range(2),S,p=[1-beta * proportion, beta * proportion]))
    S = S-d1
    I = I+d1
    if I >= 1:
        d2 = sum(np.random.choice(range(2),I,p=[1-gamma, gamma]))
        I = I-d2
        R = R+d2
    S_list.append(S)
    I_list.append(I)
    R_list.append(R)

plt.figure(figsize=(6,4),dpi=150)

plt.plot(S_list,label='susceptible')
plt.plot(I_list,label='infected')
plt.plot(R_list,label='recovered')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()

plt.savefig("test.png",type="png")
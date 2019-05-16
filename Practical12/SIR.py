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

for each time point (loop 1000 time points):
    
-----get infected-----
    
    randomly choose 0 or 1 and make S times choices
    (0 means healthy, 1 means infected)
    probability for getting infected = beta * infected person(I)/population(N)
    probability for remaining susceptible = 1 - probability for getting infected
    sum the chosen number and the number represents the infected persons
    susceptible population minus the number
    infected population plus the number

-----recover----------   
    
    randomly choose 0 or 1 and make I times choices
    (0 means stay infected, 1 means recovered)z
    probability for recovering = gamma
    probability for remaining susceptible = 1 - gamma
    sum the chosen number and the number represents the recovered persons
    infected population minus the number
    recovered population plus the number    

----------------------
    append results into the list

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
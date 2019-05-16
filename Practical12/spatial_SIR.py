#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 13:11:51 2019

@author: lanqi
"""

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# make array of all susceptible population
population = np.zeros((100,100))
# choose one random point in our 100 × 100 array for where the outbreak happens
outbreak=np.random.choice(range(100),2)
population[outbreak[0], outbreak[1]] = 1
# plot heat map
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
# set up model parameters
beta=0.3
gamma=0.05

'''
for each time point:
    find infected points using where() function
    
    for each infected point in infected points:
        get x, y coordinates
        find its 8 neighbours (x-1~x+1,y-1~y+1)
        find x:
            find y:
                if (x,y) is not the infected point:
                    if (x,y) is not out of range:
                        if (x,y) is susceotible, not infected or not recovered:
                            random choice 0(p=1-beta) or 1(p=beta) and change the value of this point
                            (0 represents susceptible, 1 represents infected)
                           
        random choice 1(p=1-gamma) or 2(p=gamma) and change the value of this point
        (1 represents stay infected, 2 represents recovered)
        
    if time point = 10 or 50 or 100:
        plot

How will you find the infected points? 
-Use where() function that numpy provides.

For each infected point, how do you address all its neighbours? 
Are there cases where this could be difficult?
-Details seen above

How do you check that neighbours are not recovered?
-The value of that point is equal to 0

How do you infect the neighbours?
-Random choice 0 or 1 with certain probability and change the value of that point

How do you allow infected individuals to recover?
-Randome choic 1 or 2 with certain probability and change the value of that point

How can you plot the outcome? 
-At chosen time point(using if), use imshow function to plot
'''
for t in range(0,101):
    # find infected points
    infectedIndex = np.where(population==1)
    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # infect all 8 neighbours
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                # don't infect yourself
                if (xNeighbour,yNeighbour) != (x,y):
                    # make sure I don't fall off an edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # only infect neighbours that are not already infected
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
       
        # 1 represents stay infected, 2 represents recovered
        population[x,y]=np.random.choice(range(1,3),1,p=[1-gamma,gamma])[0]
    
    if t ==10 or t==50 or t==100:
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')   
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 18:33:02 2019

@author: lanqi
"""
'''
----------------------------Abstract of this code------------------------------

Main part:
    First, convert xml file into a cps file
    Then, run a Copasi model from within Python
    According to the created results file(.csv), plot the content of this file
    Time course and limit cycle are plotted and well labelled

Extended part I:
    Alter the values of four parameters
    Plot new figures

Extended part II:
    Run a number of simulations (e.g. 100 times)
    Assess the results by plotting one figure or plotting seperate figures
''' 

#-----------------------------------code---------------------------------------

#In order to make things simpler, make cps file and python file in the same directory 
#And also make python change into that directory
import os
os.chdir('/Users/lanqi/Desktop/IBI1_2018-19/Practical13')

#------------convert the .xml file into a .cps file and run it-----------------

#function from Melanie
def xml_to_cps():
    import os
    import xml.dom.minidom
    
    # first, convert xml to cps 
    os.system("/Applications/COPASI/CopasiSE -i predator-prey.xml -s predator-prey.cps")
    
    # now comes the painful part. Just copy and paste this ok
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
        
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
                
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
               
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey.cps","w")
    cpsTree.writexml(cpsFile)
    cpsFile.close()    

#use the function to convert the file and run it  
xml_to_cps()
#To tell whether this worked, I run Python and see whether a new file modelResults.csv has been created

#---------------------read file and make arrays--------------------------------

import numpy
import matplotlib.pyplot as plt
# open the file
rf=open('modelResults.csv','r')
# read entire file into list of line strings 
rf=rf.readlines()

# create arrays
# L stores the results data
L = []
# names stores the variable names
names = []
# count is used to seperate names form results data
count = 0

for line in rf:
    # the first line of results file are names and will be stored in list of names
    if count == 0:
        # get comma-seperated string
        names = line.split(',')
        count = 1
    else:
        l = line.split(',')
        #timepoint = l[0]
        #delete timepoints for plotting bacause indexes represent time points
        #after deleting, the array only contains results data
        del(l[0])
        L.append(l)
        
#transform it into a numpy array, which makes indexing easier
results=numpy.array(L)
#transform the numbers into actual numbers
results=results.astype(numpy.float)

#-----------------------------Time course--------------------------------------

# name_of_array[:,n] represents the n-1 column of array
plt.plot(results[:,0],label='Predator (b=0.02, d=0.4)')
plt.plot(results[:,1],label='Prey (b=0.1, d=0.02')
plt.xlabel('time')
plt.ylabel('population size')
plt.title('Time course')
plt.legend()
plt.show()

#----------------------------Limit cycle---------------------------------------

# Limit cycle plots predator population against prey population
# It is useful or interesting because of the following reasons
# 1. The correlation between predator and prey is more explicit
# 2. The closed curve shows a balance between predator and prey
# 3. This curve shows diversity of condition 
# (one value of predator population can correspond to two values of prey population)

#x axis is the first column of array (predator population)
#y axis is the second column of array (prey population)
plt.plot(results[:,0],results[:,1])
plt.xlabel('predator population')
plt.ylabel('prey population')
plt.title('Limit cycle')
plt.show()

##########################change parameters####################################

#-------------------------------new codes--------------------------------------

import xml.dom.minidom
# parse the XML file into a DOM document object
DOMTree=xml.dom.minidom.parse('predator-prey.xml')
# get the root element of the document
collection= DOMTree.documentElement
# a list of parameters
parameters=collection.getElementsByTagName("parameter")

#since the change is similar for each parameter, a simple function is designed to reduce typing
def change():
    #let user know the name and value of this parameter
    print('parameter:',name,'initial value:',param.getAttribute('value'))
    #let user input the number which value changes into
    v=input('Please change the value of '+name+' (input any number between 0 and 1):\n')
    #change the value in the file
    param.setAttribute('value',v)

#loop each parameter
for param in parameters:
    name = param.getAttribute('name')
    if name == 'k_predator_breeds':
        change()
        #store the value for legend, followa are the same
        b1 = param.getAttribute('value')
    if name == 'k_predator_dies':
        change()
        d1 = param.getAttribute('value')
    if name == 'k_prey_breeds':
        change()
        b2 = param.getAttribute('value')
    if name == 'k_prey_dies':
        change()
        d2 = param.getAttribute('value')
        
#save changes into file
filexml = open('predator-prey.xml','w')
DOMTree.writexml(filexml)
filexml.close()

#---------------------------(almost) old codes---------------------------------

#plotting is same as before
xml_to_cps()
os.system('/Applications/COPASI/CopasiSE predator-prey.cps')

rf=open('modelResults.csv','r')
rf=rf.readlines()

L = []
names = []
count=0
for line in rf:
    if count==0:
        names = line.split(',')
        count = 1
    else:
        l = line.split(',')
        del(l[0])
        L.append(l)
        
results=numpy.array(L)
results=results.astype(numpy.float)

#time course
#there are some changes on how to label (here is what different from before)
plt.plot(results[:,0],label='Predator (b='+b1+', d='+d1+')')
plt.plot(results[:,1],label='Prey (b='+b2+', d='+d2+')')

plt.xlabel('time')
plt.ylabel('population size')
plt.title('Time course')
plt.legend()
plt.show()

#limit cycle
plt.plot(results[:,0],results[:,1])
plt.xlabel('predator population')
plt.ylabel('prey population')
plt.title('Limit cycle')
plt.show()

###########################Running many simulations############################

#-------------------------------new codes--------------------------------------
import numpy
#run 100 times for 100 simulations
for t in range(0,100):
    #loop each parameter (loop is similar to that in 'change parameters')
    for param in parameters:
        name = param.getAttribute('name')
        print('parameter:',name,'initial value:',param.getAttribute('value'))
        # draw a random number between 0 and 1
        v=str(numpy.random.sample())
        param.setAttribute('value',v)
        value = param.getAttribute('value')
        print('The value is changed into:',value)
        if name == 'k_predator_breeds':
        #store the value for legend, followa are the same
            b1 = param.getAttribute('value')
        if name == 'k_predator_dies':
            d1 = param.getAttribute('value')
        if name == 'k_prey_breeds':
            b2 = param.getAttribute('value')
        if name == 'k_prey_dies':
            d2 = param.getAttribute('value')
            
    #save changes into file
    filexml = open('predator-prey.xml','w')
    DOMTree.writexml(filexml)
    filexml.close()

#-----------------old codes (same in 'change parameters')----------------------
    
    #plotting is same as before
    xml_to_cps()
    os.system('/Applications/COPASI/CopasiSE predator-prey.cps')

    rf=open('modelResults.csv','r')
    rf=rf.readlines()

    L = []
    names = []
    count=0
    for line in rf:
        if count==0:
            names = line.split(',')
            count = 1
        else:
            l = line.split(',')
            del(l[0])
            L.append(l)
        
    results=numpy.array(L)
    results=results.astype(numpy.float)

    #time course
    plt.plot(results[:,0],label='Predator (b='+b1+', d='+d1+')')
    plt.plot(results[:,1],label='Prey (b='+b2+', d='+d2+')')

    plt.xlabel('time')
    plt.ylabel('population size')
    plt.title('Time course')
    plt.legend()
    
#way 1:
#plot all the combinations in one figure (length of legend is horribile)
plt.show() 

    #way 2: 
    #plot seperate figure for each combination (number of figures is horribile)
    #plt.show()



        
    





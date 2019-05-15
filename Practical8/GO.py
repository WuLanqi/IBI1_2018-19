#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:02:43 2019

@author: lanqi
"""

import xml.dom.minidom
import re
import pandas as pd
#parse the XML file into a DOM document object
DOMTree = xml.dom.minidom.parse("/Users/lanqi/Desktop/IBI1_2018-19/Practical8/go_obo.xml")
#Get the root element of the document
collection= DOMTree.documentElement
#a list of elements
terms=collection.getElementsByTagName("term")

'''
Function: CollectChildenGOIDSet (GOID, resultSet)
    Init: set resultSet to empty before calling the function
    depends: Global variabe terms - all terms tag of the obo xml
    
    for term in terms:
        get all <is_a> relationship tag, store them in parent_list
        for parent in parent_list:
            if parent.id = GOID:
                (found a child for this GOID)
                add term in resultSet
                CollectChildenGOIDSet (term_id, resultSet)

In the main program, count the elements in resultSet
'''
#Function to find childNodes
def CCN(id, resultSet):
    for gene in terms:
        parents = gene.getElementsByTagName("is_a")
        gene_id = gene.getElementsByTagName('id')[0].childNodes[0].data
        for parent in parents:
            if parent.childNodes[0].data == id:
                resultSet.add(gene_id)
                CCN(gene_id, resultSet)

#create a pandas.Dataframe to store the output
df = pd.DataFrame(columns=['id','name','definition','childnodes'])


re_compile= re.compile(r'autophagosome')
for gene in terms:
    defstr= gene.getElementsByTagName("defstr")[0].childNodes[0].data
    #find terms that contain the word 'autophagosome'
    if re_compile.search(defstr):
        print('*****gene*****')
        id=gene.getElementsByTagName('id')[0].childNodes[0].data
        print('id:',id)
        name=gene.getElementsByTagName('name')[0].childNodes[0].data
        print('name:',name)
        print('defstr: ',defstr)
        resultSet=set()
        CCN(id, resultSet)
        df = df.append(pd.DataFrame({'id':[id],'name':[name],'definition':[defstr],'childnodes':[len(resultSet)]})) 
        print('childNodes:', len(resultSet))

#save to excel
res= r'/Users/lanqi/Desktop/IBI1_2018-19/Practical8/autophagosome.xlsx'
df.to_excel(res,index=False)


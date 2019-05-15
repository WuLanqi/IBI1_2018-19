#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:05:11 2019

@author: lanqi
"""

import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#------------------------------find correct address----------------------------
#open address_information.csv file
a=open('/Users/lanqi/Desktop/IBI1_2018-19/Practical6/address_information.csv','r')
#creat a list to store correct email addresses
L=[]
#loop each line in file
for line in a:
    #get the comma-separated information
    line=re.split(r',+',line)
    #get the email address (the second element of each list is email address)
    if re.match(r'\S+@\S+',line[1]):
        #check whether the email address is correct (correct address contains ".com")
        if not '.com' in line[1]:
            #tell user it is a wrong address
            print(str(line[1]),': Wrong Address!')
            continue
        #tell user it is a correct address
        print(str(line[1]),': Correct Address!')
        #append correct addresses into the list
        L.append(line)

print(L)
#close the file
a.close()

#-----------------------------send email---------------------------------------
#open body.txt file
Text=open('/Users/lanqi/Desktop/IBI1_2018-19/Practical6/body.txt','r')
#read entire file into a single string
text=Text.read()
#close the file
Text.close()

#input messages of sender
sender = input('sender address:')
#e.g. xxxxxxxxxx@zju.edu.cn
password = input('password:')

#there are 3 receivers with correct email address
for i in range(0,3):
    #change "User" into corresponding receiver
    text=text[0:5]+str(L[i][0])+text[9:len(text)+1]
    receivers = [str(L[i][1])]
    
    #setup message, plain means no-format, utf-8 is the encoding
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = Header(sender, 'utf-8')
    message['To'] =  Header(text)
    subject = str(L[i][2])
    message['Subject'] = Header(subject, 'utf-8') 
    #actually send the email
    try:
        #setup SMTP object, port for server is 25
        smtp = smtplib.SMTP('smtp.zju.edu.cn',25)
        smtp.login(sender,password)
        smtp.sendmail(sender, receivers, message.as_string())
        print ("Mail sent successfully!")
    except smtplib.SMTPException:
        print ("Mail did not sent successfully!")
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:05:11 2019

@author: lanqi
"""
#open the file
a=open('/Users/lanqi/Desktop/IBI1_2018-19/Practical6/address_information.csv','r')
import re
L=[]
for line in a:
    #get the comma-separated information
    line=re.split(r',+',line)
    print(line)
    #get the correct email address
    if re.match(r'\S+@\S+',line[1]):
        if not '.com' in line[1]:
            print(str(line[1]),': Wrong Address!')
            continue
        print(str(line[1]),': Correct Address!')
        L.append(line)
print(L)

#send email
import smtplib
from email.mime.text import MIMEText
from email.header import Header

Text=open('/Users/lanqi/Desktop/IBI1_2018-19/Practical6/body.txt','r')
text=Text.read()
for i in range(0,3):
    text=text[0:5]+str(L[i][0])+text[9:len(text)+1]
    sender = '3180111438@zju.edu.cn'
    password='Pp65221922ll'
    receivers = [str(L[i][1])]  # 接收邮件的邮箱
 # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = Header("Lanqi", 'utf-8')   # 发送者
    message['To'] =  Header(text)        # 接收者 
    subject = str(L[i][2])
    message['Subject'] = Header(subject, 'utf-8') 
    try:
        smtp = smtplib.SMTP('smtp.zju.edu.cn',25)
        smtp.login(sender,password)
        smtp.sendmail(sender, receivers, message.as_string())
        print ("Mail sent successfully!")
    except smtplib.SMTPException:
        print ("Mail did not sent successfully!")
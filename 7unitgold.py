# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 18:56:48 2021

@author: SAI
"""

#program of 7 unit gold can cut minimum number of cuts so that the king can 
#give the salary to his worker everyday the king have to give 1 unit of gold to his worker

i=0
if(i==0):
     a=pow(2,i)
     print("1st day payment is:",a)
i=1
if(i==1):
     b=pow(2,i)
     print("2nd day payment is:",b)
i=2
if(i==2):
     
     print("3rd day payment is:",a+b)
i=3
if(i==3):
     c=pow(2,2)
     print("4th day payment is:",c)
i=4
if(i==4):
     
     print("5th day payment is:",a+c)
i=5
if(i==5):
     
     print("6th day payment is:",c+b)
i=6
if(i==6):
     
     print("7th day payment is:",a+b+c)


# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 09:02:54 2021

@author: SAI
"""

#write a program to sum of even number from 10 to 20 
N1=int(input("enter maximum numbers:"))
N2=int(input("enter minimumm number:"))
m=int(N1/2)
p=int(N2/2)
sum1=m*(m+1)
sum2=p*(p+1)
a=sum1-sum2
print(a)
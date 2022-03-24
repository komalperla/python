# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 08:18:14 2021

@author: SAI
"""

#this is AND OR XOR operation
str=input("enter string:")
a=int(str[0])
for i in range(1,len(str)):
    if(str[i]=='A'):
        a&=int(str[i+1])
    if(str[i]=='B'):
        a|=int(str[i+1])
    if(str[i]=='C'):
        a^=int(str[i+1])
print(a)
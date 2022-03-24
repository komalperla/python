# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 20:29:23 2021

@author: SAI
"""
str='*#*#*#*#*#*#*#*#*#*#*##**#####'
count1=0
count2=0
for i in range(0,len(str)):
    if(str[i]=='*'):
        count1+=1
    else:
        count2+=1
print("no of stars:",count1)
print("no of hash:",count2)    

# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 09:17:15 2021

@author: SAI
"""

n=int(input("enter no:"))
fact=1
if(n==0):
    print("factorial of 0 is always 1")
for i in range(1,n):
    fact += fact*i
print(fact)
    
        
            
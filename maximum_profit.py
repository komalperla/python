# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 19:25:37 2021

@author: SAI
"""

#given the trade of a company maximize your profit 
A=[455,460,465,451,414,415,441]
set(A)
list(A)
m=0
for i in range(0,len(A)):
    for j in range(i+1,len(A)):
        m=max(m,A[j]-A[i])
print("maximum profit:",m)
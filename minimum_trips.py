# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 19:38:24 2021

@author: SAI
"""
#maximum weight to minimum no. of trips
A=[10,8,5,3]
L=[5,10,9,5]
count=0
a=sorted(A)
print(a)
for i in range(0,len(a)):
    for j in range(0,len(L)):
          m=max(a)
          n=min(a)
          if(m+n==L):
              count+=1
print(count)
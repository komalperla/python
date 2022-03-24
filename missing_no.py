# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 08:25:43 2021

@author: SAI
"""

#wrute a program to determine the missing no from 1 to N
N=int(input("enter no of elements to be entered:"))
l=[]
if(N>1):
   for i in range(1,N):
       ele=int(input())
       l.append(ele)
   a=N*(N+1)
   s=round(a/2)
   missing_no=s-sum(l)
   print("missing number is:",missing_no)
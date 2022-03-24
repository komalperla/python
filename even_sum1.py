# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 08:44:03 2021

@author: SAI
"""

#write a program to sum of even number from 10 to 20 
N=int(input("enter maximum numbers:"))
N1=N/2
a=N1*(N1+1)
N2=N1/2
b=N2*(N2+1)
print(a)
print(b)
sum=a-b
print("sum of even numbers from 10 to 20:",sum)
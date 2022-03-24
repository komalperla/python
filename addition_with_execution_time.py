# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 17:18:30 2021

@author: SAI
"""

#write a program to add two numbers and calculate the time taken by the program
import time
t0=time.time()
local_time=time.ctime(t0)
print(local_time)
a=int(input("enter first number:"))
b=int(input("enter second number:"))
sum=a+b
print("sum of two numbers is:",sum)
t1=time.time()
localtime1=time.ctime(t1)
print(localtime1)
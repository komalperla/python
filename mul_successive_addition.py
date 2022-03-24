# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 17:26:58 2021

@author: SAI
"""

#write a program to multiple two numbers by sccessive addition
a=int(input("enter first number:"))
b=int(input("enter second number:"))
mul=0
if(a>b):
    for i in range(0,b):
         mul+=a
         print(mul)
else:
    for i in range(0,a):
        mul+=b
        print(mul)
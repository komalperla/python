# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 10:05:22 2021

@author: SAI
"""

def div_by(x,y,z):
    return x%y==0 and x%z==0
a=int(input("enter first nunmber: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
div=div_by(a,b,c)
print(div)
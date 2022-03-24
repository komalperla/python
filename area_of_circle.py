# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 09:35:05 2021

@author: SAI
"""
from math import *
def area_of_circle(r):
    a=pi*r**2
    return a
x=float(input("enter radius of circle:"))
area=area_of_circle(x)
print("the area of circle with radius",x,"is",area)
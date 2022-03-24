# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 09:29:59 2021

@author: SAI
"""
from math import log
# WAP to add two numbers without using '+' operation operator or any inbuilt function
def add_x_y(x,y):
    return x-(-y)
print("addition:",add_x_y(6,7))

a=10
b=5
while(b!=0):
    data=a&b
    a=a^b
    b=data<<1
print("addition:",a)

while(b>0):
    ++a
    --b
print(a)

x=10
y=-5
while(y<0):
    ++x
    ++y
print(x)
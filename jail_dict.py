# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 20:18:15 2021

@author: SAI
"""

#jail
n=int(input("enter no of cells:"))
ipl=dict()
for i in range(n):
    name=int(input("enter cell number::"))
    runs=int(input("enter no of criminals:"))
    ipl[name]=runs
for x,y in ipl.items():
    if(y<5):
        print(x,':',y)


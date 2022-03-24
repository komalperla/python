# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 20:05:36 2021

@author: SAI
"""

#create a dict with names of IPL players with there highest runs score.
n=int(input("enter no of players:"))
ipl=dict()
for i in range(n):
    name=input("enter player name:")
    runs=int(input("enter runs:"))
    ipl[name]=runs
print(ipl)
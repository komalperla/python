# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 14:58:53 2022

@author: SAI
"""

dead_count=int(input("Dead Count:"))
if(dead_count<0):
    print("Invalid input")
injured_count=int(input("Injured Count:"))
if(injured_count<0):
    print("Invalid input")
safe_count=int(input("Safe Count:"))
if(safe_count<0):
    print("Invalid input")
if(dead_count>0 or injured_count>0 or safe_count>0 ):
    print("TSUNAMI REPORT OF JAPAN ")
    print("The number of people")
    print("Dead:",dead_count)
    print("Injured:",injured_count)
    print("Safe:",safe_count)
    print(" Please help the people who are suffering!!!")

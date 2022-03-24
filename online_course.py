# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 12:15:47 2022

@author: SAI
"""

n=int(input("Enter number of courses: "))
d={}
if(n>1):
    for i in range(n):
        print("Enter name of the subject and mark respectively:")
        name=input()
        mark=int(input())
        if(mark>0 and mark<100):
            d[name]=mark
        else:
            print("Invalid mark")
    print("The courses you have cleared are:")
    for key,value in d.items():
        if(value>=80 and value<=100):
            print(key,value)
else:
    print("invalid input")
        
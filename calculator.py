# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 08:16:07 2021

@author: SAI
"""

#this is program of calculator of two operation
operation=int(input("enter operation for addition 1 and for subtraction 2:"))
if(operation==1 or operation==2):
    first_num,second_num=input("enter two nos:").split() # accepting more than one input from the user
    if(operation == 1):
        print("the sum of",first_num,"and",second_num,"is:",int(first_num) + int(second_num))
    if(operation == 2):
        print("subtraction of",first_num,"and",second_num,"is:",int(first_num) - int(second_num))
else:
    print("invalid operation")
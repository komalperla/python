# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 20:54:25 2021

@author: SAI
"""
#this is program of calculator of two operation power of two and division
operation=int(input("enter operation for addition 1 and for subtraction 2:"))
first_num,second_num=input("enter two nos:").split() # accepting more than one input from the user
if(first_num or second_num == 0):
     print("no is invalid")
     if(operation==1 or operation==2):
         if(operation == 1):
           print("the power of",first_num,"is:",int(first_num)**2)
         if(operation == 2):
            print("division of",first_num,"and",second_num,"is:",int(first_num) / int(second_num))
     else:
         print("invalid operation")
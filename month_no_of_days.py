# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 09:18:09 2021

@author: SAI
"""

month_no=int(input("enter the month number:"))
list_31=[1,3,5,7,8,10,12]
list_30=[4,6,9,11]
if(month_no>0 and month_no<13):
    if month_no in list_31:
        print("the month has 31 days")
    elif month_no in list_30:
        print("the month has 30 days")
    else:
        print("the month has 28 or 29 days")
else:
    print("please enter month no in 1- 12 only")
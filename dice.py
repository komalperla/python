# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 20:12:16 2021

@author: SAI
"""

#given number as a input check how many possible combination can be obtained 
#by throwing two dice such that the sum on the two dice should be equal to 
#the given number.
count=0
N=int(input("enter number:"))
if(N<13):
    for i in range(0,7):
        for j in range(0,7):
            if(i+j==N):
                count+=1
    print(count)
else:
    print("please enter number in 1 to 12")
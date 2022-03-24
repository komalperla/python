# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 08:24:48 2021

@author: SAI
"""
#check the number is divisible by 11 or not
num=input("enter number:")
even=0
odd=0
for i in range(0,len(num)):
    if(i%2==0):
        even+=int(num[i])
        print("even:",even)
    else:
        odd+=int(num[i])
        print("odd:",odd)
if((even-odd)==0 or (even-odd)==11):
    print("the number",num,"is divisible by 11")
else:
    print("the number",num,"is not divisible by 11")
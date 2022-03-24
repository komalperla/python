# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 16:58:41 2021

@author: SAI
"""

print("enter three numbers:")
num1=int(input())
num2=int(input())
num3=int(input())
if(num1>num2 and num1>num3):
    lcm=num1
elif(num2>num1 and num2>num3):
    lcm=num2
else:
    lcm=num3
while True:
    if(lcm%num1==0 and lcm%num2==0 and lcm%num3==0):
        break
    else:
        lcm=lcm+1
print(lcm)
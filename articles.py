# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 17:38:27 2021

@author: SAI
"""

#write a program to puchases maximum number of articles for given money
money=int(input("enter money:"))
articles=[4,7,9,39,40,55,20,12,14,15]
print(articles)
sort=sorted(articles)
print(sort)
x=0
count=0
for i in range(0,len(sort)):
    if(sort[i]<money):
        x=x+sort[i]
        count+=1
print("sum of articles:",x)
print("no of articles:",count)
        





































# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 15:20:29 2021

@author: SAI
"""

str='abcde'
x=str[0:1].upper() + str[1:len(str)-1] + str[len(str)-1:len(str)].upper()
print(x)
str2='abcdefghijklmnop'
for i in range(0,len(str2)):
    if i % 2 == 0:
        str2[i].upper()
print(str2)
          
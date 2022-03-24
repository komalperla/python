# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 08:41:08 2021

@author: SAI
"""

import array
a=array.array('i',[1,2,3,4])
print(a)
b=type(a)
print(b)
a.append(10)
print(a)
a.extend([9,8,7,6])
print(a)
a.insert(4,5)
print(a)
a.remove(10)
print(a)
a.pop(5)
print(a)
a.pop()
print(a)
c=array.array('i',[11,12,13,14,15])
print(c)
print(a[0:3])
for x in a:
    print(x)
x=0
while x < len(c) :
    print(c[x])
    x=x+1
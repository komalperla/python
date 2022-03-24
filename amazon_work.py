# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 09:11:59 2021

@author: SAI
"""
#amazon workers are stacking up empty boxes at the end
def move_empty_to_end(arr):
    for i in arr:
        if(i==0):
            arr.remove(i)
            arr.append(i)
    return arr
list=[1,3,0,6,0,5,0,4]
print(move_empty_to_end(list))

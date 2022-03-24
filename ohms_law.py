# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 20:06:42 2021

@author: SAI
"""

#ohms laws
def ohms_law(v=0,i=0,r=0):
    if v==0:
        return i*r
    elif i==0:
        return v/r
    elif r==0:
        return v/i
    else:
        return 0
print("voltage:",ohms_law(0,10,5))
print("current:",ohms_law(20,0,5))
print("resistance:",ohms_law(24,6,0))    
    
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 09:49:07 2022

@author: SAI
"""

Age=int(input("Enter the age:"))
tax=0
if(Age<18 and Age>100):
    Income=int(input("Enter the income:"))
    if(Income>0):
        if(Age<=60):
            if(Income<=250000):
                tax=(Income*0)/100
            elif(Income>250000 and Income<=500000):
                tax=(Income*10)/100
            elif(Income>500000 and Income<=1000000):
                tax=(Income*20)/100
            elif(Income>1000000):
                tax=(Income*30)/100
        elif(Age>60 and Age<=80):
            if(Income<=300000):
                tax=(Income*0)/100
            elif(Income>300000 and Income<=500000):
                tax=(Income*10)/100
            elif(Income>500000 and 1000000):
                tax=(Income*20)/100
            elif(Income>1000000):
                tax=(Income*30)/100
    elif(age>80):
        if(Income<=5000000):
            tax=(Income*0)/100
        elif(Income>500000 and Income<=1000000):
             tax=(Income*20)/100
        elif(Income>1000000):
            tax=(Income*30)/100
   print("The Tax amount is:%.2f" %tax)
   else:
      print("Invalid Income")
         
    
      
    
        


    
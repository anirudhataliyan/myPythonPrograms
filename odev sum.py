# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 11:24:33 2019

@author: APS
"""

a=1
ev=0
od=0
while a<=10:
    if a%2==0:
       ev=ev+1
    else:
      od=od+1
    a=a+1
print ("count of even no",ev) 
print ("count of odd no",od) 
a=1
sume=0
sumod=0
while a<=10:
    if a%2==0:
        sume=sume+a
    else:
        sumod=sumod+a
    a=a+1
print ("sum of ev", sume)
print ("sum of od",sumod)
    
      
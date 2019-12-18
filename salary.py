# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:49:58 2019

@author: APS
"""

a=int(input("your salary"))
if a<10000:
    da=a*5/100
    hra=a*7/100
if a>10000 and a<20000:
    da=a*9/100

    hra=a*11/100
if a>20000:
    da=a*10/100
    hra=a*12/100
gs=a+da+hra
print("da is",da)
print("hra is",hra)
print("gs is",gs)    
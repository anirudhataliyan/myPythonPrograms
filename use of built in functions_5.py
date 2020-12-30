# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 19:52:25 2020

@author: HP
"""

#input a number and converts ito nearest integer using
# two different built in functions. It also disaplay the given number
# rounded off to 3 places after decimal.

num=float(input("enter a real number:"))
tnum=int(num)
rnum=round(num)
print(tnum,"and",rnum)
rnum2=round(num,3)
print(num,"rounded off to 3 places after decimal is",rnum2)
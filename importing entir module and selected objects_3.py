# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 13:06:22 2020

@author: HP
"""
#importing modules and its functions
#example 1
import tempconversion_1
print(tempconversion_1.to_centigrade(98.6))

#example 2
# giving alias name
import tempconversion_1 as tc
print(tc.to_centigrade(98.6))

#example 3
#to import single object
from math import pi
print(pi)

#example 4
# to import multiple objects
from math import sqrt,pow
from tempconversion_1 import to_centigrade
print(tempconversion_1.to_centigrade(98.6))
print(sqrt(25))
print(pow(3,3))
print
#example 5
# to import all modules
from math import *
from tempconversion_1 import *
print(tempconversion_1.to_centigrade(98.6))
print(tempconversion_1.to_fahrenhit(98.6))
print(sqrt(25))
print(pow(3,3))


#Example 6
from tempconversion_1 import *
print(FREEZZING_C)
FREEZZING_C=17.5
print(FREEZZING_C)

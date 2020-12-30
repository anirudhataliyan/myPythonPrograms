# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:18:56 2020

@author: HP
"""
"""Conversion functions between fahrehit and centrigrade"""


#Functions
def to_centigrade(x):
    """Returns :x converted to centigrade"""
    return 5*(x-32)/9.0

def to_fahrenhit(x):
    """Returns :x converted to fahreheit"""
    return 9*x/5.0+32

#constants
FREEZZING_C=0.0
FREEZING_F=32.0

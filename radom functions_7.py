# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 13:34:56 2020

@author: HP
"""

import random
print(random.random()) #The output generated is b/w range[0.0,1.0]

print(random.random()*(35-15)+15) # The output generated floating point number b/w 15 to 35

print(random.randint(15,35)) # the output generated is integer b/w range 15 to 35

print(random.uniform(11,55)) # generating floating point random number in the range 11 to 55


print(random.randrange(23,47,3))#generate a random integer in the range 23 to 47 with step 3 

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 19:56:39 2020

@author: HP
"""

# String fucntions

#1. Join

print("*".join("Hello"))

print("***".join("Hello"))

print("$$".join(["trial","hello"])) # When Joined with list

print("$$".join(("trial","hello","new"))) #when joined with tuple

#print("$$".join((123,"hello","new"))) # sequence must contain string otherwise python will give error

#2. split 

print("I love python".split())
# or
print("I Love python".split(" "))

print("I love python".split("o")) # Given string is divided from positon contained "o"


#3. Replace
print("I love python".replace("python","Programming"))
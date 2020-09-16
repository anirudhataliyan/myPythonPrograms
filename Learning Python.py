

#i =0
#while (True):("")
#print(i+ddas1)
    #if(i==44):
        #break
    #i = i + 1f


#OPERATORS IN PYTHON
#Arithmetic Operators
#Comparison (Relational) Operators
#Assignment Operators
#Logical Operators
#Bitwise Operators
#Membership Operators
#Identity Operators

#1. Arithmetic Operators - Numeric Operations
#print("5 + 6 : ", 5+6)
#print("5 - 6 : ", 5-6)
#print("5 * 6 : ", 5*6)
#print("5 / 6 : ", 5/6)
#print("5 // 6 : ", 5//6) #It basically works with decimal value and for  float int
#print("5 ** 3 : ", 5**3) #Raise to the power ... 5*5*5*5*5*5
#print("5 % 6 : ", 5%6) #It will gives the remainder it i divide 5 by 6 .. 


#2. Assignment Operators - It assign any value or operator with value in a var
#x = 5
#print(x)
#x +=6
#print(x)
#x -=6
#print(x)
#x *=6
#print(x)
#x /=6
#print(x)
#x //=6
#print(x)
#x **=6
#print(x)

#3. Comparison (Relational) Operators
#i = 5
#print(i>=5)
#print(i == 6)
#print(i == 5)

#4. Logical Operators
#a = True
#b = False
#print(a and b) #True and false = false

#They are Used For "and" operator
#True and True = True
#True and False = False      

#5. Identity Operators
#a = True 
#b = False
#print(a is b)
#print(a is not b)

#print(5 is 6)
#print(5 is not 6)

#print(5 is 5)
#print(5 is not 5)



#6. Membership Operators
#list = [3, 4, 5, 6, 34, 43, 4, 334, 3, 4]
#print(4 in list)
#print(32 in list)
#print(32 not in list)

#7. Bitwise Operators - It is for binary numbers
#0 - 00
#1 - 01
#2 - 10
#3 - 11
#print(0 | 3)
#print(0 and 3)


#FUNCTIONS USED IN PYTHON
#(i) Builtin Functions
#a = 9
#b = 8
#c = sum((a, b))
#print(c)

#(ii) User defined Function 
#def function1(a, b):
      #print("Hello You Are in function1", a+b)
      
#def function2 (a, b):
      #average = (a+b)/2
      #print(average)
      #return average
      
#v = function2(5, 7)
#print(v)





#   Try Except Exception Handling In Python 
#x = input("Enter Your Number : ")
#y = input("Enter 2nd Number : ")
#try:
    #print("The sum of these numbers is : ",int(x) + int(y))    
#except Exception as e:
    #print(e)
#print("This Line Is very Important")
#f = open("Anirudha.txt", "rt")
#content = f.read()
#print(content)



#FILE IO BASICS
#for line in f:
#print(line, end="")
#print(f.readline())
#print(f.readline())
#print(f.readline())
#print(f.readline())
#print(f.readlines())
# f = open("harry.txt", "w")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# f.close()
# f = open("harry2.txt", "a")
# a = f.write("Harry bhai bahut achhe hain\n")
# print(a)
# f.close()
# Handle read and write both
#f = open("harry2.txt", "r+")
#print(f.read())
#f.write("thank you")
#f = open("abc.txt")
#print(f.readline())
#print(f.tell())
#f.seek(10)
#print(f.readline())
#print(f.tell())




#Using With Block
#with open("abc.txt") as f: #Isme Close Karne ki zarurrat nhi hai
    #a=f.read(4)
    #print(a)





#Scope, Global Variables and Global Keyword
#l = 10  #Global
#def function1 (n):
    #l = 5 #Local
    #m = 8 #Local
    #global l
    #l = l+10
    #print(l, m)
    #print(n, "i have printed")
#function1("This is me")
#print(m)
#x=89
#def function1():
    #x = 20
    #def function2():
        #global x
        #x = 10
    #print("Before()", x)
    #function2()
    #print("After()", x)
#function1()
#print(x)


#Recursions: Recursive Vs Iterative Approach
#def print2(str1):
    #print2(str1)
    #print2(str1)
    #print("This is "  + str1)
#print2("Anirudha")
# n! = n * n-1 * n-2 * n-3.......1
# n! = n * (n-1)!
#def factorial_iterative(n):
    #"""
        #:param n: Integer
        #:return: n * n-1 * n-2 * n-3.......1
    #"""
    #fac = 1
    #for i in range(n):
        #fac = fac * (i+1)
    #return fac
#def factorial_recursive(n):
    #"""
        #:param n: Integer
        #:return: n * n-1 * n-2 * n-3.......1
    #"""
    #if n ==1:
        #return 1
    #else:
        #return n * factorial_recursive(n-1)
    # 5 * factorial_recursive(4)
    # 5 * 4 * factorial_recursive(3)
    # 5 * 4 * 3 * factorial_recursive(2)
    # 5 * 4 * 3 * 2 * factorial_recursive(1)
    # 5 * 4 * 3 * 2 * 1 = 120
# 0 1 1 2 3 5 8 13
#def fibonacci(n):
    #if n==1:
        #return 0
    #elif n==2:
        #return 1
    #else:
        #return fibonacci(n-1)+ fibonacci(n-2)
#number = int(input("Enter then number"))
# print("Factorial Using Iterative Method", factorial_iterative(number))
# print("Factorial Using Recursive Method", factorial_recursive(number))
#print(fibonacci(number))

#Astrologers Stars EXERCISE
#a = int(input("please add number of line you want to print"))
#b = bool(int(input("please add 0 for False")))
#def star(a, b):
    #if b == True:
        #c = 1
        #while c <= a:
            #print(c * "*")
            #c = c + 1
    #else:
        #while a > 0:
            #print(a * "*")
            #a = a - 1
#star(a, b)

# Lambda functions or anonymous functions
#  minus = lambda x, y: x-y
# print(minus(9, 4))


# Health Management System
#def getdate():
    #import datetime
    #return datetime.datetime.now()
#import datetime
#def gettime():
    #return datetime.datetime.now()
#def take(k):
    #if k==1:
        #c=int(input("enter 1 for excersise and 2 for food"))
        #if(c==1):
            #value=input("type here\n")
            #with open("harry-ex.txt","a") as op:
                #op.write(str([str(gettime())])+": "+value+"\n")
            #print("successfully written")
        #elif(c==2):
            #value = input("type here\n")
            #with open("harry-food.txt", "a") as op:
                #op.write(str([str(gettime())]) + ": " + value + "\n")
            #print("successfully written")
    #elif(k==2):
        #c = int(input("enter 1 for excersise and 2 for food"))
        #if (c == 1):
            #value = input("type here\n")
            #with open("rohan-ex.txt", "a") as op:
                #op.write(str([str(gettime())]) + ": " + value + "\n")
            #print("successfully written")
        #elif (c == 2):
            #value = input("type here\n")
            #with open("rohan-food.txt", "a") as op:
                #op.write(str([str(gettime())]) + ": " + value + "\n")
            #print("successfully written")
    #elif(k==3):
        #c = int(input("enter 1 for excersise and 2 for food"))
        #if (c == 1):
            #value = input("type here\n")
            #with open("hammad-ex.txt", "a") as op:
                #op.write(str([str(gettime())]) + ": " + value + "\n")
            #print("successfully written")
        #elif (c == 2):
            #value = input("type here\n")
            #with open("hammad-food.txt", "a") as op:
                #op.write(str([str(gettime())]) + ": " + value + "\n")
            #print("successfully written")
    #else:
        #print("plz enter valid input (1(harry),2(rohan),3(hammad)")
#def retrieve(k):
    #if k==1:
        #c=int(input("enter 1 for excersise and 2 for food"))
        #if(c==1):
            #with open("harry-ex.txt") as op:
                #for i in op:
                    #print(i,end="")
        #elif(c==2):
            #with open("harry-food.txt") as op:
                #for i in op:
                    #print(i, end="")
    #elif(k==2):
        #c = int(input("enter 1 for excersise and 2 for food"))
        #if (c == 1):
            #with open("rohan-ex.txt") as op:
                #for i in op:
                    #print(i, end="")
        #elif (c == 2):
            #with open("rohan-food.txt") as op:
                #for i in op:
                    #print(i, end="")
    #elif(k==3):
        #c = int(input("enter 1 for excersise and 2 for food"))
        #if (c == 1):
            #with open("hammad-ex.txt") as op:
                #for i in op:
                    #print(i, end="")
        #elif (c == 2):
            #with open("hammad-food.txt") as op:
                #for i in op:
                    #print(i, end="")
    #else:
        #print("plz enter valid input (harry,rohan,hammad)")
#print("health management system: ")
#a=int(input("Press 1 for log the value and 2 for retrieve "))
#if a==1:
    #b = int(input("Press 1 for harry 2 for rohan 3 for hammad "))
    #take(b)
#else:
    #b = int(input("Press 1 for harry 2 for rohan 3 for hammad "))
    #retrieve(b)

# F STRINGS IN PYTHON
#import math
#me = "Harry"
#a1 =3
# a = "this is %s %s"%(me, a1)
# a = "This is {1} {0}"
# b = a.format(me, a1)
# print(b)
#a = f"this is {me} {a1} {math.cos(65)}"
# time
#print(a)









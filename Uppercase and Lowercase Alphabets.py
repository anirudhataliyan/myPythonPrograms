a = input("Please Enter Your Own Character : ")
if(a >= 'A' and a <= 'Z'):
    print("The Given Character ", a, "is an Uppercase Alphabet") 
elif(a >= 'a' and a <= 'z'):
    print("The Given Character ", a, "is a Lowercase Alphabet")
else:
    print("The Given Character ", a, "is Not a Lower or Uppercase Alphabet")
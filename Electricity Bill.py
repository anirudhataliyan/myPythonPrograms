#Electricity Bill Calculator
a = int(input("Enter The Unit consumed : "))
if a<=100:
    print("Total Amount = $",a*1)
elif a>100 and a<=200:
    print("Total Amount = $",(100)+(a-100)*2)
if a>200 and a<=300:
    print("Total Amount = $",(100*2)+(a-200)*3)
if a>300 and a<=400:
    print("Total Amount = $",(100*3)+(a-300)*4)
if a>400 and a<=500:
    print("Total Amount = $",(100*4)+(a-400)*5)
if a>500:
    print("Total Amount = $",(100+200+300+400+500)+(a-500)*6)
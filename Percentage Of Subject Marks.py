a = int(input("Enter Marks of English : "))
b = int(input("Enter Marks of Marhs/Bio : "))
c = int(input("Enter Marks of Physics : "))
d = int(input("Enter Marks of Chemistry : "))
e = int(input("Enter Marks of CS/IP/PE/ : "))
g = int(input("Enter Total Marks : "))
f = a+b+c+d+e
h = ((f/g)*100)
print("Sum : ", f)
print("Percentage : ", h)
if h>=90:
    print("First Division")
if h>=80 and h<90:
    print("Secound Division")
if h>=70 and h<80:
    print("Third Division")
if h<=30:
    print("Failed")





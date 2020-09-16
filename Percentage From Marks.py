a = int(input("Enter 1st No.: "))
b = int(input("Enter 2nd No : "))
c = int(input("Enter 3rd No.: "))
d = int(input("Enter 4th No.: "))
e = int(input("Enter 5th No.: "))
g = int(input("Total value : "))
h = (a+b+c+d+e)
f = (h/g) 
print("Sum Of your marksbn = ",h )
print("Your Percentage = ",f*100)

if f>=90:
    print("Selected")
if f>=85 and f<90:
    print("Waiting ")
if f>80 and f<=85:
    print("Shortlisted Waiting")
if f<80:
    print("Tryn after 5 years")

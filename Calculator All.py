#Made My Anirudha Kumar
while(True):
    print("Select Your Operator")
    print("1. Adition")
    print("2. Subtaction")
    print("3. Multiplication")
    print("4. Division")
    operator = input("Select your operator (1/2/3/4) : ")
    x = int(input("Enter Your First Number : "))
    y = int(input("Enter Your Secound Number : ")) 
    if operator == "1":
        print("Sum Of These Numbers Is : ", int(x) + int(y))    
    if operator == "2":
        print("Subtracted Number is : ", int(x)-int(y))
    if operator == "3":
        print("Multiplication of Number is : ", int(x)*int(y))
    if operator == "4":
        print("Divided Number is : ", int(x)/int(y))                      
    else:
        z = input("Press y to countinue And n to stop : ")
        if z == "n":
            print("Thanks ... See You Again") 
            break
        if z == "y":
            continue
        else:
            print("Thanks ... See You Again") 
            break
        
            
        
        
            
        
        
            


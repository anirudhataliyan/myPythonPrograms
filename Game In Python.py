import random
e = ['s', 'w', 'g' ]
f = 10
c = 0
h = 0
d = 0 
print("s For Snake\nw For Water\ng For Gun" )
while c<f:
    a = input("Enter Your Choise : ")
    b = random.choice(e)
    if a == b:
        print("Tie Both 0 point to each \n ")
        d = d + 0
        h = h + 0
    if a == "s" and b == "g":
        d = d + 1
        h = h + 0
        print(f"your guess {a} and computer guess is {b} \n")
        print("Computer Wins 1 Point")
        print(f"d is {d} and your point is {h} \n ")
    elif a == "s" and b == "w":
        h = h + 1
        print(f"your guess {a} and computer guess is {b} \n")
        print("Human wins 1 point ")
        print(f"computer_point is {d} and your point is {h} \n")
    elif a == "w" and b == "s":
        d = d + 1
        print(f"your guess {a} and computer guess is {b} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {d} and your point is {h} \n ")    
    elif a == "w" and b == "g":
        h = h + 1
        print(f"your guess {a} and computer guess is {b} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {d} and your point is {h} \n")
    elif a == "g" and b == "s":
        h = h + 1
        print(f"your guess {a} and computer guess is {b} \n")
        print("Human wins 1 point \n")
        print(f"computer_point is {d} and your point is {h} \n")
    elif a == "g" and b == "w":
        d = d + 1
        print(f"your guess {a} and computer guess is {b} \n")
        print("computer wins 1 point \n")
        print(f"Computer point is {d} and your point is {h} \n ")
    else:
        print("you have input wrong \n")    
    c = c + 1
    print(f"{f - c} is left out of {f} \n")   

print("Game over") 

if d > h:
    print("Computer wins and you loose")
else:
    print("you win and computer loose")
print(f"your point is {h} and computer point is {d}")    
        
        
        
    
    
    
      
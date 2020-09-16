x=1
print("Number Of Guesses Is Limited")
while (x<=9):
    guess_number = int(input("Guess the number : "))
    if guess_number<18:
        print("You Enter Smaller Number Please Enter Greater Number.\n")
    elif guess_number>18:
        print("You Enter Greater Number Please Enter Smaller Number.\n ")
    else:
        print("Conguratulations You Won\n")
        print(x,"Number Of Guesses You Took To Finish.")
        break
    print(9-x,"Number Of Guesses Left")
    x = x + 1
    
if(x>9):
    print("Game Over")

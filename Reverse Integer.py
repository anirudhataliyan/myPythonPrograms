"""
Reverse Integer

A simple program to print the reverse of the user entered integer on the console screen. The program is written in Python3 programming language. This source file is for beginners to learn into python programming, and hence the code might not look very professional level, instead it is of beginner level.

Author : Anirudha Taliyan (https://github.com/anirudhataliyan/)
Created on : September 6, 2020

Last modified by : Rishav Das (https://github.com/rdofficial/)
Last modified on : May 13, 2021

Changed made in the last modification :
1. Added the main function and put the entire source code inside it.
2. Added the conditional statements for the proper calling of the main function + error handling too at that point of the script execution.
3. Also the error catching code by which now the user has the option to exit the script anytime by pressing the CTRL+C key combination.
4. Instead of directly calculating the output, we have created a one-liner function 'reverse' that takes in a string-type variable and returns its reverse. Thus, we pass the string parsed integer to the function and get the reverse of the integer back.

Authors contributed to this script (Add your name below if you have contributed) :
1. Anirudha Taliyan (github:https://github.com/anirudhataliyan/, email:akt746083@gmail.com)
2. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

# The function which returns the inverted form of an string which is passed to it as a parameter (argument). The function takes in 1 argument : variable.
reverse = lambda variable : variable[::-1]

def main():
    # Using the while..true loop for infinite execution of the script until the user wants to exit
    while True:
        # Asking the user to enter a number
        number = int(input('Enter a number : '))
        print(f'Reverse of the number : {reverse(str(number))}')

        # Asking the user wheter to continue the loop again or not
        choice = input('\nEnter Y to do again (else to stop) : ')
        if (choice.lower() == 'y' or choice.lower() == 'yes') == False:
            # If the user entered the choice to exit, then we break the loop and exit the script

            break

if __name__ == '__main__':
    try:
        main()
        print('\n[ EXITING ]')
    except KeyboardInterrupt:
        # If the user presses the CTRL+C key combo, then we exit the script

        print('\n[ EXITING ]')
        exit()
    except Exception as e:
        # If there are errors encountered during the process, then we display the error on the console screen

        input(f'\n[ Error : {e} ]\nPress enter key to continue...')
        exit()

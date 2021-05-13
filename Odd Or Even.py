"""
Odd or Even

A python script to check wheter the user entered number is odd or even number.

Author : Anirudha Taliyan (https://github.com/anirudhataliyan/)
Created on :

Last modified by : Rishav Das (https://github.com/rdofficial/)
Last modified on : May 12, 2021

Changes made in last modification :
1. Filled the entire code inside try..except block in order to prevent any errors that may occur during the execution of the script.
2. Added commented docs as well as comment lines between the codes.

Authors contributed to this script (Add your name below if you have contributed) :
1. Anirudha Taliyan (github:https://github.com/anirudhataliyan/, email:akt746083@gmail.com)
2. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

try:
    # Asking the user to enter the number
    number = int(input('Enter a number : '))

    if (number % 2) == 0:
        # If the user entered number is even
        
        print(f'\n[ The specified number ({number}) is even ]')
    else:
        # If the user entered number is odd
        
        print(f'\n[ The specified number ({number}) is odd ]')
    input('Press enter key to continue...')
except Exception as e:
    # If there are any errors encountered during the execution, then we display the error message on the console screen
    
    input(f'\n[ Error : {e} ]\nPress enter key to continue...')
    exit()

"""
Tables

A python script to print the table for the user entered number.

Author : Anirudha Taliyan (https://github.com/anirudhataliyan/)
Created on : September 6, 2020

Last modified by : Rishav Das (https://github.com/rdofficial/)
Last modified on : May 13, 2021

Changed made in the last modification :
1. Added the main function and added the entire source code into it.
2. Put the main function call inside try..except blocks to prevent any uncertain crashing of the script whenever there are any errors encountered.
3. Added the feature for the user to exit the script by clicking key combination CTRL+C.
4. Added commented docs + added comment lines within the source code.

Authors contributed to this script (Add your name below if you have contributed) :
1. Anirudha Taliyan (github:https://github.com/anirudhataliyan/, email:akt746083@gmail.com)
2. Rishav Das (github:https://github.com/rdofficial/, email:rdofficial192@gmail.com)
"""

def main():
    # Asking the user the required input
    number = int(input('Enter the number : '))
    endpoint = int(input('Enter the endpoint of the table : '))
    
    # Displaying the table on the console screen
    print(f'\nThe table of {number} :')
    for i in range(endpoint):
        print(f'{number} x {i} = {number * i}')
       
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        # If the user presses CTRL+C key combo, then we exit the script
        
        exit()
    except Exception as e:
        # If there are any errors encountered during the process, then we display the error message on the console screen
        
        print(f'\n[ Error : {e} ]\nPress enter key to continue...')

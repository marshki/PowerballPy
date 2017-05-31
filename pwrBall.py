from __future__ import print_function
from builtins import input 

#!/usr/bin/env Python
#!/usr/bin/env Python3 
# Python 2 or 3 

""" Pseudo-random number generator for 'Powerball' lottery """

# Import Python modules 
import random                                   # for number generation 
from prettytable import PrettyTable             # for tabular formatting 

# Create table for displaying number with headers; align output to left 

table = PrettyTable(['White #s', 'Red #'])
table.align = "l"

# Define functions 

'''
Add a better try/excpet block here in line with userRuns() 
'''

def userInput():
    """ Prompt user for Y/N input """ 
    while True: 
        userChoice = str(input('Generate Powerball numbers? Y/N: ')).lower()
        if userChoice == 'y' or userChoice == 'n': 
            return userChoice  

def userRuns(): 
    """ Prompt user for number of runs """
    while True:
        try: 
            return int(input('Enter number of runs: '))
        except ValueError: 
                print('Try again')

def whiteNums(): 
    """ Generate 5 'white ball' numbers between 1 and 69--inclusive, no duplicates"""
    whites = random.sample(range(1, 69 + 1),5)  # Python range stops at y - 1 in range(x, y)
    return(', '.join(map(str, whites)))         # strip non-integer characters, separate numbers with commas 

def redNum(): 
    """ Generate 1 'red ball' number between 1 and 26--inclusive """ 
    red = random.sample(range(1, 26 + 1),1)     # Python range stops at y - 1 in range (x, y)
    return(', '.join(map(str, red)))            # as above 

def generateNums(): 
    """ Create table with Powerball numbers  """ 
    runs = userRuns()
    for int in range(runs): 
        white = whiteNums()
        red = redNum()
        table.add_row([white, red])
    return table 

def powerball(): 
    """ Guts of the program  """ 
    while True: 
        runMe = userInput() 
        if runMe == 'y': 
            generate = generateNums()
            print(generate)
            continue 
        else: 
            print('Ciao!')
            break 
            
# Let's play!

if __name__ == '__main__': 
    print("\nWelcome to the Powerball Number Generator!")
    prettyTable = powerball()


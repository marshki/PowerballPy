from __future__ import print_function
from builtins import input 

#!/usr/bin/env python

""" Pseudo-random number generator for 'Powerball' lottery """

from prettytable import PrettyTable             # for tabular formatting 
import random                                   # for number generation 

def makeTable(): 
    """ Create table for displaying number with headers; aligh output to left """ 
    table = PrettyTable(['Whites #s', 'Red #'])
    table.align = 'l'
    return table 

def userInput():
    """ Prompt user for Y/N input """ 
    while True: 
        try: 
            userChoice = str(input('Generate Powerball numbers? Y/N: ')).lower()
            if userChoice in ['y','n']: 
                return userChoice 
        except ValueError: 
            print('Try again')  

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
    
    table = makeTable()

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

if __name__ == '__main__': 
    print("Welcome to the Powerball Number Generator!")
    prettyTable = powerball()

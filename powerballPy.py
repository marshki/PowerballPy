#!/usr/bin/env python

from __future__ import print_function
from builtins import input

"""
Pseudo-random number generator for 'Powerball' lottery.
"""

from prettytable import PrettyTable             # for tabular formatting
import random                                   # for number generation

def make_table():
    """ Create table for displaying numbers with headers. Align left. """
    table = PrettyTable(['Whites #s', 'Red #'])
    table.align = 'l'
    return table

def yes_no_input():
    """ Prompt user for Y/N input. """
    while True:
        try:
            user_input = str(input('Generate Powerball numbers? Y/N: ')).lower()
            if user_input in ['y','n']:
                return user_input
        except ValueError:
            print('Try again')

def numerical_input():
    """ Prompt user for numerical input. """
    while True:
        try:
            return int(input('How many sets of Powerball numbers should we generate?: '))
        except ValueError:
                print('Try again')

def white_numbers():
    """ Generate 5 'white ball' numbers between 1 and 69--inclusive--no duplicates. """
    whites = random.sample(range(1, 69 + 1),5)  # Python range stops at y - 1 in range(x, y)
    return(', '.join(map(str, whites)))         # strip non-integer characters, separate numbers with commas

def red_number():
    """ Generate 1 'red ball' number between 1 and 26--inclusive. """
    red = random.sample(range(1, 26 + 1),1)     # As
    return(', '.join(map(str, red)))            # above

def generate_powerball_table():
    """ Create table with Powerball numbers.  """

    table = make_table()

    sets = numerical_input()

    for num in range(sets):
        white = white_numbers()
        red = red_number()
        table.add_row([white, red])
    return table

def powerball():
    """ Guts of the program  """
    while True:
        play = yes_no_input()
        if play == 'y':
            generate = generate_powerball_table()
            print(generate)
            continue
        else:
            print('Ciao!')
            break

if __name__ == '__main__':
    print("Welcome to the Powerball Number Generator!")
    prettyTable = powerball()

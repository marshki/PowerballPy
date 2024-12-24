#!/usr/bin/env python3

"""Pseudo-random number generator for 'Powerball' lottery.
"""

import argparse
import random
from prettytable import PrettyTable

def make_table():
    """Use 'PrettyTable' module to create table for output. Align left.
    """
    table = PrettyTable(['Whites #s', 'Red #'])
    table.align = 'l'
    return table

def white_numbers():
    """Generate five (5) unique 'white ball' numbers btwn. 1 and 69.
    """
    return random.sample(range(1, 69 + 1), 5)

def red_number():
    """Generate one (1) 'red ball' number between 1 and 26.
    """
    return random.sample(range(1, 26 + 1), 1)

def generate_powerball_table(num_sets):
    """Generate a table of PowerBall numbers.
    """
    table = make_table()
    for _i in range(num_sets):
        white = white_numbers()
        red = red_number()
        table.add_row([', '.join(map(str, white)), ', '.join(map(str, red))])
    return table

def main():
    """Generate PowerballPy table based on user input.
    """
    parser = argparse.ArgumentParser(description="PowerballPy Number Generator")
    parser.add_argument("-n", "--num_sets", type=int, default=1, help="Number of sets to generate")
    args = parser.parse_args()

    try:
        if args.num_sets < 1:
            raise argparse.ArgumentTypeError("Number of sets must be a positive integer.")
    except argparse.ArgumentTypeError as error:
        parser.error(str(error))

    generate = generate_powerball_table(args.num_sets)
    print(generate)

if __name__ == '__main__':
    print("Welcome to the PowerballPy Number Generator!")
    main()

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
    """Generate five (5) 'white ball' numbers btwn. 1 and 69--inclusive--no duplicates.
    Strip non-integer characters, separate numbers with commas.
    """

    whites = random.sample(range(1, 69 + 1), 5)
    return whites

def red_number():
    """Generate one (1) 'red ball' number between 1 and 26--inclusive.
    Strip non-integer characters.
    """

    red = random.sample(range(1, 26 + 1), 1)
    return red

def generate_powerball_table(num_sets):
    """Iterate through _i number of sets;
    generate 'white' & 'red' numbers;
    append to table. Add rows as needed.
    """

    table = make_table()

    for _i in range(num_sets):
        white = white_numbers()
        red = red_number()
        table.add_row([', '.join(map(str, white)), ', '.join(map(str, red))])
    return table

def main():
    """Main function.
    """

    parser = argparse.ArgumentParser(description="Powerball Number Generator")
    parser.add_argument("-n", "--num_sets", type=int, default=1, help="Number of sets to generate")

    args = parser.parse_args()

    generate = generate_powerball_table(args.num_sets)
    print(generate)

if __name__ == '__main__':
    print("Welcome to the Powerball Number Generator!")
    main()

#!/usr/bin/env python3

"""Try/except block for user input. 
Needs integration with argparse.
Probably enough to exit for invalid input.
"""

while True:
    number = input("Enter a number: ")
    try:
        value = int(number)
        if value < 1:
            print("Try again.")
            continue
        break
    except ValueError:
        print("That's not an integer.")

print(value)

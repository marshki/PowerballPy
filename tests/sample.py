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
            print("Integer must be greater than or equal to one (1).")
            continue
        break
    except ValueError:
        print("That's not an integer.")

print(value)


"""
parser = argparse.ArgumentParser(description="Powerball Number Generator")
parser.add_argument("-n", "--num_sets", type=int, default=1, help="Number of sets to generate")

args = parser.parse_args()

try:
    if args.num_sets < 1:
        raise argparse.ArgumentTypeError("Number of sets must be a positive integer.")
except argparse.ArgumentTypeError as e:
    parser.error(str(e))
""'

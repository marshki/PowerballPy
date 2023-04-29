#!/usr/bin/env python3

parser = argparse.ArgumentParser(description="Powerball Number Generator")
parser.add_argument("-n", "--num_sets", type=int, default=1, help="Number of sets to generate")

args = parser.parse_args()

try:
    if args.num_sets < 1:
        raise argparse.ArgumentTypeError("Number of sets must be a positive integer.")
except argparse.ArgumentTypeError as e:
    parser.error(str(e))

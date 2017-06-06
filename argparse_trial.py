#!/usr/bin/env python 

import argparse         # module for argument parsing 

# Arguments 

parser = argparse.ArgumentParser(description='Do magic with integers.')

# integers attribute will be a list of one or more ints 

parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')

# accumulate attribute will be either a sum or max function, per user call

parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max, 
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print args.accumulate(args.integers) 

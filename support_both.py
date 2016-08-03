#!/bin/py 
# Python 2 or 3 

"""Pseudo-random number generator for 'Powerball' lottery"""
 
#Import 'random' Python library 
import random 

#Define functions 
def white_nums():
	"""Generate 5 'white ball' numbers between 1 and 69--inclusive, no duplicates."""
	white = random.sample(range(1,69),5)
	print('Your \'white ball\' numbers are:')
	print( ', '.join(map(str, white))) 	
	print('')
() 

def red_num():
	"""Generate 1 'red ball' number between 1 and 26 (inclusive)""" 
	red = random.sample(range(1,26),1)	
	print('Your \'red ball\' number is:')
	print(', '.join(map(str, red))) 
	print('') 
()

#Prompt user for number of runs 
runs=int(input('Enter number of runs: '))

# Run program 
for n in range(runs):
	white_nums(), red_num()

#!/bin/py
# Python 2 or 3 

"""Pseudo-random number generator for 'Powerball' lottery"""
 
# Import Python modules 
import random					            # for number generation  
from prettytable import PrettyTable 		# for tabular formatting 

# Create table for displaying numbers with headers; align ouput to left 

table = PrettyTable(['White #s', 'Red #'])	
table.align = "l"

# Define functions 

def user_runs(): 
	"""Prompt user for number of runs"""
	return int(input('Enter number of runs:  '))

def white_nums():
	"""Generate 5 'white ball' numbers between 1 and 69--inclusive, no duplicates"""
	whites = random.sample(range(1, 69 + 1),5)	# Python range stops at y - 1 in range(x, y)
	return(', '.join(map(str, whites)))		# strip non-integer characters, separate numbers with commas 

def red_num():
	"""Generate 1 'red ball' number between 1 and 26--inclusive""" 
	red = random.sample(range(1, 26 + 1),1)		# Python range stops at y - 1 in range(x, y)
	return(', '.join(map(str, red)))		# strip non-integer characters, separate numbers with commas 
	
def program():
	"""Guts of the program"""
	runs = user_runs()				
	for int in range(runs):
		white = white_nums() 
		red = red_num()
		table.add_row([white, red])  		# add row to table 
	return table 

# Let's play! 		
if __name__ == '__main__': 
    print("\nWelcome to the Powerball Number Generator!\n")
    pretty_table = program()
    print(pretty_table) 
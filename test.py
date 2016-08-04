#!/bin/py 
# Python 2 or 3 

"""Pseudo-random number generator for 'Powerball' lottery"""
 
# Import 'random' Python library
 
import random 

# Define functions 

def white_nums():
	"""Generate 5 'white ball' numbers between 1 and 69--inclusive, no duplicates"""
	whites = random.sample(range(1,69),5)
	return(', '.join(map(str, whites))) 	


def red_num():
	"""Generate 1 'red ball' number between 1 and 26--inclusive""" 
	red = random.sample(range(1,26),1)	
	return(', '.join(map(str, red))) 


def user_input(): 
	"""Prompt user for number of runs, accepting only valid input"""
	return int(input('Enter number of runs:  '))

def program():
	runs = user_input()
	for int in range(runs):
		white = white_nums()
		red = red_num()
		print(white)
		print(red) 

program()

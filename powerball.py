#!/bin/py 
"""
Pseudo-random number generator
Prompt user for number of runs. 
Generate 5 'white ball' numbers between 1 and 69 (inclusive, no duplicates) 
Generate 1 'red ball' number between 1 and 26 (inclusive) 
"""

#Import 'random' Python library 
import random 

#Define functions 
def powerball_1():
	white = random.sample(range(1,69),5)
	print 'Your \'white ball\' numbers are:'
	print ', '.join(map(str, white))
() 

def powerball_2():
	red = random.sample(range(1,26),1)	
	print 'Your \'red ball\' number is:' 
	print ', '.join(map(str, red)) 
()

#Prompt user for number of runs 
#Run program 
runs=int(raw_input('Enter number of runs: '))

for n in range(runs):
	powerball_1(), powerball_2()

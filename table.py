#!/bin/bash
# table fomratting with tablulate 
from tabulate import tabulate 
import random 


print tabulate([['Ben Dover', 99, 'Flushing'], ['Seymour Butts', 21, 'Bayside']], headers=['Name', 'Age', 'Neighborhood'])

print

print tabulate([['1', '2, 3, 4, 5, 6', '7'], ['2', '8, 9, 10, 11, 12', '13']], headers=['Run #', 'White #s', 'Red #'], tablefmt='orgtbl')

print 

def white_nums():
        """Generate 5 'white ball' numbers between 1 and 69--inclusive, no duplicates"""
        whites = random.sample(range(1,69),5)
	return(', '.join(map(str, whites)))


def red_num():
        """Generate 1 'red ball' number between 1 and 26--inclusive"""
        red = random.sample(range(1,26),1)
        return(', '.join(map(str, red)))       


whitey = white_nums()
redy = red_num()

print tabulate([[whitey, redy]], headers=['White #s', 'Red #'], tablefmt='orgtbl')




 

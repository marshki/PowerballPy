#!/bin/bash
# table fomratting with tablulate 
from tabulate import tabulate 
print tabulate([['Ben Dover', 99, 'Flushing'], ['Seymour Butts', 21, 'Bayside']], headers=['Name', 'Age', 'Neighborhood'])
print tabulate([['1', '2, 3, 4, 5, 6', '7'], ['2', '8, 9, 10, 11, 12', '13']], headers=['Run #', 'White #s', 'Red #'], tablefmt='orgtbl')

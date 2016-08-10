#!/bin/bash
# table fomratting with tablulate 
from tabulate import tabulate 
print (tabulate([['Ben Dover', 99, 'Flushing'], ['Seymour Butts', 21, 'Bayside']], headers=['Name', 'Age', 'Neighborhood']))

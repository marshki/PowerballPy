# Powerball Number Generator 

Pseudo-random number generator for `Powerball Lottery` in Python 2 & 3.
`powerball_3.0.py` is the latest version of this program. 

## Requirements 

[future 0.16.0](https://pypi.python.org/pypi/future) may be installed with:`pip install future` 
[PrettyTable 0.7.2](https://pypi.python.org/pypi/PrettyTable) may be installed with:`pip install https://pypi.python.org/pypi/PrettyTable`

## Usage 

Run directly from a shell with:
 
`python powerball_3.0.py` or `python3 powerball_3.0.py`

Program generates the following set:

* 5 pseudo-random numbers between 1 and 69, inclusive (with no duplicates), and
* 1 pseudo-random number between 1 and 26, inclsuive. 

to a `PrettyTable` 

User designates the number of sets they'd like to create.

## Todo: 

- [x] Format output to a nice table.
- [x] Refactor: separation of concerns. 
- [ ] Argument parsing so you can run this directly w/out invoking script 
- [ ] Add unit tests.
- [ ] Integrate with travis-ci & landscape.io 

## History 

First commit Apr. 21, 2016 @20:23 ET. 

Unified programs for Python 2 & 3 Aug. 4, 2016.  

## License 

[MIT License](https://opensource.org/licenses/MIT). 'Nuff said.  

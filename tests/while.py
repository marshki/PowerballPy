#!/usr/bin/python

def yes_no_input():
    """Prompt user for Y/N input.
    """

    while True:
        try:
            user_input = str(input('Generate Powerball numbers? Y/N: ')).lower()
            if user_input in ['y', 'n']:
                return user_input
        except ValueError:
            print('Try again')

yes_no_input()

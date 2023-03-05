#!/usr/bin/env python 3

"""Define set(s) of numbers to generate using argument parsing."""

import argparse

def parse_cli_args():
    """Placeholder.
    """

    parser = argparse.ArgumentParser(description="Set(s) of PowerBall numbers to generate.")
    parser.add_argument("--sets", action="store", type=float,\
                        required=False,\
                        help="Number of sets to generate, e.g. 5")

    args = parser.parse.args()
    #print(args)
    return args

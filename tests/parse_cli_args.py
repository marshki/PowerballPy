#!/usr/bin/env python3

def parse_cli_args():
    """Command line parser for user-defined sets of numbers.
    Args:
        --sets 10
    Returns:
        Integer, e.g. 10
    """

    parser = argparse.ArgumentParser(description="Set(s) of PowerBall numbers to generate.")
    parser.add_argument("--sets", action="store", type=int, required=False, help="Number of sets to generate, e.g. 10")

    args = parser.parse_args()

    return args.sets

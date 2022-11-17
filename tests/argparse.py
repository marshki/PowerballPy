#!/usr/bin/env python 3

"""Place-holder.
"""


def parse_cli_args():
    """Define command line parser w/arguments.
    """
    parser = argparse.ArgumentParser(description="PowerballPy.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--", help="define n of sets to generate", nargs='+', type=float)

    args = parser.parse_args()

    if args.n_sets is None:
        parser.error("Argument required. None given.")

    return args

#!/usr/bin/python

"""Turns a command-line program into a WSGI application."""

# Insure maximum compatibility between Python 2 and 3
from __future__ import absolute_import, division, print_function

# Metadate...
__author__ = "Samuel T. Denton, III <sam.denton@dell.com>"
__contributors__ = []
__copyright__ = "Copyright 2019 Samuel T. Denton, III"
__version__ = '0.4'

# Declutter our namespace
#__all__ = ['wsgiwrapper']

# Python standard libraries
import argparse, sys

# Python site libraries

# Python personal libraries

def mk_parser():
    """Build an argument parser."""
    parser = argparse.ArgumentParser(description=__doc__)
    grp1 = parser.add_argument_group('None')
    grp1.add_argument('--none')
    grp2 = parser.add_argument_group('Enums')
    grp2.add_argument('--optional', nargs=argparse.OPTIONAL)
    grp2.add_argument('--one', nargs=argparse.ONE_OR_MORE)
    grp2.add_argument('--zero', nargs=argparse.ZERO_OR_MORE)
    grp3 = parser.add_argument_group('Integers')
    for i in 1, 2, 3:
        grp3.add_argument('--nargs%d' % i, nargs=i)
    return parser

def process(args):
    print(repr(args))

def main(argv=None):
    # Cribbed from [Python main() functions](https://www.artima.com/weblogs/viewpost.jsp?thread=4829)
    if argv is None:
        argv = sys.argv[1:]
    parser = mk_parser()
    args = parser.parse_args(argv)
    return process(args)

if __name__ == '__main__':
    sys.exit(main())

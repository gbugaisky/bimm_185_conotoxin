#!/usr/bin/env python

"""This is the main program for the conotoxin analyzer."""

import sys
from argparse import ArgumentParser
from conotoxins import procFASTA

if sys.version_info < (2, 7):
    print "This program requires Python 2.7 or newer."
    sys.exit(1)

def main(parser=None,
         passed_defaultsini=None,
         passed_personalini=None):
    if not parser:
        parser = ArgumentParser()

    parser.add_argument("sequence", help="A protein sequence.")
    parser.add_argument("-f", "--fasta", default=None, action="store_true",
        help="Provide a FASTA file rather than a protein sequence.")

    args = parser.parse_args()
    if args.fasta:
        protein = procFASTA(fASTAfile)
    else:
        protein = args.sequence

    print args
    


if __name__ == "__main__":
    main(sys.argv[1:])

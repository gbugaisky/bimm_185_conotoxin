#!/usr/bin.env python

"""This is the main program for the conotoxin analyzer."""

import sys
from optparse import OptionParser

if sys.version_info < (2, 7):
    print "This program requires Python 2.7 or newer."
    sys.exit(1)

def main(argv,
         parser=None,
         passed_defaultsini=None,
         passed_personalini=None):
    if not parser:
        parser = OptionParser("usage: %prog [options] sequence")

    parser.add_option("-f", "--fasta", default=None,
        help="Provide a FASTA file rather than a protein sequence.")

    (options, args) = parser.parse_args(argv)

    if len(args) != 1:
        parser.error("incorrect number of arguments")



if __name__ == "__main__":
    main(sys.argv[1:])

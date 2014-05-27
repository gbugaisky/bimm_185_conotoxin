#!/usr/bin/env python
import sys
import string

def CysCheck(args):
    sequence = args[0].upper()
    cys = sequence.count('C') / 2
    posit = [(i+1) for i, char in enumerate(sequence) if char == "C"]
    print "Possibility of " + str(cys) + " disulfide bridges at pos " + str(posit)

if __name__ == "__main__":
    CysCheck(sys.argv[1:])
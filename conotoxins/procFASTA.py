import os

def procFASTA(fASTAfile):
    preString = []
    with open(fASTAfile, 'r') as infile:
        for line in infile:
            if line.startswith(">"):
                continue
            preString.append(line[:-1])
    sequence = (''.join(preString))
    return sequence


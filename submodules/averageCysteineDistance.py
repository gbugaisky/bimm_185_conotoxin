#!/usr/bin/env python

"""
    averageCysteineDistance takes in a mature protein sequence in single
    letter form, and returns the average cysteine distance between all
    cysteines in that sequence.

    input:  String - legal protein sequence
    returns: int 
"""
def averageCysteineDistance(sequence):
    cysteineLocation = [i for i, ltr in enumerate(sequence) if ltr == 'C'] 
    cysteineAvg = 0.0
    for i in range(0, len(cysteineLocation) - 1):
        cysteineAvg += (cysteineLocation[i + 1] - cysteineLocation[i] + 1)
    cysteineAvg = cysteineAvg / (len(cysteineLocation) - 1)
    return cysteineAvg
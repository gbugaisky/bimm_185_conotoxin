#!usr/bin/env python
"""
    calculateMass takes in a mature protein sequence in single letter form,
    and returns the monoisotopic mass of that sequence.
"""

MONOISOTOPIC_MASS_TABLE = {
    'A': 71.03711,
    'C': 103.00919,
    'D': 115.02694,
    'E': 129.04259,
    'F': 147.06841,
    'G': 57.02146,
    'H': 137.05891,
    'I': 113.08406,
    'K': 128.09496,
    'L': 113.08406,
    'M': 131.04049,
    'N': 114.04293,
    'P': 97.05276,
    'Q': 128.05858,
    'R': 156.10111,
    'S': 87.03203,
    'T': 101.04768,
    'V': 99.06841,
    'W': 186.07931,
    'Y': 163.06333,
}


AVERAGE_MASS_TABLE = {
    'A': 71.0788,
    'R': 156.1875,
    'N': 114.1038,
    'D': 115.0886,
    'C': 103.1388,
    'E': 129.1155,
    'Q': 128.1307,
    'G': 57.0159,
    'H': 137.1411,
    'I': 113.1594,
    'L': 113.1594,
    'K': 128.1741,
    'M': 131.1926
    'F': 147.1766,
    'P': 97.1167,
    'S': 87.0782,
    'T': 101.1051,
    'W': 186.2132,
    'Y': 163.1760,
    'V': 99.1326,
}

def calculateMonoisotropicMass(sequence):
    mass = 18.01528
    upsequence = sequence.upper()
    for aa in upsequence:
        mass += MONOISOTOPIC_MASS_TABLE[aa]
    return mass

def calculateAverageMass(sequence):
    mass = 18.01528
    upsequence = sequence.upper()
    for aa in upsequence:
        mass += AVERAGE_MASS_TABLE[aa]
    return mass

def calculateMass(sequence, flag):
    if flag:
        return calculateMonoisotropicMass(sequence)
    else:
        return calculateAverageMass(sequence)


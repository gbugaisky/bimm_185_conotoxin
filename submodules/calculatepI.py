#!usr/bin/env python
"""
    calcuatepI takes in a mature protein sequence in single letter form,
    and returns the pI (Isoelectric Point) of that sequence.

    input:  String - legal protein sequence
    returns: int
"""

pKa     = {'D':3.9, 'E':4.3, 'H':6.1, 'C':8.3, 'Y':10.1, 'K':10.5, 'R':12, 'N-term':8, 'C-term':3.1}
charges = {'D':-1,  'E':-1,  'H':+1,  'C':-1,  'Y':-1,   'K':1,    'R':1,  'N-term':1, 'C-term':-1}

def calculateAminoAcidCharge(amino_acid, pH):
    ratio = 1 / (1 + 10**(pH - pKa[amino_acid]))
    
    if charges[amino_acid] == 1:
        return ratio
    else:
        return ratio - 1

def calculateProteinCharge(sequence, pH):
    protein_charge = calculateAminoAcidCharge('N-term', pH) + calculateAminoAcidCharge('C-term', pH)
    
    for amino_acid in pKa.keys():
        protein_charge += sequence.count(amino_acid) * calculateAminoAcidCharge(amino_acid, pH)

    return protein_charge

def calculateIsoelectricPoint(sequence):   
    min_pH, max_pH = 3, 13 

    while True:
        mid_pH = 0.5 * (max_pH + min_pH)
        protein_charge = calculateProteinCharge(sequence, mid_pH)
        
        if protein_charge > 0.5:
            min_pH = mid_pH
        elif protein_charge < -0.5:
            max_pH = mid_pH
        else:
            return mid_pH
#!/usr/bin/env python

from Bio.Blast import NCBIWWW, NCBIXML

def callpBLAST(sequence):
	result_handle = NCBIWWW.qblast("blastp", "nr", sequence)
	blast_record = NCBIXML.read(result_handle)
	return blast_record
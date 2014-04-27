#!/usr/bin/env python

import os
import time

from Bio.Align.Applications import ClustalOmegaCommandline

ALIGN_PATH = '\\.alignPharmFam\\'
if not os.path.exists(ALIGN_PATH):
	os.makedirs(ALIGN_PATH)

fastaFiles = os.listdir('.\\superPharmSequences\\')
for item in fastaFiles:
	print "Starting clustal omega of " + item
	clustalomega_cline = ClustalOmegaCommandline(infile=('.\\superPharmSequences\\' + item), outfile=(ALIGN_PATH + item), verbose=True, auto=True)
	print "Sleeping for 5 seconds"
	time.sleep(5)
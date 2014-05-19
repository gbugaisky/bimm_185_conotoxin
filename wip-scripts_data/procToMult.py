#!/usr/bin/env python

import tempfile
import os
import math
from sys import argv
import subprocess

def parser(filename, charstart):
	#first, get a line count to properly space the sequences
	with open("unproc\\" + filename, 'r') as counting:
		for count, l in enumerate(counting, 1):
			pass

	#set max spacing, with default of 1
	maxSpacing = 1
	while (count >= 1):
		maxSpacing += 1
		count /= 10
	print maxSpacing

	# Start processing the file
	with open("unproc\\" + filename, 'r') as inf, tempfile.NamedTemporaryFile(delete=False) as outf:
		i = 0
		for line in inf:

			# Write the file header, files mimic CLUSTAL W format
			if i is 0:
				outf.write("CLUSTAL W(1.4) multiple sequence alignment")
				outf.write('\n\n\n')
				i += 1

			if (math.log10(float(i)).is_integer()):
				maxSpacing -= 1
			#write the sequence number, followed by spaces, followed by the sequence
			outf.write(str(i))
			for idx in range(0, maxSpacing):
				outf.write(' ')
			outf.write(line[int(charstart):])
			i += 1
		outname = outf.name

	multiName = "multi\\" + os.path.splitext(filename)[0] + ".clustal"
	try:
		os.remove(multiName)
	except OSError:
		pass
	os.rename(outname, multiName)

	# Then, perform EMBOSS prophecy on the output, and save the Gribskov profile
	

if __name__ == "__main__":
	parser(argv[1], argv[2])
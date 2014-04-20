#!/usr/bin/env python

import tempfile
import os
import math
from sys import argv

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

			# Write the file header
			if i is 0:
				seqChar = len(line) - int(charstart)
				for idx in range(0, maxSpacing):
					outf.write(' ')
				outf.write('1')
				for idx in range(1, (seqChar - len(str(seqChar)))):
					outf.write(' ')
				outf.write(str(seqChar) + '\n')
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
	try:
		os.remove("multi\\temp" + filename)
	except OSError:
		pass
	os.rename(outname, "multi\\temp" + filename)

if __name__ == "__main__":
	parser(argv[1], argv[2])
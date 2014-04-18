import re

def validate_dna_string(dnastring, search=re.compile(r'[^ACGT]', re.IGNORECASE).search):
    print "Stuck at DNA validation"
    return not bool(search(dnastring))

def validate_nuc_string(nucstring, search=re.compile(r'[^GAVLIMFWPSTCYNQDEKRH]', re.IGNORECASE).search):
    print "Stuck at Nucleic Acid validation"
    return not bool(search(nucstring))
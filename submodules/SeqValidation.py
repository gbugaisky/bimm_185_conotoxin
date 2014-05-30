import re

def validate_dna_string(dnastring, search=re.compile(r'[^ACGT]', re.IGNORECASE).search):
    print "Stuck at DNA validation"
    return not bool(search(dnastring))

def validate_prot_string(protstring, search=re.compile(r'[^GAVLIMFWPSTCYNQDEKRH]', re.IGNORECASE).search):
    print "Stuck at Protein validation"
    return not bool(search(protstring))
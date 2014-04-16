import re

def validate_dna_string(dnastring, search=re.compile(r'[^ACGT]', re.IGNORECASE).search):
    print "Stuck validation"
    return not bool(search(dnastring))
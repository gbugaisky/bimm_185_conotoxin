#!/usr/bin/env python

import json
import os
from time import clock

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

def parseConotoxinXML(xmlFile):
    SEQUENCES_PATH = ".\\superPharmSequences\\"
    SEQUENCE_THRESHOLD = 4

    #create the sequence directory
    if not os.path.exists(SEQUENCES_PATH):
        os.makedirs(SEQUENCES_PATH)

    # Take the XML database and 'import' it
    start = clock()
    tree = ET.ElementTree(file=xmlFile)
    end = clock()
    print "Load time of Database: " + str(end - start)
    superCount = {}
    tree.getroot()

    # Create dictionary of all superfamilies
    for element in tree.findall('entry'):
        try:
            superfamily = element.find('pharmacologicalFamily').text
            #if 'precursor' in element.find('name').text:
            superCount[superfamily] = superCount.get(superfamily, 0) + 1
        except AttributeError:
            continue

    # This file only exists for debugging and analytic purposes
    with open('pharm_superfamily_count.txt', 'w') as supFile:
        supFile.write(json.dumps(superCount))

    # now, create the superfamily files in a pseudoFASTA format
    start = clock()
    for familyName, count in superCount.iteritems():
        if count >= SEQUENCE_THRESHOLD:
            with open(SEQUENCES_PATH + familyName +".fasta", 'w') as f:
                for element in tree.findall('entry'):
                    try:
                        superfamily = element.find('pharmacologicalFamily').text
                        if superfamily == familyName:# and 'precursor' in element.find('name').text:
                            f.write(">" + element.find('name').text.replace(' ', '_') + '\n')
                            f.write(element.find('sequence').text + '\n\n')
                    except AttributeError:
                        continue
    end = clock()
    print "Pharmacological Superfamily Files Creation Time: " + str(end - start)



if __name__ == "__main__":
    parseConotoxinXML("conoserver_protein.xml")


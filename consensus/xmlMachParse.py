#!/usr/bin/env python

import json
import os
from time import clock

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

def parseConotoxinXML(xmlFile):
    SEQUENCES_PATH = ".\\MachineParse\\"
    SEQUENCE_THRESHOLD = 9
    FEATURES = "length_cysteines_superfamily"

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
    geneSuperCount = {}

    # Create dictionary of all superfamilies
    for element in tree.findall('entry'):
        try:
            superfamily = element.find('pharmacologicalFamily').text
            #if 'precursor' in element.find('name').text:
            superCount[superfamily] = superCount.get(superfamily, 0) + 1
            superfamily = element.find('geneSuperfamily').text
            geneSuperCount[superfamily] = geneSuperCount.get(superfamily, 0) + 1

        except AttributeError:
            continue

    superMap = []
    geneMap = geneSuperCount.keys()
   
    #generate list and "map" for labels
    for familyName, count in superCount.iteritems():
        if count >= SEQUENCE_THRESHOLD:
            superMap.append(familyName)

    # This file only exists for debugging and analytic purposes
    with open(SEQUENCES_PATH + 'label&gene_count.txt', 'w') as supFile:
        supFile.write(json.dumps(superCount) + '\n' + '\n'.join(superMap) + '\n\n' + '\n'.join(geneMap))
    exit()

    # now, create the data file
    start = clock()
    with open(SEQUENCES_PATH + FEATURES + ".csv", 'w') as f:
        for element in tree.findall('entry'):
            try:
                superfamily = element.find('pharmacologicalFamily').text
                if superfamily in superMap:
                    f.write(str(len(element.find('sequence').text)) + ' ' + str(element.find('sequence').text.count('C')) + ' ' + 
                        str(superMap.index(superfamily) / float(len(superMap))) + '\n')
            except AttributeError:
                continue
    end = clock()
    print "Data File Creation Time: " + str(end - start)



if __name__ == "__main__":
    parseConotoxinXML("conoserver_protein.xml")


#!/usr/bin/env python

import traceback
import json
import os
import logging
from time import clock

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

def parseConotoxinXML(xmlFile):
    SEQUENCES_PATH = ".\\MachineParse\\"
    SEQUENCE_THRESHOLD = 9
    FEATURES = "mass_isoElectricPoint_cysAvg"
    logging.basicConfig(filename="xmlLogging.txt")

    #create the sequence directory
    if not os.path.exists(SEQUENCES_PATH):
        os.makedirs(SEQUENCES_PATH)

    # Take the XML database and 'import' it
    start = clock()
    tree = ET.ElementTree(file=xmlFile)
    #nucleicTree = ET.ElementTree(file="conoserver_nucleic.xml")
    end = clock()
    print "Load time of Database: " + str(end - start)
    superCount = {}
    tree.getroot()
    geneSuperCount = {}
    cFrameworkCount = {}

    # Create dictionary of all superfamilies
    for element in tree.findall('entry'):
        try:
            superfamily = element.find('pharmacologicalFamily').text
            #if 'precursor' in element.find('name').text:
            superCount[superfamily] = superCount.get(superfamily, 0) + 1
            superfamily = element.find('geneSuperfamily').text
            geneSuperCount[superfamily] = geneSuperCount.get(superfamily, 0) + 1
            #superfamily = element.find('cysteineFramewrok').text
            #cFrameworkCount[superfamily] = cFrameworkCount.get(superfamily, 0) + 1

        except AttributeError:
            continue

    superMap = []
    geneMap = geneSuperCount.keys()
    #cFrameMap = cFrameworkCount.keys()
   
    #generate list and "map" for labels
    for familyName, count in superCount.iteritems():
        if count >= SEQUENCE_THRESHOLD:
            superMap.append(familyName)

    # This file only exists for debugging and analytic purposes
    with open(SEQUENCES_PATH + 'label&gene_count.txt', 'w') as supFile:
        supFile.write(json.dumps(superCount) + '\n' + '\n'.join(superMap) + '\n\n' + '\n'.join(geneMap)) #+ '\n\n' + '\n'.join(cFrameMap))
    #exit()

    # now, create the data file
    start = clock()
    with open(SEQUENCES_PATH + FEATURES + ".csv", 'w') as f:
        for element in tree.findall('entry'):
            try:
                superfamily = element.find('pharmacologicalFamily').text
                if superfamily in superMap:
                    # ' ' + str(cFrameMap.index(element.find('cysteineFramewrok').text)) + 
                    sequence = element.find('sequence').text

                    # Calculate Average Distance b/w all the cysteines
                    cysLoc = [i for i, ltr in enumerate(sequence) if ltr == 'C']
                    cysAvg = 0.0
                    for i in range(0, len(cysLoc) - 1):
                        cysAvg += (cysLoc[i + 1] - cysLoc[i] + 1)
                    cysAvg = cysAvg / (len(cysLoc) - 1)
                    
                    mass = element.find('averageMass').text
                    isoElec = element.find('isoelecticPoint').text
                    f.write(mass + ' ' + isoElec + ' ' + str(cysAvg) + ' ' + str(superMap.index(superfamily)) +'\n')
                    """
                    try:
                        f.write(str(geneMap.index(element.find('geneSuperfamily').text)) + ' ' + str(cysAvg) + ' ' + 
                            str(superMap.index(superfamily)) + '\n')# / float(len(superMap))) + '\n')
                    except AttributeError:
                        f.write('-1 ' + str(cysAvg) + ' ' + str(superMap.index(superfamily)) + '\n')
                    """
            except AttributeError:
                logging.warning( traceback.format_exc() )
                continue
                
    end = clock()
    print "Data File Creation Time: " + str(end - start)



if __name__ == "__main__":
    parseConotoxinXML("conoserver_protein.xml")


#!/usr/bin/env python

from time import clock
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

def parseConotoxinXML(xmlFile):
    start = clock()
    tree = ET.ElementTree(file=xmlFile)
    end = clock()
    print "Load time of Database: " + str(end - start)
    tree.getroot()
    fileAsup = open('A_superfamily', 'w')
    for element in tree.findall('entry'):
        try:
            superfamily = element.find('geneSuperfamily').text
            if superfamily == "A superfamily" and ('precursor' in element.find('name').text):
                fileAsup.write(element.find('sequence').text + '\n')
        except AttributeError:
            continue
    #    fileAsup.write(element.tag + element.attrib + "\n")
    fileAsup.close()

if __name__ == "__main__":
    parseConotoxinXML("conoserver_protein.xml")


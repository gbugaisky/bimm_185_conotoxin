#!usr/bin/env/python
from os import path, makedirs

LABELS_TABLE = {
    0: "Delta",
    1: "Mu",
    2: "Omega",
    3: "Alpha",
    4: "Chi",
}

def parseToPharmSets(filename):
    print "Running"
    FILEPATH = ".\\SeperatePharmSets\\"
    if not path.exists(FILEPATH):
        makedirs(FILEPATH)

    conoData = [[] for i in range(5)]
    with open(filename, 'r') as data:
        for line in data:
            conoData[int(line[-2])].append(line)

    for i in LABELS_TABLE:
        with open(FILEPATH + "dataSet" + (LABELS_TABLE[i]) + ".csv", 'w') as data:
            for row in conoData[i]:
                data.write(row)
    
if __name__ == "__main__":
    parseToPharmSets(".\\MachineParse\\mass_isoElectricPoint_cysAvg.csv")
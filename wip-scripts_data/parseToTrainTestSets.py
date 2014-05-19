#!usr/bin/env/python
from os import path, makedirs

def parseToTrainTestSets(filename):
    FILEPATH = ".\\SeparatedTrainTest\\"
    if not path.exists(FILEPATH):
        makedirs(FILEPATH)

    conoData = [[] for i in range(5)]
    with open(filename, 'r') as data:
        for line in data:
            conoData[int(line[-2])].append(line)

    for i in range(0, 10):
        print i
        with open(FILEPATH + 'trainDataSet' + str(i) + '.csv', 'w') as training, open(FILEPATH + 'testDataSet' + str(i) + '.csv', 'w') as testing:
            for label in conoData:
                threshold = int(len(label) * 0.1 * i)
                threshLimit = threshold + int(len(label) * 0.1)
                if threshLimit == threshold:
                    threshLimit += 1
                for idx, row in enumerate(label):
                    if idx < threshold:
                        training.write(row)
                    elif idx >= threshold and idx < threshLimit:
                        testing.write(row)
                    else:
                        training.write(row)

if __name__ == "__main__":
    parseToTrainTestSets(".\\MachineParse\\mass_isoElectricPoint_cysAvg.csv")
#!usr/bin/env/python

def parseToTrainTestSets(filename):
	conoData = [[] for i in range(5)]
	with open(filename, 'r') as data:
		for line in data:
			conoData[int(line[-2])].append(line)

	with open('trainData.csv', 'w') as training, open('testData.csv', 'w') as testing:
		for label in conoData:
			threshold = int(len(label) * 0.9)
			print threshold
			for idx, row in enumerate(label):
				if idx < threshold:
					training.write(row)
				else:
					testing.write(row)

if __name__ == "__main__":
	parseToTrainTestSets(".\\MachineParse\\mass_isoElectricPoint_cysAvg.csv")
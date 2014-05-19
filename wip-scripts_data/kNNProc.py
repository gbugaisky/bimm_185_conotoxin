#!usr/bin/env/python

import numpy as np
import pylab as pl
from matplotlib.colors import ListedColormap
from sklearn import neighbors

def kNNGen(trainfile, testfile):
	features = np.genfromtxt(trainfile, delimiter=' ', usecols=(0, 1, 2))
	labels = np.genfromtxt(trainfile, delimiter=' ', usecols=(-1))
	tests = np.genfromtxt(testfile, delimiter=' ', usecols=(0, 1, 2))
	testlabels = np.genfromtxt(testfile, delimiter=' ', usecols=(-1))

	n_neighbors = 10

	h = 0.02
	accuracyScores = []
	for weights in ['uniform', 'distance']:
		clf = neighbors.KNeighborsClassifier(n_neighbors, leaf_size=20, weights=weights)
		clf.fit(features, labels)
		accuracyScores.append(clf.score(tests, testlabels))
	return accuracyScores

if __name__ == "__main__":
	FILEPATH = ".\\SeparatedTrainTest\\"
	accuracyVals = []
	for i in range(0, 10):
		accuracyVals.append(kNNGen(FILEPATH + "trainDataSet" + str(i) + ".csv", FILEPATH + "testDataSet" + str(i) + ".csv"))
	uniformScore = 0
	distanceScore = 0
	with open("kNNAverageAccuracy.txt", 'w') as results:
		for element in accuracyVals:
			results.write(str(element) + '\n')
			uniformScore += element[0]
			distanceScore += element[1]

		results.write("Uniform kNN Accuracy: " + str(uniformScore / 10.0) + '\n')
		results.write("Distance kNN Accuracy: " + str(distanceScore / 10.0) + '\n')
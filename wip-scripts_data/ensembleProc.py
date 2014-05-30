#!usr/bin/env/python

import numpy as np
import pylab as pl
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import zero_one_loss
from time import clock

def ensembleProc(n_estimators, learning_rate, trainfile, testfile):
	features = np.genfromtxt(trainfile, delimiter=' ', usecols=(0, 1, 2))
	labels = np.genfromtxt(trainfile, delimiter=' ', usecols=(-1))
	tests = np.genfromtxt(testfile, delimiter=' ', usecols=(0, 1, 2))
	testlabels = np.genfromtxt(testfile, delimiter=' ', usecols=(-1))

	dt_stump = DecisionTreeClassifier(max_depth=1, min_samples_leaf=1)
	dt_stump.fit(features, labels)

	ada_real = AdaBoostClassifier(
		base_estimator=dt_stump,
		learning_rate=learning_rate,
		n_estimators=n_estimators,
		algorithm="SAMME")
	ada_real.fit(features, labels)

	error = np.zeros((n_estimators,))
	for i, predict in enumerate(ada_real.staged_predict(tests)):
		error[i] = zero_one_loss(predict, testlabels)
	
	return np.mean(error)

if __name__ == "__main__":
	FILEPATH = ".\\SeparatedTrainTest\\"
	N_ESTIMATORS = [200, 225, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300, 305, 310, 315, 320, 325, 330, 335, 340, 345, 350]#[25, 50, 75, 100, 125, 150, 175, 200, 225, 250]
	LEARN_RATES = [0.001, .05, .1, .15, .2, .25, .3, .35, .4, .45, .5, .55, .6, .65, .7, .75, .8, .85, .9, .95, 1.]
	start = clock()

	with open("DiscreteAdaBoostErrorRateTo350n.txt", 'w') as results:
		for learnRate in LEARN_RATES:
			results.write("\nCurrent Learn Rate: " + str(learnRate) + "\n")
			for estimator in N_ESTIMATORS:
				errorVals = []
				for i in range(0, 10):
					errorVals.append(ensembleProc(estimator, learnRate, FILEPATH + "trainDataSet" + str(i) + ".csv", FILEPATH + "testDataSet" + str(i) + ".csv"))

				results.write("Average AdaBoost Error with " + str(estimator) + " estimators: " + str(np.mean(errorVals)) + "\n")
	print (clock() - start)
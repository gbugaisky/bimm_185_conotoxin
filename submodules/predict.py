#!/usr/bin/env python

from sklearn.ensemble import AdaBoostClassifier
from sklearn.externals import joblib

#This is a dictionary rather than an array for clarity of data, and easier changes
LABELS_TABLE = {
	0: "Delta",
	1: "Mu",
	2: "Omega",
	3: "Alpha",
	4: "Chi",
}

def predictLabel(averageMass, isoPoint, cysAvg):
	clf = joblib.load("classifier.pkl")
	result = clf.predict([averageMass, isoPoint, cysAvg])
	print result
	return LABELS_TABLE[result[0]]
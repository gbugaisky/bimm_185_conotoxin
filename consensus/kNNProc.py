#!usr/bin/env/python

import numpy as np
import pylab as pl
from matplotlib.colors import ListedColormap
from sklearn import neighbors

def kNNGen(filename):
	features = np.genfromtxt(filename, delimiter=' ', usecols=(0, 1, 2))
	labels = np.genfromtxt(filename, delimiter=' ', usecols=(-1))

	n_neighbors = 10

	h = 0.02

	for weights in ['uniform', 'distance']:
		clf = neighbors.KNeighborsClassifier(n_neighbors, leaf_size=20, weights=weights)
		clf.fit(features, labels)
		print clf.get_params(deep=True)
		print clf.score(features, labels)
		print clf.kneighbors_graph(features)

if __name__ == "__main__":
	kNNGen(".\\MachineParse\\mass_isoElectricPoint_cysAvg.csv")
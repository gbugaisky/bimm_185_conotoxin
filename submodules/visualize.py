#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

LABELS_TABLE = {
	0: "Delta",
	1: "Mu",
	2: "Omega",
	3: "Alpha",
	4: "Chi",
}
FILEPATH = ".\\data_sets\\dataSet"

def visualize(mass, iPoint, cysAvg):
	#with open(".\\MachineParse\\length_cysteines.txt", 'rb') as readIn:
	#data = np.genfromtxt(".\\mass_isoElectricPoint_cysAvg.csv", delimiter=' ', names=['x', 'y', 'z', 'label'])
	color_REF = ['#FF0000', '#0000CC', '#003300', '#E6E600', '#CC9900']

	#Initialize all data arrays with known sizes
	alpha = np.genfromtxt(FILEPATH + "alpha.csv", delimiter=' ', names=['x', 'y', 'z', 'label'])
	delta = np.genfromtxt(FILEPATH + "delta.csv", delimiter=' ', names=['x', 'y', 'z', 'label'])
	chi = np.genfromtxt(FILEPATH + "chi.csv", delimiter=' ', names=['x', 'y', 'z', 'label'])
	mu = np.genfromtxt(FILEPATH + "mu.csv", delimiter=' ', names=['x', 'y', 'z', 'label'])
	omega = np.genfromtxt(FILEPATH + "omega.csv", delimiter=' ', names=['x', 'y', 'z', 'label'])



	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	i = 0
	refList = [delta, mu, omega, alpha, chi]

	for element in refList, i in range(0,5):
		#print element
		#print color_REF[(element['label'].astype(int))]
		if isinstance(element, bool):
			continue
		for data in element:
			for j in range(0, len(data)):
				ax.plot([data[j][0]], [data[j][1]], [data[j][2]], 'o', c=color_REF[i], label=LABELS_TABLE[i], alpha=0.1)
	pointarray = [mass, iPoint, cysAvg]
	newpoint = np.asanyarray(pointarray)
	newpoint = np.reshape(newpoint, (-1, 3))
	print newpoint
	#ax.plot(newpoint[0], newpoint[1], newpoint[2], 'o', c='#FFFFFF', label="Given Point")
	#ax.plot(mass, iPoint, cysAvg, 'o', c="#FFFFFF", label="Given Point")
	ax.set_title("Feature Sets: Mass, Isoelectric Point, Average Cysteine Distance")
	ax.set_xlabel('Mass')
	ax.set_ylabel('Isoelectric Point')
	ax.set_zlabel('Average Cysteine Distance (# of Amino Acids)')

	#cbar = fig.colorbar(cax, ticks=[0, 0.2, 0.4, 0.6, 0.8, 1])
	#cbar.ax.set_yticklabels(['delta', 'mu', 'omega', 'alpha', 'chi', ''])
	plt.legend(loc='upper left', numpoints=1, ncol=3, fontsize=8, bbox_to_anchor=(0,0))

	plt.show()
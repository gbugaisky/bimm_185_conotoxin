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

def visualize(mass, iPoint, cysAvg):
	#with open(".\\MachineParse\\length_cysteines.txt", 'rb') as readIn:
	data = np.genfromtxt(".\\mass_isoElectricPoint_cysAvg.csv", delimiter=' ', names=['x', 'y', 'z', 'label'])
	color_REF = ['#FF0000', '#0000CC', '#003300', '#E6E600', '#CC9900']
	
	aleph, bet, gimmel, dalet, hey = np.zeros((0,), dtype=[('x', np.float64), ('y', np.float64), ('z', np.float64), ('label', np.float64)])

	for element in data:
		if element['label'] is 0:
			aleph = np.vstack([aleph, element])
		elif element['label'] is 1:
			bet = np.vstack([bet, element])
		elif element['label'] is 2:
			gimmel = np.vstack([gimmel, element])
		elif element['label'] is 3:
			dalet = np.vstack([dalet, element])
		else:
			hey = np.vstack([hey, element])

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	for element in enumerate(aleph, bet, gimmel, dalet, hey), i in range(0,5):
		#print element
		#print color_REF[(element['label'].astype(int))]
		#print LABELS_TABLE[(element['label'].astype(int))]
		ax.plot(element['x'], element['y'], element['z'], s=80, marker='o',
			c=color_REF[i], label=LABELS_TABLE[i], alpha=0.1)
	newPoint = np.asarray([mass, iPoint, cysAvg])
	ax.plot(newPoint[0], newPoint[1], newPoint[2], s=100, marker='o', c='#FFFFFF', label="Given Point")
	ax.set_title("Feature Sets: Mass, Isoelectric Point, Average Cysteine Distance")
	ax.set_xlabel('Mass')
	ax.set_ylabel('Isoelectric Point')
	ax.set_zlabel('Average Cysteine Distance (bp)')

	#cbar = fig.colorbar(cax, ticks=[0, 0.2, 0.4, 0.6, 0.8, 1])
	#cbar.ax.set_yticklabels(['delta', 'mu', 'omega', 'alpha', 'chi', ''])
	plt.legend(loc='upper left', numpoints=1, ncol=3, fontsize=8, bbox_to_anchor=(0,0))

	plt.show()
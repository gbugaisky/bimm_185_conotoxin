#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

def visualize(mass, iPoint, cysAvg):
	#with open(".\\MachineParse\\length_cysteines.txt", 'rb') as readIn:
	data = np.genfromtxt(".\\mass_isoElectricPoint_cysAvg.csv", delimiter=' ', names=['x', 'y', 'z', 'label'])
	color_REF = ['#FF0000', '#0000CC', '#003300', '#E6E600', '#CC9900']

	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	for element in data:
		#print element
		#print color_REF[(element['label'].astype(int))]
		ax.scatter(element['x'], element['y'], element['z'], s=80, c=color_REF[(element['label'].astype(int))], alpha=0.1)
	ax.scatter(mass, iPoint, cysAvg, s=100, c='#FFFFFF')
	ax.set_title("Feature Sets: Mass, Isoelectric Point, Average Cysteine Distance")
	ax.set_xlabel('Mass')
	ax.set_ylabel('Isoelectric Point')
	ax.set_zlabel('Average Cysteine Distance (bp)')

	#cbar = fig.colorbar(cax, ticks=[0, 0.2, 0.4, 0.6, 0.8, 1])
	#cbar.ax.set_yticklabels(['delta', 'mu', 'omega', 'alpha', 'chi', ''])

	plt.show()
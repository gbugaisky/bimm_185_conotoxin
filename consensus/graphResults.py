#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#with open(".\\MachineParse\\length_cysteines.txt", 'rb') as readIn:
data = np.genfromtxt(".\\MachineParse\\cysCount_avgCdist.csv", delimiter=' ', names=['x', 'y', 'label'])
color_REF = ['#FF0000', '#0000CC', '#003300', '#E6E600', '#CC9900']


fig, ax = plt.subplots()

for element in data:
	ax.scatter(element['x'], element['y'], s=80, c=color_REF[(element['label'].astype(int))], alpha=0.1)
ax.set_title("Feature Sets: Cys Distance and # of Cysteines")
ax.set_xlabel('Cysteine Count')
ax.set_ylabel('Cysteine Distance')

#cbar = fig.colorbar(cax, ticks=[0, 0.2, 0.4, 0.6, 0.8, 1])
#cbar.ax.set_yticklabels(['delta', 'mu', 'omega', 'alpha', 'chi', ''])

plt.show()
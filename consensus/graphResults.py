#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

#with open(".\\MachineParse\\length_cysteines.txt", 'rb') as readIn:
data = np.genfromtxt(".\\MachineParse\\superfamily_cFrame_cysteines.csv", delimiter=' ', names=['x', 'y', 'z', 'label'])
print data['label']
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

cax = ax.scatter(data['x'], data['y'], data['z'], c=data['label'], cmap=cm.gist_rainbow)

ax.set_title("Feature Sets: Mapped Superfamily, Mapped Cysteine Framework, and # of Cysteines")
ax.set_xlabel('Mapped Superfamily')
ax.set_ylabel('Mapped Cysteine Framework')
ax.set_zlabel('Cysteine Count')

cbar = fig.colorbar(cax, ticks=[0, 0.2, 0.4, 0.6, 0.8, 1])
cbar.ax.set_yticklabels(['delta', 'mu', 'omega', 'alpha', 'chi', ''])

plt.show()
#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#with open(".\\MachineParse\\length_cysteines.txt", 'rb') as readIn:
data = np.genfromtxt(".\\MachineParse\\length_cysteines.csv", delimiter=' ', names=['x', 'y', 'label'])

fig, ax = plt.subplots()

cax = ax.scatter(data['x'], data['y'], s=80, c=data['label'], cmap=cm.gist_rainbow)
ax.set_title("Feature Sets: Sequence Length and # of Cysteines")
ax.set_xlabel('Sequence Length')
ax.set_ylabel('Cysteine Count')

cbar = fig.colorbar(cax, ticks=[0, 0.2, 0.4, 0.6, 0.8, 1])
cbar.ax.set_yticklabels(['delta', 'mu', 'omega', 'alpha', 'chi', ''])

plt.show()
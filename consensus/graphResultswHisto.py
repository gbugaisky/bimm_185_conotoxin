#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.axes_grid1 import make_axes_locatable

# For 3D figures
# data = np.genfromtxt(".\\MachineParse\\superfamily_cFrame_cysteines.csv", delimiter=' ', names=['x', 'y', 'z', 'label'])

# For 2D figures
data = np.genfromtxt(".\\MachineParse\\superfamily_cysteines_v2.csv", delimiter=' ', names=['x', 'y', 'label'])
color_REF = ['#FF0000', '#0000CC', '#003300', '#E6E600', '#CC9900']
xVals = data['x'].tolist()
yVals = data['y'].tolist()
labels = data['label'].astype(int).tolist()

# Quick Sanity Check
if (len(xVals) != len(yVals)) or (len(xVals) != len(labels)):
	print "Error in .csv file setup.  Use xmlMachParse.py for gen."
	exit()

fig = plt.figure()

# For 3D Figures
# ax = fig.add_subplot(111, projection='3d')
# cax = ax.scatter(data['x'], data['y'], data['z'], c=data['label'], cmap=cm.gist_rainbow)


axscatter = fig.add_subplot(111)
# For 2D Figures

colors = []
for index in xrange(0, len(xVals)):
	color = color_REF[labels[index]]
	axscatter.scatter(xVals[index], yVals[index], s=80, c=color, edgecolors='none', alpha=0.3)
	colors.append(color)

axscatter.set_title("Feature Sets: Mapped Superfamily and # of Cysteines")
axscatter.set_xlabel('Mapped Superfamily')
axscatter.set_ylabel('Cysteine Count')
axscatter.set_aspect(1.)

# Set up histograms
divider = make_axes_locatable(axscatter)
axhistX = divider.append_axes("top", 1.2, pad=0.5, sharex=axscatter)
axhistY = divider.append_axes("right", 1.2, pad=0.5, sharey=axscatter)
plt.setp(axhistX.get_xticklabels() + axhistY.get_yticklabels(), visible=False)

bin_W = 0.2
bins = np.arange(0, bin_W, bin_W)
histtype = 'bar'
axhistX.hist(xVals, bins=bins, histtype=histtype, color=color_REF)
axhistY.hist(yVals, bins=bins, orientation=horizontal, histtype=histtype, color=color_REF)

# cbar = fig.colorbar(cax, ticks=[0, 0.2, 0.4, 0.6, 0.8, 1])
# cbar.ax.set_yticklabels(['delta', 'mu', 'omega', 'alpha', 'chi', ''])

plt.draw()
plt.show()
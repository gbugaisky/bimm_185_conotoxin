#!usr/bin/env python

import os
import numpy as np
import pylab as pl
from sklearn import svm

def linearSvcProc(filename):
    #features = np.zeroes(shape=(250,3))
    #labels = np.zeroes(shape=(250,1))
    h = 0.02
    C =1.0
    #with open(filename, 'r') as procFile:
    #    for line in procFile:
    #            features.appen

    features = np.genfromtxt(filename, dtype=int, delimiter=' ', usecols=(0, 1))
    labels = np.genfromtxt(filename, dtype=int, delimiter=' ', usecols=(-1))
    svc = svm.SVC(kernel='linear', C=C).fit(features, labels)
    rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(features, labels)
    poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(features, labels)
    lin_svc = svm.LinearSVC(C=C).fit(features, labels)
    x_min, x_max = features[:, 0].min() - 1, features[:, 0].max() + 1
    y_min, y_max = features[:, 1].min() - 1, features[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    titles = ['SVC with linear kernel',
          'SVC with RBF kernel',
          'SVC with polynomial (degree 3) kernel',
          'LinearSVC (linear kernel)']

    for i, clf in enumerate((svc, rbf_svc, poly_svc, lin_svc)):
        pl.subplot(2, 2, i + 1)
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

        Z = Z.reshape(xx.shape)
        pl.contourf(xx, yy, Z, cmap=pl.cm.Paired)
        pl.scatter(features[:, 0], features[:, 1], c=labels, cmap=pl.cm.Paired)
        pl.title(titles[i])

    pl.show()

if __name__ == "__main__":
    linearSvcProc(".\\MachineParse\\mass_isoElectricPoint_cysAvg.csv")
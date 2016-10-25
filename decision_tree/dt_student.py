#!/usr/bin/python

def classify(features_train, labels_train):
    from sklearn import tree
    clf = tree.DecisionTreeClassifier(min_samples_split=100)
    clf.fit(features_train, labels_train)

    return clf


import sys
sys.path.append("../tools/")
from picture_tool import pretty_picture, output_image
from terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = makeTerrainData()

### classify
clf = classify(features_train, labels_train)

### measure the accuracy
from sklearn.metrics import accuracy_score
pred = clf.predict(features_test)
print 'Accuract of DT is ', accuracy_score(pred, labels_test)

### plot the prediction and save in test.png file
pretty_picture(clf, features_test, labels_test)
plt.show()

#!/usr/bin/python

"""
    Use Support Vector Machine (SVM) to identify emails by their authors

    Authors and labels:
    Sara has label 0
    Chris has label 1
"""
import sys
sys.path.append("../tools/")
from email_preprocess import preprocess

### pre processing the data
features_train, features_test, labels_train, labels_test = preprocess()

### fit the classifier
from sklearn.svm import SVC
clf = SVC(kernel='rbf', C = 100)
clf.fit(features_train, labels_train)

### predict
pred = clf.predict(features_test)
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print ("Accuracy of SVM is", acc)





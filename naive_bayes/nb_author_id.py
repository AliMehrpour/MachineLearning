#!/usr/bin/python

"""
    Use Naive Bayes classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1

"""
import sys
sys.path.append("../tools/")
from email_preprocess import preprocess

### get the features and labels for training and testing
features_train, features_test, labels_train, labels_test = preprocess()


### traning
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(features_train, labels_train)


### prediction
pred = clf.predict(features_test)
print pred


### calculate accuracy
from sklearn.metrics import accuracy_score
print "Accuracy of NB is ", accuracy_score(pred, labels_test)

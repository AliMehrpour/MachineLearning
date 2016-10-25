#!/usr/bin/python

import sys
sys.path.append("../tools/")
from email_preprocess import preprocess

### prepare the dataset
features_train, features_test, labels_train, labels_test = preprocess()

### print features info
print '# features: ', len(features_train[0])

### train the classifier
from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split=40)
clf.fit(features_train, labels_train)

### predict
pred = clf.predict(features_test)

### measure accuracy
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print 'Accuracy is ', acc


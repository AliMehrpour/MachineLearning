#!/usr/bin/python

from sklearn.datasets import load_iris
from sklearn import tree


### import iris dataset
iris = load_iris()
print 'feature_names : ', iris.feature_names
print 'target_names : ', iris.target_names
for i in range(len(iris.target)):
    print 'Example %d, features %s, label %s' % (i, iris.data[i], iris.target[i])


### prepare tarin and test data
import numpy as np
test_idx = [0, 50, 100]


train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)


test_target = iris.target[test_idx]
test_data = iris.data[test_idx]


### train classifier
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)


### predict
print test_target
print clf.predict(test_data)


### visualize code
"""
from IPython.display import Image
dot_data = tree.export_graphviz(clf, out_file = None,
                         feature_names = iris.feature_names,
                         class_names = iris.target_names,
                         filled = True, rounded = True,
                         special_characters = True)
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())
"""

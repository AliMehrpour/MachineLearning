# import dataset
from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)


# decision tree classifier
from sklearn import tree
clf_dt = tree.DecisionTreeClassifier()
clf_dt.fit(X_train, y_train)

print 'Decision Tree'
pred = clf_dt.predict(X_test)
print pred

# calculate the accuracy
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, y_test)
print "Accuracy is ", acc
print


# k neighbors classifier
from sklearn.neighbors import KNeighborsClassifier
clf_knc = KNeighborsClassifier()
clf_knc.fit(X_train, y_train)

print 'K Neighbors Classifier'
pred = clf_knc.predict(X_test)
print pred

# calculate the accuracy
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, y_test)
print "Accuracy is ", acc

# My own classifier
from scipy.spatial import distance
def euc(a,b):
    return distance.euclidean(a, b)

class ScrappyKNN():
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        preds = []
        for row in X_test:
            label = self.closest(row)
            preds.append(label)

        return preds

    def closest(self, row):
        best_dist = euc(row, self.X_train[0])
        best_index = 0;
        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.y_train[best_index]


clf_knn = ScrappyKNN()
clf_knn.fit(X_train, y_train)

print 'ScappyKNN Classifier'
pred = clf_knn.predict(X_test)
print pred

# calculate the accuracy
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, y_test)
print "Accuracy is ", acc


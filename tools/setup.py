#!/usr/bin/python

# Check all needed libraries are installed correctly or now

print
print "Checking for nltk - Natural Language Toolkie(http://www.nltk.org/)"
try:
    import nltk
    print "nltk is installed"
except ImportError:
    print 'You should install nltk before continuing'

print
print "Checking for numpy"
try:
    import numpy
    print "numpy is installed"
except ImportError:
    print 'You should install numpy before continuing'

print
print "Checking for scipy"
try:
    import scipy
    print "scipy is installed"
except ImportError:
    print 'You should install scipy before continuing'

print
print "Checking for sklearn"
try:
    import sklearn
    print "sklearn is installed"
except ImportError:
    print 'You should install sklearn before continuing'

print
print "downloading the Enron dataset (this may take a while)"
print "to check on progress, you can cd up one level, then execute <ls -lthr>"
print "Enron dataset should be last item on the list, along with its current size"
print "download will complete at about 423 MB"
import urllib
url = "https://www.cs.cmu.edu/~./enron/enron_mail_20150507.tgz"
urllib.urlretrieve(url, filename="../enron_mail_20150507.tgz")
print "download complete!"


print
print "unzipping Enron dataset (this may take a while)"
import tarfile
import os
os.chdir("..")
tfile = tarfile.open("enron_mail_20150507.tgz", "r:gz")
tfile.extractall(".")

print "you're ready to go!"

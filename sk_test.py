import logging
import numpy as np
from optparse import OptionParser
import sys
from time import time
import pylab as pl


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB

from sklearn.svm import LinearSVC


input_file = open("test_training.txt", "r")
input_target_file = open("test_target.txt", "r")


'''
data = []
target = []

for line in input_file:
    data.append(line)
    
for line in input_target_file:
    line = line.strip("\n")
    target.append(int(line))
    
print "got all data"
'''

data = np.array([['1'],['2'],['3'],['4'],['3'],['6'],['4'],['2'],['5']])
target = [0,1,0,1,0,1,1,1,0]





    


new_data =['i love my girlfriend', ' i hate my boss', 'i had sushi for brekfast']

'''
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(data)
tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)


X_train_tf = tf_transformer.transform(X_train_counts)
'''


target = np.float64(target)

print target

svm = LinearSVC().fit(data, target)
#clf = MultinomialNB().fit(X_train_tf, target)

X_new_counts = count_vect.transform(new_data)
X_new_tf = tf_transformer.transform(X_new_counts)

predicted = svm.predict(X_new_tf)

print "predicted", predicted




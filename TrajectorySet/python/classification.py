# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:24:22 2016

@author: matsui
"""
import pickle
import numpy as np
from sklearn import preprocessing

with open('../result/10fisher_dict.pickle', 'r') as f:
    A = pickle.load(f)#train test reverse

max_abs_scaler = preprocessing.MaxAbsScaler()

lis_name = []
lis_value =[]
for k, v in sorted(A.items()):
    lis_name.append(k)
    v_mas = max_abs_scaler.fit_transform(v)
    lis_value.append(v_mas) 

y = np.array([0]*lis_value[0].shape[0])
X = lis_value[0]

for i in range(len(lis_value)-1):
    y = np.hstack((y, np.array([i+1]*lis_value[i+1].shape[0])))
    X = np.vstack((X, lis_value[i+1]))

print(lis_name)
np.save("../result/X_class.npy", X)
np.save("../result/y_class.npy", y)

"""
z = np.loadtxt("../result/10fisher_group.txt")

from sklearn.svm import SVC, LinearSVC


from sklearn.neural_network import MLPClassifier

g = open("../10sort.txt",'w')

from sklearn.model_selection import LeaveOneGroupOut
lol = LeaveOneGroupOut()

scores = []
for train_index, test_index in lol.split(X, y, z):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    clf = MLPClassifier()
    clf.fit(X_train, y_train)
    
    score = clf.score(X_test, y_test)
    print(score)
    g.write(str(score))
    g.write("\n")
    scores.append(score)

scores = np.array(scores)
print(scores.mean())
g.write("\n"+"mean"+"\n" +str(scores.mean()))

g.close()"""
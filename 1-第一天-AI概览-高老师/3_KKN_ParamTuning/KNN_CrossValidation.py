"""
Please note, this code is only for python 3+. If you are using python 2+, please modify the code accordingly.
"""
#coding: UTF-8
#Definiation of COLs:
#1. sepal length in cm
#2. sepal width in cm
#3. petal length in cm
#4. petal width in cm
#5. class:
#      -- Iris Setosa
#      -- Iris Versicolour
#      -- Iris Virginica
#Missing Attribute Values: None

from __future__ import print_function
from sklearn.datasets import load_iris
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import PolynomialFeatures
from sklearn.cross_validation import cross_val_score
import matplotlib.pyplot as plt

iris = load_iris()
X = iris.data
y = iris.target

k_range = range(1, 31)
k_scores = []

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X, y, cv=3, scoring='accuracy') # for classification
    k_scores.append(scores.mean())

plt.plot(k_range, k_scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Cross-Validated Accuracy')
plt.show()














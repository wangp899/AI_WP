import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsClassifier


def feature_engineer(i):
    #return np.array([i])
    #return np.array([i % 3, i % 5, i % 15])
    return np.array([i % 3, i % 5])
    #return np.array([i % 3])


def construct_sample_label(i):
    if i % 15 == 0: return np.array([3])
    elif i % 5 == 0: return np.array([2])
    elif i % 3 == 0: return np.array([1])
    else: return np.array([0])


max_train_num = 1100
x_train = np.array([feature_engineer(i) for i in range(101, max_train_num)])
y_train = np.array(
    [construct_sample_label(i) for i in range(101, max_train_num)])

x_test = np.array([feature_engineer(i) for i in range(1, 100)])
y_test = np.array([construct_sample_label(i) for i in range(1, 100)])

knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(x_train, y_train)

print('knn train score: %f' % knn.score(x_train, y_train))
print('knn test score: %f' % knn.score(x_test, y_test))

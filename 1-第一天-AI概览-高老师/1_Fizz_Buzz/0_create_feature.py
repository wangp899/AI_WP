import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error


def feature_engineer(i):
    #return np.array([i])
    return np.array([i % 3, i % 5, i % 15])
    #return np.array([i % 3, i % 5])


def construct_sample_label(i):
    if i % 15 == 0: return np.array([3])
    elif i % 5 == 0: return np.array([2])
    elif i % 3 == 0: return np.array([1])
    else: return np.array([0])


x_train = np.array([feature_engineer(i) for i in range(101, 200)])
y_train = np.array([construct_sample_label(i) for i in range(101, 200)])

x_test = np.array([feature_engineer(i) for i in range(1, 100)])
y_test = np.array([construct_sample_label(i) for i in range(1, 100)])

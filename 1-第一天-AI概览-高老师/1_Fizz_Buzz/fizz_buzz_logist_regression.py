import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsClassifier


def feature_engineer(i):
    #return np.array([i])
    return np.array([i % 3, i % 5, i % 15])
    #return np.array([i % 3])


def construct_sample_label(i):
    if i % 15 == 0: return np.array([3])
    elif i % 5 == 0: return np.array([2])
    elif i % 3 == 0: return np.array([1])
    else: return np.array([0])


x_train = np.array([feature_engineer(i) for i in range(101, 200)])
y_train = np.array([construct_sample_label(i) for i in range(101, 200)])

x_test = np.array([feature_engineer(i) for i in range(1, 100)])
y_test = np.array([construct_sample_label(i) for i in range(1, 100)])

logistic = linear_model.LogisticRegression(C=0.1)  # 内存创建了 y = f(AX)
logistic.fit(x_train, y_train)  # 训练f，找A

print('LogisticRegression train score: %f' % logistic.score(x_train, y_train))
print('LogisticRegression test score: %f' % logistic.score(x_test, y_test))

print(
    logistic.predict(
        [feature_engineer(231),
         feature_engineer(232),
         feature_engineer(101)]))


def out_transfer(i, origin):
    if i == 3: return "fizz_buzz"
    elif i == 2: return "buzz"
    elif i == 1: return "fizz"
    else: return str(origin)


num = 7
print(out_transfer(logistic.predict([feature_engineer(num)]), num))

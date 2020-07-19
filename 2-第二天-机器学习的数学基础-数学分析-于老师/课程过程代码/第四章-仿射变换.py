import numpy as np  
import matplotlib.pyplot as plt   

X = np.random.random([1000, 2]) 
# 空间拉伸
W1 = np.array([[0.5, 0], 
               [0.0, 2]]) # |W|=1
X1 = X @ W1 # 如果+b就是空间平移 
# 空间旋转
o = np.pi/4
W2 = np.array([[np.cos(o), np.sin(o)], [-np.sin(o), np.cos(o)]]) #|w|=1
X2 = X @ W2
# 旋转和拉伸
W3 = W2 @ W1 @ W2.T 
X3 = X @ W3 
plt.scatter(X[:, 0], X[:, 1]) 
plt.scatter(X1[:, 0], X1[:, 1]) 
plt.scatter(X2[:, 0], X2[:, 1])
plt.scatter(X3[:, 0], X3[:, 1])
plt.axis("equal")#横纵坐标等长
plt.show()
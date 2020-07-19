import numpy as np  
import matplotlib.pyplot as plt  
def Cov(x1, x2):
    """协方差"""
    return np.mean((x1-np.mean(x1))*(x2-np.mean(x2)))
def rho(x1, x2):
    """线性相关系数""" 
    return Cov(x1, x2)/np.std(x1)/np.std(x2)
x = np.random.normal(0, 1, [1000]) 
y1 = np.random.normal(0, 1, [1000])  
y2 = -3 * x + 1 + np.random.normal(0, 0.3, [1000]) 
print(Cov(x, y1), Cov(x, y2), rho(x, y1), rho(x, y2))
plt.scatter(x, y1, c="r") 
plt.scatter(x, y2, c="b")
plt.show()
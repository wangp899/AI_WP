import numpy as np 
import matplotlib.pyplot as plt 

x = np.random.normal(0, 1, [1000]) 
y = x ** 2 + x + np.random.normal(0, 0.3, [1000]) 

# x,y是数据，样本点
plt.scatter(x, y) 
plt.show()
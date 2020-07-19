import numpy as np  
import matplotlib.pyplot as plt  
def Normal(x, mu, std):
    """正态分布"""
    return 1/(2*np.pi*std) * np.exp(-(x-mu)**2/(2*std**2))


x1 = np.random.normal(1, 1, [2000])

x = np.linspace(-2, 4, 1000) 
p = Normal(x, 1, 1)
# 统计结果，统计的概率分布
plt.hist(x1, color="#ff0000", bins=36, density=True, alpha=0.5)
# 理论计算结果 
plt.plot(x, p, lw=2, c="r", alpha=0.5)
plt.show()
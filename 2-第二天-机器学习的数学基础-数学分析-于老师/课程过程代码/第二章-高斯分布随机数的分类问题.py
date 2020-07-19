import numpy as np  
import matplotlib.pyplot as plt  
def Normal(x, mu, std):
    """正态分布"""
    return 1/(np.sqrt(2*np.pi)*std) * np.exp(-(x-mu)**2/(2*std**2))

# 第一类样本
x1 = np.random.normal(3, 1, [2000])
# 第二类样本
x2 = np.random.normal(-1, 1.5, [2000])
x2 = np.random.random([2000])
######################仅知道x1,x2取值############################3
# 问题，如果一个数字x0=1，此时他是属于哪一类的？ 
## 思路1：统计一下属于哪一类概率比较高。绘制柱状图。 
plt.hist(x1, color="#ff0000", bins=36, normed=True, alpha=0.5, label="class 1")
plt.hist(x2, color="#0000ff", bins=36, density=True, alpha=0.5, label="class 1")
plt.show()
## 通过观察发现，蓝色概率比较高。

## 思路2：假设高斯分布，求解参数 
mu1 = np.mean(x1) 
std1 = np.std(x1)
mu2 = np.mean(x2) 
std2 = np.std(x2)
x = np.linspace(-4, 6, 1000) 
p1 = Normal(x, mu1, std1) 
p2 = Normal(x, mu2, std2) 

plt.plot(x, p1, c="r", lw=2) 
plt.plot(x, p2, c="b", lw=2)
plt.hist(x1, color="#ff0000", bins=36, normed=True, alpha=0.5, label="class 1")
plt.hist(x2, color="#0000ff", bins=36, normed=True, alpha=0.5, label="class 1")
plt.legend()
plt.show()
## 通过计算模型可以估计属于哪一类

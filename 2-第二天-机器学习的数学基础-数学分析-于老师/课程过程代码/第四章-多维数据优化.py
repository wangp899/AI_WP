import numpy as np 
import matplotlib.pyplot as plt 
######### 产生的测试数据，不带有任何含义
files = np.load("data.npz") 
x = files["x"] 
d = files["d"]

x2d = np.zeros([1000, 3]) 
x2d[:, 0] = x**1 
x2d[:, 1] = x**2
x2d[:, 2] = x**3

# 构建模型 
def model(x, w, b):
    return x @ w + b 
def grad(x, d, w, b):
    y = model(x, w, b) 
    dLdy = 2*(y-d) 
    dLdw = w.T @ dLdy/len(x) # \partial L /partial w 
    dLdb = np.sum(dLdy, axis=0)/len(x)
# x,d是数据，样本点
w = np.random.normal(0, 1, [3, 1]) # 初始值，一般是随机数
b = 0
eta = 0.05 # 学习率，超参数之一
batch_size = 32 # 批尺寸，超参数之一
for step in range(1000): 
    idx = np.random.randint(0, 1000, [batch_size]) 
    xin = x[idx] # 随机选择样本
    din = d[idx] # 随机选择标签 
    dw, db = grad(xin, din, w, b) 
    w = w - eta * dw 
    b = b - eta * db 
    print(step, L(x, d, w, b)) 

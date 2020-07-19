import numpy as np 

A = np.random.normal(0, 1, [2, 2])
B = np.random.normal(0, 1, [2, 2]) 
np.savez("AB.npz", A=A, B=B) # 变量保存 

C = np.dot(A, B)# 传统方式 
C = A @ B # 新版本Python和numpy支持。

# 使用矩阵组织数据，对于最小二乘法2例子中，数据有1000条，使用了[x,x^2]进行拟合。 
# 所示数据可以表示为X[1000, 2]
def f(x):
    """定义函数"""
    return x ** 2 + 2 * x  
def gradf(x):
    """导数""" 
    return 2 * x + 2 

x0 = 0 # 初始值
eta = 1e-4 #学习率
for step in range(20):
    g = gradf(x0)
    # 减去梯度（导数）方向 
    x0 = x0 - eta * g 
    print(f"Setp:{step}, {x0}, {f(x0)}")
    # 2.x, 3.3-3.5 "{}{}".format(x1, x2)
    # c            "%f %f"%(x1, x2)
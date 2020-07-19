def f(x1, x2):
    """定义函数"""
    return x1 ** 2 + 2 * x1 + x2 ** 2 + x2 
def gradf(x1, x2):
    return 2 * x1 + 2, 2 * x2 + 1 

x1, x2 = 0, 0 # 初始值 
eta = 0.3 # 学习率 
for step in range(200):
    g1, g2 = gradf(x1, x2)
    # 减去梯度（导数）方向 
    x1 = x1 - eta * g1 
    x2 = x2 - eta * g2  
    print(f"Setp:{step}, {(x1, x2)}, {f(x1, x2)}")
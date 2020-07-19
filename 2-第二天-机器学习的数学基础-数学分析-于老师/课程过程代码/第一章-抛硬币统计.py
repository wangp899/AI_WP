import numpy as np  
import matplotlib.pyplot as plt  

coin = np.random.randint(0, 2, [10000]) 

print(f"Mean:{np.mean(coin)}, 标准差：{np.std(coin)}") 

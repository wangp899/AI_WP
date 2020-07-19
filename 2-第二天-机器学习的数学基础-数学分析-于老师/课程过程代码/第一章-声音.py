"""
信号滤波演示
"""
import wave 
import numpy as np 
import scipy.signal as signal
import matplotlib.pyplot as plt 
x = np.linspace(0, 2*np.pi, 20000) 
y = np.sin(x * 500) + np.random.normal(0, 0.3, [20000])
plt.plot(x, y)
plt.show()
y = signal.convolve(y, np.ones(50)/50, mode="valid")
plt.plot(y)
plt.show()
y *= 1000
y = y.astype(np.int16)
files = wave.open("test.wav", "wb") 
files.setnchannels(1) 
files.setsampwidth(2)
files.setframerate(10000) 
files.writeframes(y.tostring()) 
files.close
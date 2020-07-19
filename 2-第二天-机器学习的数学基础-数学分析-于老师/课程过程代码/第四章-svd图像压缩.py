import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np 
import matplotlib.pyplot as plt
img = mpimg.imread('img/jin.jpg')
img = img[:, :, :]/255 
# 灰度化
a1, a2, a3 = 0.2989, 0.5870, 0.1140
img_gray = img[:,:,0]*a1+img[:,:,1]*a2+img[:,:,2]*a3 
# 奇异值分解 
from numpy import linalg as LA
M, Q, N = np.linalg.svd(img_gray, full_matrices=True)
Q=np.diag(Q)
re_img=M[:, :50] @ Q[:50, :50] @ N[:50, :]
plt.imshow(np.real(re_img), cmap=plt.get_cmap("gray"))
plt.show()
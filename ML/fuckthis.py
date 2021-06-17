import numpy as np
import scipy.stats as tiger
import matplotlib.pyplot as plt

x = np.arange(-3,3,0.01)
y = tiger.norm.pdf(x, 0, 1)

plt.plot(x,y)
plt.show()

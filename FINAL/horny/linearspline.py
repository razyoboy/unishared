import numpy as np
import matplotlib.pyplot as plt

x = np.array([2,3,4])
y = np.array([0.2239, -0.2601, -0.3971])
z = np.zeros(len(y)-1)
m = np.zeros(len(y)-1)

m[0] = (y[1] - y[0])/(x[1]-x[0])
m[1] = (y[2] - y[1])/(x[2]-x[1])

def cal(h):
    z = y[1] +m[1]*(h-x[1])   #use m[1] 'cuz 3.2 is between 3 and 4 in which the slope of linear graph is m[1]
    return z


a = cal(3.2)
print(m)
print(a)
plt.plot(x,y)
plt.show()
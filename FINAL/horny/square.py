import matplotlib.pyplot as plt
import numpy as np

x = np.array([2,3,4])
y = np.array([0.2239, -0.2601, -0.3971])
z = np.arange(2,4.1,0.1)
w = np.array([z])
def equa(x,y):
    c0 = y[0]
    c1 = (y[1]-y[0])/(x[1]-x[0])
    c2 = ((y[2]-y[1])/(x[2]-x[1])-c1)/(x[2]-x[0])

    return c0,c1,c2, x


c0,c1,c2,x = equa(x,y)
def squa(d):
    f = c0 + c1*(d-x[0])+c2*(d-x[0])*(d-x[1])
    return f

f = squa(z)
print(z)
print(f)


plt.scatter(x,y)
plt.plot(x,y)
plt.scatter(z,f)
plt.plot(z,f)
plt.show()
    

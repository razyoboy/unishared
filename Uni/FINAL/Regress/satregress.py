import numpy as np
import matplotlib.pyplot as plt

xbar = np.array([1,2,3,4,5])
ybar = np.array([0.1,0.7,0.9,1.7,2.1])

n = len(xbar)
x = 1/xbar; sumx = sum(x)
y = 1/ybar; sumy = sum(y)
xsq = np.square(x); sumxsq = np.sum(xsq)
xy = x*y; sumxy = np.sum(xy)

a = np.array([[n, sumx], [sumx, sumxsq]])
bx = np.array([[sumy],[sumxy]])
res = np.linalg.solve(a,bx)
rawa0 = res[0]; a1 = res[1]
a0 = 1/rawa0;  b = a1*a0
r = np.arange(-3,6,0.01)
eqn = (a0*r)/(b+r)

print(f"Calculated a0 is {a0} and a1 of {b}")
print(f"-> f(x) = {a0}x / {b} + x")

plt.plot(r,eqn)
plt.scatter(xbar,ybar, color='g')
plt.legend(['Regressed f(x)','Data Points'])
plt.title('Saturated Growth Rate Regressed Fitted Line')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#github.com/razyoboy/unishared
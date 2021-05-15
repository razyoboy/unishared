import numpy as np
import matplotlib.pyplot as plt

xbar = np.array([1,2,3,4,5])
ybar = np.array([0.1,0.7,0.9,1.7,2.1])

n = len(xbar)
x = np.log10(xbar); sumx = np.sum(x)
y = np.log10(ybar); sumy = np.sum(y)
xsq = np.square(x); sumxsq = np.sum(xsq)
xy = x*y; print(xy); sumxy = np.sum(xy)

a = np.array([[n, sumx], [sumx, sumxsq]])
b = np.array([[sumy],[sumxy]])
res = np.linalg.solve(a,b)
rawa0 = res[0]; a1 = res[1]
a0 = 10**rawa0
b = -1*a1
r = np.arange(-3,3,0.01)
eqn = a0*(r**b)
#WILL THROW ERRORS
#Since it goes into the complex realm, but all is fine - this can be ignored.

print(f"Calculated a is {a0} and b of {b}")
print(f"-> f(x) = {a0}x^-{a1}")

plt.plot(r,eqn)
plt.scatter(x,y, color='g')
plt.legend(['Regressed f(x)','Data Points'])
plt.title('Power Regressed Fitted Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#github.com/razyoboy/unishared







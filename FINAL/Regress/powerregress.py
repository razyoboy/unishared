import numpy as np
import matplotlib.pyplot as plt


xbar = np.array([1,2,3,4,5])
ybar = np.array([0.1,0.7,0.9,1.7,2.1])

'''
xbar = np.array([])
ybar = np.array([])

print("Please input your x-values\nWhen done please type any character")

while True:
    xint = input('> ')
    try: 
        (isinstance(float(xint), float) == True) or (isinstance(float(xint), int) == True)
        x = np.append(x, float(xint)) 
    except:
        break

print("Please input your y-values\nWhen done please type any character")

while True:
    yint = input("> ")
    try:
        (isinstance(float(yint), float) == True) or (isinstance(float(yint), int) == True)
        y = np.append(y, float(yint))
    except:
        break
'''

n = len(xbar)
x = np.log10(xbar); sumx = np.sum(x)
y = np.log10(ybar); sumy = np.sum(y)
xsq = np.square(x); sumxsq = np.sum(xsq)
xy = x*y; sumxy = np.sum(xy)

a = np.array([[n, sumx], [sumx, sumxsq]])
bx = np.array([[sumy],[sumxy]])
res = np.linalg.solve(a,bx)
rawa0 = res[0]; a1 = res[1]
a0 = 10**rawa0
b = a1
r = np.arange(-30,30,0.01)
eqn = a0*(r**b)

print(f"Calculated a is {a0} and b of {b}")
print(f"-> f(x) = {a0}x^{a1}")

plt.plot(r,eqn)
plt.scatter(xbar,ybar, color='g')
plt.legend(['Regressed f(x)','Data Points'])
plt.title('Power Regressed Fitted Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#github.com/razyoboy/unishared







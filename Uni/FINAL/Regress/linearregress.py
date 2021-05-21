import numpy as np
import matplotlib.pyplot as plt

x = np.array([])
y = np.array([])

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

n = len(x)
sumx = np.sum(x)
sumy = np.sum(y)
xsq = np.square(x)
sumxsq = np.sum(xsq)
xy = x*y
sumxy = sum(xy)

a = np.array([[n, sumx], [sumx, sumxsq]])
bx = np.array([[sumy],[sumxy]])
res = np.linalg.solve(a,bx)
a0 = res[0]; a1 = res[1]
r = np.arange(-30,30,0.01)
eqn = a0 + (a1*r)

print(f"Calculated a0 is {a0} and a1 of {a1}")
print(f"-> f(x) = {a0} + ({a1})x")

plt.plot(r,eqn)
plt.scatter(x,y, color='g')
plt.legend(['Regressed f(x)','Data Points'])
plt.title('Linear Regressed Fitted Line')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#github.com/razyoboy/unishared
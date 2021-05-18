import numpy as np
'''
dy/dx = ax + b
let 
x = 0
a = 69
b = 420

dy/dx = 69x + 420

'''
def dydx(x):
    return (69*x) + 420 

def funcint(x):
    return ((69/2)*x**2)+(420*x) + 1

y0 = funcint(0)
n = 10; h = 1 #CAN BE CHANGED
xn = 0
ans = np.array([y0]) #From y(0)
roundstr = np.array([])
exact = np.array([])

for i in range(n):
    yn = y0 + ((((dydx(xn)+dydx(xn+1)))/2)*h)
    y0 = yn
    xn += 1
    ans = np.append(ans, float(y0))

xfunc = np.arange(0,n+1)
for i in xfunc:
    exacts = funcint(i)
    exact = np.append(exact, float(exacts))

for j in range(len(ans)):
    ansh = ans[j]
    rounded = "{:.3f}".format(ansh)
    roundstr = np.append(roundstr, float(rounded))

print(f"Calculated ODE with Heun's Method is:")

for m in range(len(ans)):
    err = ((exact[m] - ans[m])/exact[m])*100
    errfor = "{:.2f}".format(err)
    print(f"IVP of y({m}) -> {roundstr[m]}")
    print(f" With an error of {errfor}%")
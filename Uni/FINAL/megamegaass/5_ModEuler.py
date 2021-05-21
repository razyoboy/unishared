import numpy as np

'''
dy/dx = ax + b
let 
x = 0
a = 69
b = 420

dy/dx = 69x + 420

'''
#   ODE function
def dydx(x):
    return (4*x) + 4

#   ODE exact answer from integration
def funcint(x):
    return ((2*x**2)+(4*x)) - 5

y0 = funcint(0)
n = 10; h = 1 # Again, step size at 1
xn = 0  #x starts at zero
ans = np.array([y0])

#   y(0) is stored first, since it is already known
#   and the fact that this will calculate starting
#   at y(1) and so on.
roundstr = np.array([])
exact = np.array([])

for i in range(n):
    #   Since we have no y-term, we can ignore this.
    yhalf = y0 + (dydx(xn+0.5))*(h/2)

    #   This is the real difference, as stated in the text,
    #   it starts at zero but plus half of the step size;
    #   which is 0.5 - by which this would then be iterating
    #   over 'n' number of times
    #   And the rest is the same.
    yprime = dydx(xn+0.5)
    #   Increase as normal step (h = 1)
    xn += 1
    yn = y0 + (yprime*h)
    #   Let y0 to be yn; for the re-iteration
    y0 = yn
    #   Append this into an array
    ans = np.append(ans, float(y0))

xfunc = np.arange(0,n+1)
for i in xfunc:
    #   Calling the solved ODE function
    #   to calculate the errors based on this exact answer
    exacts = funcint(i)
    exact = np.append(exact, float(exacts))

#   For appending and rounding numbers to a 3 digit
#   decimal places, so that its not messy.
for j in range(len(ans)):
    ansh = ans[j]
    rounded = "{:.3f}".format(ansh)
    roundstr = np.append(roundstr, float(rounded))

print(f"Calculated ODE with Modified Euler's Method is:")

for m in range(len(ans)):
    err = ((exact[m] - ans[m])/exact[m])*100
    errfor = "{:.2f}".format(err)
    print(f"IVP of y({m}) -> {roundstr[m]}")
    print(f" With an error of {errfor}%")
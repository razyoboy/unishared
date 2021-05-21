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
    return (69*x) + 420 

#   ODE Exact answer from Integration
def funcint(x):
    return ((69/2)*x**2)+(420*x) + 1

y0 = funcint(0)
n = 10; h = 1 # Step size = 1
xn = 0 #    Starting x0 = 0
#  From y(0), as stated before - the calculation
#   starts at y(1) and above.
ans = np.array([y0]) 
#   For storing data, rounding up and exact
#   answers for error calculations
roundstr = np.array([])
exact = np.array([])

for i in range(n):
    #   Note that xn is now +1 on the right side
    #   and is just averaging itself.
    #   Main difference between Heun and Euler.
    yn = y0 + ((((dydx(xn)+dydx(xn+1)))/2)*h)
    #   Let y0 becomes yn; to iterate itself.
    y0 = yn
    xn += 1
    #   Append it to an array for storage.
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

#   Error is then calculated here which calls the
#   index of each array as an iteration of the loop

print(f"Calculated ODE with Heun's Method is:")

for m in range(len(ans)):
    err = ((exact[m] - ans[m])/exact[m])*100
    errfor = "{:.2f}".format(err)
    print(f"IVP of y({m}) -> {roundstr[m]}")
    print(f" With an error of {errfor}%")
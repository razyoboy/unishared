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

#   ODE exact answer from integration
def funcint(x):
    return ((69/2)*x**2)+(420*x) + 1

y0 = funcint(0) #   Hence y(0) = 1

n = 10; h = 1 # Let step size = 1
xn = 0 #    And xn (x) starts at 0
#   y(0) is stored first, since it is already known
#   and the fact that this will calculate starting
#   at y(1) and so on.

ans = np.array([y0]) 

#   For storing data 
roundstr = np.array([])#    For rounding of the answers
exact = np.array([])#   For storing the exact answers

#   Iterate over a number of n (how far of y(n))
for i in range(n):
    yn = y0 + (h*(dydx(xn)))
    #   Let y0 becomes yn, so that it can loop
    #   over itself with the new data
    y0 = yn
    xn += 1
    #   Append this into an array
    ans = np.append(ans, float(y0))

#   The loop below this purely for the exact answers
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

print(f"Calculated ODE with Euler's Method is:")

#   Error is then calculated here which calls the
#   index of each array as an iteration of the loop

for m in range(len(ans)):
    err = ((exact[m] - ans[m])/exact[m])*100
    errfor = "{:.2f}".format(err)
    print(f"IVP of y({m}) -> {roundstr[m]}")
    print(f" With an error of {errfor}%")


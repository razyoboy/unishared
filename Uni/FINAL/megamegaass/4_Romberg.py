import numpy as np
import scipy.integrate as wendy

#   Define the fifth order integrand
def f(x):
    return (9*x**5) + (3*x**4) - (7*x**3) + (2*x**2) + x - 8

#   For calculating the required Im and Ir values
#   Through the use of composite trapezoid rule

def comptrap(f,a,b,n):

    #   Empty array for storing data
    calc = np.array([])
    #   Mark the beginning of the I bond.
    j = a
    #   Calculate h-value
    h = float(((b-a)/n))

    #   n represents the number of 
    #   intervals, the more int, the 
    #   more accurate it is

    for i in range(n+1):
        cal = f(j)
        calc = np.append(calc, float(cal))
        j += h

    #   Based on the rule, the first term and
    #   and the last term are pulled out on its own
    x0 = calc[0]; xn = calc[-1]
    #   And the rest is then summed together
    sumcalprep = calc[1:-1]
    sumcal = np.sum(sumcalprep)
    #   Where this would be the general formula for
    #   getting the answer.
    Icomp = ((h/2)*((x0+xn) + 2*float(sumcal)))
    return Icomp
#   Defining the lower (a) and
#   the upper (b) bond.
a = 0
b = 1

#   All of these are for storing values in 
#   the many loops down below

Narray = np.array([])
Firstlvl = np.array([])
Secondlvl = np.array([])
Thirdlvl = np.array([])


#   This is the very first loop, which calculates
#   the Ir and Im for n levels.

for i in range(6): #6n levels
    n = 2**i
    #   Call the function for the comp. trapezoid rule.
    groundlevel = comptrap(f,a,b,n)
    #   Store the values then do the next one
    Narray = np.append(Narray, float(groundlevel))

#   All of these are also for the counting
#   of the many loops down below
#   where this represents the position that
#   The Ir and Im values must move down the chain

m = 0
u = 0
e = 0

for i in range(1,4): #  1,4 represents doing over 3 times
    k = 1
    firstlevel = (((4**k)*(Narray[1+m]))-Narray[0+m])/((4**k)-1)
    m += 2 #    Move two levels down
    #   Store the values then do the next one
    Firstlvl = np.append(Firstlvl, float(firstlevel))

for i in range(1,3):#   Doing over 2 times
    k = 2
    secondlevel = (((4**k)*(Firstlvl[1+u]))-Firstlvl[0+u])/((4**k)-1)
    #   Store the values then do the next one
    Secondlvl = np.append(Secondlvl, float(secondlevel))
    u += 1 #    Move one level down

for i in range(1,2):#   Doing over 1 time
    k = 3
    thirdlevel = (((4**k)*(Secondlvl[1+e]))-Secondlvl[0+e])/((4**k)-1)
    #   Store the values then do the next one
    Thirdlvl = np.append(Thirdlvl, float(thirdlevel))
    e += 1 #    Move on level down

#   Calling the first index of the array (the only element)
ansraw = Thirdlvl[0]
#   For rounding the answer into 4 decimal places
ans = "{:.4f}".format(ansraw)
#   Exact Integral is calculated by the scipy.integrate module.
Iexact = wendy.quad(f,a,b); exact = Iexact[0]
err = abs(((exact - ansraw) / exact) * 100)

print(f"The calculated integral with bounds from {b} to {a} is:")
print(f"> {ans}")
print(f"(with an error percentage of {err} %)")



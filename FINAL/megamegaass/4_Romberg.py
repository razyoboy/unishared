import numpy as np
import scipy.integrate as wendy

def f(x):
    return (9*x**5) + (3*x**4) - (7*x**3) + (2*x**2) + x - 8

def comptrap(f,a,b,n):

    calc = np.array([])
    j = a
    h = float(((b-a)/n))

    for i in range(n+1):
        cal = f(j)
        calc = np.append(calc, float(cal))
        j += h

    x0 = calc[0]; xn = calc[-1]
    sumcalprep = calc[1:-1]
    sumcal = np.sum(sumcalprep)
    Icomp = ((h/2)*((x0+xn) + 2*float(sumcal)))
    return Icomp

a = 0
b = 1

Narray = np.array([])
Firstlvl = np.array([])
Secondlvl = np.array([])
Thirdlvl = np.array([])

for i in range(6): #4n levels
    n = 2**i
    groundlevel = comptrap(f,a,b,n)
    Narray = np.append(Narray, float(groundlevel))
m = 0
u = 0
e = 0

for i in range(1,4):
    k = 1
    firstlevel = (((4**k)*(Narray[1+m]))-Narray[0+m])/((4**k)-1)
    m += 2 #Move two levels down
    Firstlvl = np.append(Firstlvl, float(firstlevel))

for i in range(1,3):
    k = 2
    secondlevel = (((4**k)*(Firstlvl[1+u]))-Firstlvl[0+u])/((4**k)-1)
    Secondlvl = np.append(Secondlvl, float(secondlevel))
    u += 1

for i in range(1,2):
    k = 3
    thirdlevel = (((4**k)*(Secondlvl[1+e]))-Secondlvl[0+e])/((4**k)-1)
    Thirdlvl = np.append(Thirdlvl, float(thirdlevel))
    e += 1

ansraw = Thirdlvl[0]
ans = "{:.4f}".format(ansraw)
Iexact = wendy.quad(f,a,b); exact = Iexact[0]
err = abs(((exact - ansraw) / exact) * 100)

print(f"The calculated integral with bounds from {b} to {a} is:")
print(f"> {ans}")
print(f"(with an error percentage of {err} %)")



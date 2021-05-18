from typing import no_type_check


import numpy as np
import scipy.integrate as wendy

def f(x):
    return ((2*x**3)-(5*x**2)+(3*x)+1)

def comptrap(f,a,h,n):
    
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
n = 1
h = float(((b-a)/n))

Irom = np.zeros((10,9))
ea = 100; n = 1; i = 1
Irom[1,1] = comptrap(f,a,h,n)

while ea > 0.001:
    n = 2**i
    h = float(((b-a)/n))
    Irom[i+1, 1] = comptrap(f,a,h,n)
    for k in range(2,i+2):
        j = 2 + i - k
        Irom[j,k] = (4**(k-1) * Irom[j+1, k-1] - Irom[j,k-1])/(4**(k-1)-1)

        ea = abs((Irom[1,i+1] - Irom[2,i])/Irom[1,i+1]) * 100
        i += 1

print(Irom)

##not finished, i give up ทำมือเอาไอสัสยากชห
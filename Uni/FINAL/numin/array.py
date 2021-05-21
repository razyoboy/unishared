import numpy as np
import scipy.integrate as wendy

def f(x):
    return x**2+x

a = -1
b = 1
I = wendy.quad(f,a,b); print(I)

first = f(-1/np.sqrt(3))
sec = f(1/np.sqrt(3))
res = first + sec; print(res)
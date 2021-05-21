import numpy as np
import scipy.integrate as wendy

def f(x):
    return ((2*x**3)-(5*x**2)+(3*x)+1)

a = 0
b = 2
h = ((b-a)/2)

I = wendy.quad(f, a,b)

calc = np.array([])
j = a

while j != b + 1:
    cal = f(j)
    calc = np.append(calc, float(cal))
    j += h

x0 = calc[0]; x2 = calc[-1]; x1 = calc[1]
Isimp = ((h/3)*(x0+(4*x1)+x2))
err = ((Isimp - I[0])/I[0])*100

print(f"An exact approximation is:")
print(f"{I[0]} with an error of {I[1]*100} %")
print("Answer obtained from the Simpson's Rule:")
print(f" I = {Isimp} with an error of {err} %")

#github.com/razyoboy/unishared
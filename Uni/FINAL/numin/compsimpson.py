import numpy as np
import scipy.integrate as wendy

def f(x):
    return ((x**4)+(2*x**3)-(5*x**2)+(3*x)+1)

print("Enter your lower bond")
a = float(input("> "))
print("Enter your upper bond")
b = float(input("> "))

print("Specify 'n' (How much 'soy' you want) [EVEN NUMBERS ONLY]")
n = int(input("> "))

h = float(((b-a)/n))

I = wendy.quad(f,a,b)
calc = np.array([])
j = a

for i in range(n+1):
    cal = f(j)
    calc = np.append(calc, float(cal))
    j += h

x0 = calc[0]; xn = calc[-1]
sumcalprep = calc[1:-1]
odd = sumcalprep[::2]; even = sumcalprep[1::2]
sumodd = np.sum(odd); sumeven = np.sum(even)
Icomp = ((h/3)*(x0+xn+(4*sumodd)+(2*sumeven)))
err = ((Icomp - I[0])/I[0])*100

print(f"An exact approximation is:")
print(f"{I[0]} with an error of {I[1]*100} %")
print("Answer obtained from the Composite Trapezoidal Rule:")
print(f"(with n = {n})")
print(f" I = {Icomp} with an error of {err} %")

#github.com/razyoboy/unishared
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as wendy

def f(x):
    return ((2*x**3)-(5*x**2)+(3*x)+2)

print("Enter your lower bond")
a = float(input("> "))
print("Enter your upper bond")
b = float(input("> "))

I = wendy.quad(f, a,b)
print(f"An exact approximation is:")
print(f"{I[0]} with an error of {I[1]*100} %")

print("Answer obtained from Trapezoidal Rule:")
Itrap = (((b-a)/2)*(f(a)+f(b)))
err = ((I[0] - Itrap) / I[0])*100
print(f"{Itrap} with an error of {err} %")

#github.com/razyoboy/unishared
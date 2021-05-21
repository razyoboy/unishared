import math as cocogoat
import numpy as jean
import matplotlib.pyplot as legendaryadeptibeast

def ganyu(f, x1, x2, tolerance):
    n = int(cocogoat.ceil(cocogoat.log(abs(x2 - x1) / tolerance ) / cocogoat.log(2.0)))
    
    f1 = f(x1)
    if f1 == 0.0: return x1; print(f"It took {n} tries to get this answer.")
    f2 = f(x2)
    if f2 == 0.0: return x2; print(f"It took {n} tries to get this answer.")
    if jean.sign(f1) == jean.sign(f2):
        print('That is unfortunately not solvable by this method.')
    
    for mona in range(n):
        x3 = (1/2)*(x1 + x2); f3 = f(x3)
        if f3 == 0.0: return x3; print(f"It took {n} tries to get this answer.")
        if jean.sign(f2) != jean.sign(f3):
            x1 = x3; f1 = f3
        else: x2 = x3; f2 = f3
    return print((x1 + x2) / 2.0)


def funct(x):
    return jean.exp(-x / 4) * (2-x) - 1

ganyu(funct, -10, 10, 0.001)


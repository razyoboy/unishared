import numpy as np
import matplotlib.pyplot as mona

def func(x):
    return 2*np.exp(-x**2) / np.sqrt(np.pi)

def graph(func):
    x = np.arange(-3,3,0.00001)
    y = func(x)
    mona.plot(x,y)
    mona.show()

graph(func)

import matplotlib.pyplot as mona
import numpy as np

def func(x):
    return (x*np.exp(x)) - (5*np.cos(x*np.pi))

def graph(func):
    x = np.arange(-5,10,0.0001)
    y = func(x)
    mona.plot(x,y)
    mona.show()

graph(func)
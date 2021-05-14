import matplotlib.pyplot as plt
import numpy as np

x = np.array([2,3,4])
y = np.array([0.2239, -0.2601,-0.3971])

a = input(">> ")
b = int(a)
c = np.ones(3)
"""
def general(b):
    for i in range(b,0,-1):
        print(i)
    return i

general(b)
"""

def general(b):
    for i in range(0,b,1):
        y[i] = c[i] + c[i+1]*(x[i]-x[0]) + c[i+2]*(x[i]-x[1])*(x[i]-x[0]) 
        

        
        
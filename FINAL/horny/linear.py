import numpy as np
import matplotlib.pyplot as plt

"""
x = np.array([2,4])
y = np.array([0.2239, -0.3971])
"""

#y = mx+c
def equa(x1,x2,f1,f2):
    c0 = f1
    c1 = (f2-f1)/(x2-x1)
    return c0,c1, x1

c0, c1,x1= equa(2,4,0.2239, -0.3971)

def cal(x):
    y = c0 + (x-x1)*c1
    return y

y = cal(3.2)
print(y)








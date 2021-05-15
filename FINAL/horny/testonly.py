
import numpy as np
"""
a = [0,0,0,0,0]
a.insert(2,1)
print(a)
b = np.ones(3)
print(b)
print(b[2])
c = input(">>")
d = int(c)
h =d
print(h)
"""
mat = np.ones([3,3])
ne = np.ones([3,3])
ne[2,0] = 2
print(ne)
ne = mat
print(ne)

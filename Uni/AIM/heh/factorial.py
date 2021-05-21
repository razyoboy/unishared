import numpy as np

print("Hello, welcome to the Fatorian finder calculator.\nPlease specify your value below!")
a = input(">")
b = np.arange(1,int(a)+1)
c = np.product(b)
print(c)

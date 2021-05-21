import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 4])
y = np.array([0.2239,-0.3971])

intx = float(input("> "))

c0 = y[0]
c1 = (y[1] - y[0]) / (x[1] - x[0])
diff = intx - x[0]

inty = c0 + (c1*diff)

print(inty)

#It works but its not really 'automated' so i dunno :/
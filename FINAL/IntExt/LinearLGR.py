import numpy as np
import matplotlib.pyplot as plt

x = np.array([2,4,3.2])
y = np.array([0.2239,-0.3971])

def LGR(x,y):
    n = len(x) - 2
    j = 0
    for i in range(n):
        l0 = (x[1+j]-x[2+j])/(x[1+j]-x[0+j])
        l1 = (x[0+j]-x[2+j])/(x[0+j]-x[1+j])
        inty= (l0*y[0+j])+(l1*y[1+j]) 
        j += 1
        y = np.append(y, float(inty))
    return y

ymod = LGR(x,y)
print(f"Interpolated values are (x,y);")
w = len(ymod)
p = 0
for k in range (w):
    print(f"(X{p},Y{p}) -> ({x[0+p]}, {ymod[0+p]})")
    p += 1

plt.scatter(x,ymod)
plt.xlabel('x')
plt.ylabel('f(x)')

for xs,ys in zip(x,ymod):
    xout = "{:.2f}".format(xs)
    yout = "{:.2f}".format(ys)
    label = f"({xout},{yout})"
    plt.annotate(label, (xs,ys))

plt.title('Linear LGR Interpolation Results')
plt.show()
import numpy as np
import matplotlib.pyplot as plt

x = np.array([5,8,10,12,14,16,18,13.75])
y = np.array([10989,18959,47019,98519,183875,315423,507419])

def NDD(x,y):
    c0 = y[0]
    c1 = (y[1] - y[0])/(x[1]-x[0])
    c2 = (((y[2]-y[1])/(x[2]-x[1])) - c1) / (x[2]-x[0])
    c3 = (((y[3] - y[2] - y[1])/(x[3]-x[2]-x[1])) - (y[2]-y[1]-y[0])/(x[2]-x[1]-x[0])) / (x[3]-x[0])
    c4 = (((y[4]-y[3]-y[2]-y[1])/(x[4]-x[3]-x[2]-x[1])) - ((y[3]-y[2]-y[1]-y[0])/(x[3]-x[2]-x[1]-x[0])))/(x[4]-x[0])
    c5 = (((y[5]-y[4]-y[3]-y[2]-y[1])/(x[5]-x[4]-x[3]-x[2]-x[1])) - ((y[4]-y[3]-y[2]-y[1]-y[0])/(x[4]-x[3]-x[2]-x[1]-x[0])))/(x[5]-x[0])
    c6 = (((y[6]-y[5]-[4]-y[3]-y[2]-y[1])/(x[6]-x[5]-x[4]-x[3]-x[2]-x[1])) - ((y[5]-y[4]-y[3]-y[2]-y[1]-y[0])/(x[5]-x[4]-x[3]-x[2]-x[1]-x[0])))/(x[6]-x[0])
    diffc1 = (x[7]-x[0])
    diffc2 = (x[7]-x[0])*(x[7]-x[1])
    diffc3 = (x[7]-x[0])*(x[7]-x[1])*(x[7]-x[2])
    diffc4 = (x[7]-x[0])*(x[7]-x[1])*(x[7]-x[2])*(x[7]-x[3])
    diffc5 = (x[7]-x[0])*(x[7]-x[1])*(x[7]-x[2])*(x[7]-x[3])*(x[7]-x[4])
    diffc6 = (x[7]-x[0])*(x[7]-x[1])*(x[7]-x[2])*(x[7]-x[3])*(x[7]-x[4])*(x[7]-x[5])
    inty = c0 + (c1*diffc1) + (c2*diffc2) + (c3*diffc3) + (c4*diffc4) + (c5*diffc5) + (c6*diffc6)
    print(inty)
    y = np.append(y, float(inty))
    return y

ymod = NDD(x,y)
print(f"Interpolated values are (x,y);")
w = len(ymod)
p = 0
for k in range (w-1):
    print(f"(X{p},Y{p}) -> ({x[0+p]}, {ymod[0+p]})")
    p += 1

ans = ymod[-1]
exact = 170950.8
err = abs(((exact - ans)/exact) * 100)
print(f"Error percentage is {err}%")

print(f"(Xint,Yint) -> ({x[-1]}, {ymod[-1]})")
plt.scatter(x,ymod)
plt.xlabel('x')
plt.ylabel('f(x)')

for xs,ys in zip(x,ymod):
    xout = "{:.2f}".format(xs)
    yout = "{:.2f}".format(ys)
    label = f"({xout},{yout})"
    plt.annotate(label, (xs,ys))

plt.title('Polynomial (Higher Order) NDD Interpolation Results')
plt.show()


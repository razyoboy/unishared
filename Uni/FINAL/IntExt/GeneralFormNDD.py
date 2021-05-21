import numpy as np
import matplotlib.pyplot as plt

x = np.array([9,12,16,19,13.75])
y = np.array([30635,98519,315423,631065])

#For three points, I think I'll add four and five later - but I think I get how it works.
#So if she have six points then its mega messy, but it'll be okay. -ish.
def three(x,y):
    n = len(x) - 4
    j = 0
    for i in range(n):
        c0 = y[0+j]
        c1 = (y[1+j] - y[0+j])/(x[1+j]-x[0+j])
        c2 = ((((y[2+j] - y[1+j])/(x[2] - x[1])) - ((y[1+j] - y[0+j]) / (x[1+j]-x[0+j])))) / (x[2+j] - x[0+j])
        c3 = (((y[3+j] - y[2+j] - y[1+j])/(x[3+j]-x[2+j]-x[1+j])) - (y[2+j]-y[1+j]-y[0+j])/(x[2+j]-x[1+j]-x[0+j])) / (x[3+j]-x[0+j])
        diffc1 = (x[4+j]-x[0+j])
        diffc2 = (x[4+j]-x[0+j])*(x[4+j]-x[1+j])
        diffc3 = (x[4+j]-x[0+j])*(x[4+j]-x[1+j])*(x[4+j]-x[2+j])
        inty = c0 + (c1*diffc1) + (c2*diffc2) + (c3*diffc3)
        j += 1
        y = np.append(y, float(inty))
    return y

ymod = three(x,y)
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

plt.title('Polynomial (Higher Order) NDD Interpolation Results')
plt.show()

#github.com/razyoboy/unishared
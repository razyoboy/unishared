import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,10,20,13.75])
y = np.array([-1,47019,776039])

'''
print("Please input your x-values (x-axis) [Minimum of Three] \n When done please type any character")

while True:
    xint = input('> ')
    try: 
        (isinstance(float(xint), float) == True) or (isinstance(float(xint), int) == True)
        x = np.append(x, float(xint)) 
    except:
        break

print("Please inout your f(x)-values (y-axis) [NO MORE than Three]\n When done please type any character")

while True:
    yint = input("> ")
    try:
        (isinstance(float(yint), float) == True) or (isinstance(float(yint), int) == True)
        y = np.append(y, float(yint))
    except:
        break
'''

def LGR(x,y):
    n = len(x) - 3
    j = 0
    for i in range(n):
        l0 = ((x[2+j]-x[3+j])*(x[1+j]-x[3+j]))/((x[2+j]-x[0+j])*(x[1+j]-x[0+j]))
        l1 = ((x[2+j]-x[3+j])*(x[0+j]-x[3+j]))/((x[2+j]-x[1+j])*(x[0+j]-x[1+j]))
        l2 = ((x[1+j]-x[3+j])*(x[0+j]-x[3+j]))/((x[1+j]-x[2+j])*(x[0+j]-x[2+j]))
        inty = (l0*y[0+j])+(l1*y[1+j])+(l2*y[2+j])
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

plt.title('Quadratic LGR Interpolation Results')
plt.show()

#github.com/razyoboy/unishared
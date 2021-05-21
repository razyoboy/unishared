import numpy as np
import matplotlib.pyplot as plt

#   Randomly chosen data points, out of 25 given - 7 were chosen 
x = np.array([5,8,10,12,14,16,18,13.75])
y = np.array([10989,18959,47019,98519,183875,315423,507419])

def NDD(x,y):
    #   c0 through c6 are substituted based on the position of the x and y arrays.
    c0 = y[0]
    c1 = (y[1] - y[0])/(x[1]-x[0])
    c2 = ((((y[2] - y[1])/(x[2] - x[1])) - ((y[1] - y[0]) / (x[1]-x[0])))) / (x[2] - x[0])
    c3 = ((y[3]-y[0] - (c1*(x[3]-x[0])) - (c2*(x[3]-x[0])*(x[3]-x[1]))))/((x[3]-x[0])*(x[3]-x[1])*(x[3]-x[2]))
    c4 = ((y[4]-y[0] - (c1*(x[4]-x[0])) - (c2*(x[4]-x[0])*(x[4]-x[1])) - ((c3*(x[4]-x[0])*(x[4]-x[1])*(x[4]-x[2]))))/((x[4]-x[0])*(x[4]-x[1])*(x[4]-x[2])*(x[4]-x[3])))
    c5 = ((y[5]-y[0] - (c1*(x[5]-x[0])) - (c2*(x[5]-x[0])*(x[5]-x[1])) - ((c3*(x[5]-x[0])*(x[5]-x[1])*(x[5]-x[2]))) - (c4*(x[5]-x[0])*(x[5]-x[1])*(x[5]-x[2])*(x[5]-x[3])))/((x[5]-x[0])*(x[5]-x[1])*(x[5]-x[2])*(x[5]-x[3])*(x[5]-x[4])))
    c6 = ((y[6]-y[0] - (c1*(x[6]-x[0])) - (c2*(x[6]-x[0])*(x[6]-x[1])) - ((c3*(x[6]-x[0])*(x[6]-x[1])*(x[6]-x[2]))) - (c4*(x[6]-x[0])*(x[6]-x[1])*(x[6]-x[2])*(x[6]-x[3])) - (c5*(x[6]-x[0])*(x[6]-x[1])*(x[6]-x[2])*(x[6]-x[3])*(x[6]-x[4])))/((x[6]-x[0])*(x[6]-x[1])*(x[6]-x[2])*(x[6]-x[3])*(x[6]-x[4])*(x[6]-x[5])))
    
    #   diff is simply the (xn-x0) terms on every cn terms, to simplify things.
    diffc1 = (x[7]-x[0])
    diffc2 = (x[7]-x[0])*(x[7]-x[1])
    diffc3 = (x[7]-x[0])*(x[7]-x[1])*(x[7]-x[2])
    diffc4 = (x[7]-x[0])*(x[7]-x[1])*(x[7]-x[2])*(x[7]-x[3])
    diffc5 = (x[7]-x[0])*(x[7]-x[1])*(x[7]-x[2])*(x[7]-x[3])*(x[7]-x[4])
    diffc6 = (x[7]-x[0])*(x[7]-x[1])*(x[7]-x[2])*(x[7]-x[3])*(x[7]-x[4])*(x[7]-x[5])

    #   From the general formula of NDD; f(x) = inty
    inty = c0 + (c1*diffc1) + (c2*diffc2) + (c3*diffc3) + (c4*diffc4) + (c5*diffc5) + (c6*diffc6)
    y = np.append(y, float(inty))
    return y

#   Call the function to return y
ymod = NDD(x,y)
print(f"Interpolated values are (x,y);")

#   Loop for printing the given values, k is minus one due to the nature of the code,
#   that would append the answer to the last element, so it is not yet needed here.

w = len(ymod)
p = 0
for k in range (w-1):
    print(f"(X{p},Y{p}) -> ({x[0+p]}, {ymod[0+p]})")
    p += 1

#   Since the answer is appended to the very end of the array, 
#   -1 is the index for the last element of an array
#   Where ans is calling the said last element index 

ans = ymod[-1]
exact = 170950.8

#Calculate the error 

err = abs(((exact - ans)/exact) * 100)
print(f"Error percentage is {err}%")

#Finally, print the result of the interpolation

print(f"(Xint,Yint) -> ({x[-1]}, {ymod[-1]})")
plt.scatter(x,ymod)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.scatter(x[-1],ymod[-1])
plt.legend(['Given Data Points','Interpolated Point'])


#   Can be used but the graph is too messy, since there are many values.
#   And that the y-values are large, the text would overlap each other.

'''
for xs,ys in zip(x,ymod):
    xout = "{:.2f}".format(xs)
    yout = "{:.2f}".format(ys)
    label = f"({xout},{yout})"
    plt.annotate(label, (xs,ys))
'''
plt.title('Polynomial (Higher Order) NDD Interpolation Results')
#   For saving the figure without screencapping and
#   without manually going through the box
plt.savefig("OutNDD"+".png", format="PNG", bbox_inches='tight')
plt.show()




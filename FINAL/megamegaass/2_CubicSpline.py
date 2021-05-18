import numpy as np
import matplotlib.pyplot as plt

#Function is x^3+3x^2-x+1
def func(x):
    return (x**3) + (3*x**2) - x + 1


r = np.arange(1,12,0.01)
x = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
y = np.array([func(x)])
ynoise = np.array([1.86659720203050,20.8674563253425,52.7006420027122,108.941988472583,
196.364904335012,315.869887971699,483.830921040365,700.207892701206,964.196695549280,
1291.08274722698,1682.53166177461,2148.93837253998])

#From MATLAB

y0 = 1.86659720203050
y1 = 108.941988472583
y2 = 700.207892701206
y3 = 2148.93837253998
x0 = 1
x1 = 4
x2 = 8
x3 = 12

matA = np.array([
    [x1**3, x1**2, x1, 1,0,0,0,0,0,0,0,0],
    [0,0,0,0,x1**3,x1**2,x1,1,0,0,0,0],
    [0,0,0,0,x2**3,x2**2,x2,1,0,0,0,0],
    [0,0,0,0,0,0,0,0,x2**3,x2**2,x2,1],
    [x0**3,x0**2,x0,1,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,x3**3,x3**2,x3,1],
    [3*x1**2,2*x1,1,0,-3*x1**2,-2*x1,-1,0,0,0,0,0],
    [0,0,0,0,3*x2**2,2*x2,1,0,-3*x2**2,-2*x2,-1,0],
    [6*x1,2,0,0,-6*x1,-2,0,0,0,0,0,0],
    [0,0,0,0,6*x2,2,0,0,-6*x2,-2,0,0],
    [6*x0,2,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,6*x3,2,0,0]])

#matB = np.array([y1,y1,y2,y2,y0,y3,0,0,0,0,0,0])
matB = np.array([[y1],[y1],[y2],[y2],[y0],[y3],[0],[0],[0],[0],[0],[0]])
res = np.linalg.solve(matA, matB)

a1 = res[0]; b1 = res[1]; c1 = res[2]; d1 = res[3]
a2 = res[4]; b2 = res[5]; c2 = res[6]; d2 = res[7]
a3 = res[8]; b3 = res[9]; c3 = res[10]; d3 = res[11]

r1 = np.arange(1,4.001,0.001)
r2 = np.arange(4,8.001,0.001)
r3 = np.arange(8,12.001,0.001)

eqnA = (a1*r1**3) + (b1*r1**2) + (r1*c1) + d1
eqnB = (a2*r2**3) + (b2*r2**2) + (r2*c2) + d2
eqnC = (a3*r3**3) + (b3*r3**2) + (r3*c3) + d3

#Test for errors
rangeA = x[0:4]
rangeB = x[4:8]
rangeC = x[8:12]

for i in rangeA:
    eqnerA = (a1*i**3) + (b1*i**2) + (i*c1) + d1
    exactval = ynoise[i-1]
    errA = abs((exactval - eqnerA)/(exactval)*100)
    print(f"Error for f(x1) at x = {i} is {errA} %")
    
for i in rangeB:
    eqnerB = (a2*i**3) + (b2*i**2) + (i*c2) + d2
    exactval = ynoise[i-1]
    errB = abs((exactval - eqnerB)/(exactval)*100)
    print(f"Error for f(x2) at x = {i} is {errB} %")

for i in rangeC:
    eqnerC = (a3*i**3) + (b3*i**2) + (i*c3) + d3
    exactval = ynoise[i-1]
    errC = abs((exactval - eqnerC)/(exactval)*100)
    print(f"Error for f(x3) at x = {i} is {errC} %")

plt.plot(r1,eqnA); plt.plot(r2,eqnB); plt.plot(r3,eqnC)
plt.legend(['f(x1)','f(x2)','f(x3)'])
plt.scatter(x, ynoise)
plt.show()
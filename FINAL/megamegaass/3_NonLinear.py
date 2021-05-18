import numpy as np
import matplotlib.pyplot as plt

#Define random function (Non-Linear)
#Value generated from MATLAB, will attached in the paper.
#   y = 1 - 0.1*x - 0.8*x**2
#   Noise is added by y = y + 2*randn(size(x)); where size(x) is 1 to 20, with step of 1

xbar = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
y = np.array([0.145779585503260, -2.92399086993218, -10.0004247368936, -12.7713019431907, 
-21.1627330231353, -30.3584126103346, -41.2128033113280, -52.0671142186320,-68.7052714717661,
-78.0715411547368,-95.8598797970891,-115.440055703285,-135.569542172057,-158.796327169128,
-178.462629435743,-205.666434959015,-233.329060327574,-257.297228463147,-290.149542112105,
-322.178058061442])

n = len(xbar)
xp2= xbar**2
xp3 = xbar**3
xp4 = xbar **4
sumxp2 = np.sum(xp2)
sumxp3 = np.sum(xp3)
sumxp4 = np.sum(xp4)
sumx = np.sum(xbar)
sumy = np.sum(y)
xbary = xbar*y; sumxy = np.sum(xbary)
xbarp2y = xp2*y; sumxbarp2y = np.sum(xbarp2y)

matA = np.array([[n, sumx, sumxp2],[sumx, sumxp2, sumxp3],[sumxp2, sumxp3, sumxp4]])
matB = np.array([[sumy],[sumxy],[sumxbarp2y]])
res = np.linalg.solve(matA, matB)
a0 = res[0]; a1 = res[1]; a2 = res[2]
r = np.arange(-1,20,0.01)
eqn = a0 + (a1*r) + (a2*(r**2))
plt.scatter(xbar,y)
plt.plot(r,eqn, color='g')
plt.legend(['Regressed f(x)','Data Points'])
plt.title('Polynomial Regressed Fitted Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as texas

x = np.array([2,3,4])
y = np.array([0.2239,-0.2601,-0.3971])
pairs = np.array([[2,0.2239],[3,-0.2601],[4,-0.3971]])
f = np.array([3.2]) 
m = np.array([])
store = np.array([])
yint = np.array([])
ans = np.array([])

fx = np.append(x,f)
fsort = np.sort(fx)

for i in f:
    res = np.where(fsort == i)
    bef = res[0]-1  #x0 pos
    mid = res[0]    #x pos
    aft = res[0]+1  #x1 pos
    x0 = fsort[bef]
    xm = fsort[mid]
    x1 = fsort[aft]
    store = np.append(store, float(x0))
    store = np.append(store, float(xm))
    store = np.append(store, float(x1))

for i, j in pairs:
    find = np.where(store == i)
    pos = find[0]
    val = store[pos]
    
    for i in val:
        findagain = np.where(pairs == i)
        posagain = findagain[0]
        sub = pairs[posagain]
        yval = sub[0][1]
        yint = np.append(yint, float(yval))

e = 0
l = 0
for i in f:
    intm = (yint[1+e]-yint[0+e])/(x1-x0)
    e += 2
    funcx = yint[0+l] + (intm*(xm-x0))
    l += 1
    ans = np.append(ans, float(funcx))

print(ans)









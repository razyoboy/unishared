
import numpy as np
"""
a = [0,0,0,0,0]
a.insert(2,1)
print(a)
b = np.ones(3)
print(b)
print(b[2])
c = input(">>")
d = int(c)
h =d
print(h)

mat = np.ones([3,3])
ne = np.ones([3,3])
ne[2,0] = 2
print(ne)
ne = mat
print(ne)
"""
"""
a = np.array([0,1,2])
b = np.array([4,5,6])
c = np.array([5,5,5])
x = np.vstack((a,b,c))

print(">>",x.transpose())
"""
"""
def cal(a,b,n):
    for j in np.arange(a+(b-a)/n, b+(b-a)/n, (b-a)/n):
       print (j)
    return a

x = cal(0,4,8)
print(x)
"""

file1= 'data2_x.txt' 
x = np.loadtxt(file1, delimiter=',', dtype=float)
x = np.array(x) #change x to array


file2 = 'data2_y.txt'
y = np.loadtxt(file2, delimiter = ',', dtype=float)
y = np.array(y) #change y to array
#In this case, we may perform with 3 funcitons 4 points
print(x[0]**2)
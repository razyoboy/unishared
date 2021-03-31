import numpy as np      
x = np.array([2,3,4],float)
y = np.array([0.2239,-0.2601,-0.3971],float)      
n = len(x)
x_value = 3.2    
y_new = 0    
#Construct table and load xy pairs in first columns
A = np.zeros([n,n+1])

for i in range (0,n):
    A[i][0] = x[i] 
    A[i][1] = y[i]
    
#Fill in Divided differences
for j in range(2,n+1):
    for i in range(j-1,n):
        A[i][j] = (A[i][j-1]-A[i-1][j-1]) / (A[i][0]-A[i-j+1][0])

#Copy diagonal elements into array for returning
c = np.zeros(n)
for i in range(0,n):
    c[i] = A[i][i+1]

print ('C0 is:', c[0])
print ('C1 is:', c[1])
print ('C2 is:', c[2])

f = np.zeros(n)
for i in range (0,n):
    f[i] = 1 
for i in range (n):
    for j in range(1,i+1,1):
        f[i] = f[i] * (x_value-x[j-1])
for i in range (0,n):
    y_new = y_new + (c[i]*f[i])   

print (y_new)
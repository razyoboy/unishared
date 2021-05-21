import numpy as np

a = int(input("size of matrix >> ")) #the size that we get is a*a (square matrix)
mat = np.ones([int(a), int(a)])
newmat = np.ones([int(a), int(a)])
res = np.ones([int(a),1])



for i in range(0,a,1):
    for j in range(0,a,1):
        print(f"Position {i+1} * {j+1} ") #that must be  of the equation
        v = int(input("the coefficient >> "))
        mat[i,j] = v
        newmat[i,j] = v

#print(np.linalg.det(mat))

for i in range(0,a,1):
    print(f"Position {i+1} * {1}")
    u = int(input("the result >> "))
    res[i,0] = u # careful the size is not what you thought

#b = int(input("the indent of x we want to calculate >> ")) #begin with x0,x1, .... , 
                                                            #xn >>>>> careful...
                                                            # if you want to find x0 put 0 into the input

for i in range(0,a,1):
    for j in range(0,a,1):
        newmat[j, i] = res[j,0]
        if j+1 == a : 
            #print("first> \n", newmat)  
            #print("mat >\n", mat) 
            ans = np.linalg.det(newmat)/np.linalg.det(mat)
            print(f"The value of x{i} is {ans}")
            newmat[:,:] = mat[:,:]
        





      



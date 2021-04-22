import numpy as np
set = [2,4,6,7,8,5]
a = int(input(">> "))
def cal(a):
    if  a>1 :
        for i in range(2, a):
            if a % i :
                print("This is a prime number")
                return a
            else: 
                print("This is not")      
    else :
        print("This is not prime")

val= cal(a)
print(">> ", val)
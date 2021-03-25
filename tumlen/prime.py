import numpy as ganyu

set = [2,4,6,7,8,5]
b = []

def prime(set):
    for i in range(2,len(set)):
        for p in range(len(set)):
            num = set[p]
            print(num)
            if (num % i) == 0:
                if num not in b:
                    b.append(num)
                    return b

res = prime(set); print(res)
import numpy as np

setA = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
setB = [ 8830, 8831, 8832, 8833, 8834, 8835, 8836, 8837, 8838, 8839 ]
setC = [ -37, 3/7, 7//3, '3', 7, 7.3, 3+7, 37, 73, 703 ]

def cal(set):
    res = []
    for num in set:
        if num > 1:
            for i in range(2, num):
                if num % i:
                    res.append(num)

                    return res

results = cal(setB)

print(results)

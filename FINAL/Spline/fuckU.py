import numpy as np

a = np.array([2,4])
b = np.array([3])
y = np.array([0.2239, -0.2601, -0.3971])
x = np.array([])

tobesort = np.append(a, b)
#print(tobesort)

sorted = np.sort(tobesort)
print(sorted)


while True:
    xint = input('> ')
    try: 
        (isinstance(float(xint), float) == True) or (isinstance(float(xint), int) == True)
        x = np.append(x, float(xint)) 
    except:
        break

print("the interest value", x)
#j = float(input("the value we want to find >> "))
for i in range(0, len(x)):
    for j in range(0, len(sorted)):
        if x[i] < sorted[j]:
            """
            print("hi >> ",sorted[j])
            print("hello >> ",sorted[j-1])
            """
            slope = (y[j]-y[j-1])/(sorted[j]-sorted[j-1])
            f = slope*(x[i]-sorted[j-1]) + y[j-1]
            print("the ans is ", f)
            break



           
            




import numpy as np

a = np.array([2,3,4])
b = np.array([3.2])
y = np.array([0.2239,-0.2601,-0.3971])
pairs = np.array([[2,0.2239],[3,-0.2601],[4,-0.3971]])
tobesort = np.append(a, b)
#print(tobesort)

sorted = np.sort(tobesort)
#print(sorted)
hentai = np.array([])
sex = np.array([])
for i in b:
    res = np.where(sorted == i)
    bef = res[0]-1
    mid = res[0]
    aft = res[0]+1
    x0 = sorted[bef]
    x = sorted[mid]
    x1 = sorted[aft]
    sex = np.append(sex, float(x0))
    sex = np.append(sex, float(x))
    sex = np.append(sex, float(x1)); print(sex)
    #print(bef,mid,aft)

for i, j in pairs:
        ok = np.where(sex == i)
        ehe = ok[0]
        val = sex[ehe]
        for i in val:
            this = np.where(pairs == i)
            fin = this[0]
            yfuck = pairs[fin]
            pop = yfuck[0][1]; print(pop)
            hentai = np.append(hentai, float(pop)); print(hentai)


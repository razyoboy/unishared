import random
import numpy as np

class Gacha():
    count4s = 0
    count5s = 0

    def __init__(self, roll):
        self.roll = roll

    def rng(self, roll):
        for _ in range(roll):
            rollit = random.uniform(0,100)
            yield rollit

    def gurantee(self):
        if self.count4s == 10:
            res = (f"4-Stars (Pity)")
            self.count42 = 0
            return res
        elif self.count5s == 90:
            res = (f"5-Stars (Pity)")
            self.count5s = 0
            return res
        else: return None

    def nrolls(self):

        res = self.rng(self.roll)
        store = np.array([])
        for i in res:
            store = np.append(store, float(i))
        for i in store:
            if i >= 99.99:
                print("ต่ อ ย ท้ อ ง น า ง ฟ้ า")
            elif i >= 98.00:
                self.count5s += 1
                self.count4s += 1
                j = self.gurantee()
                if j is None:
                    print("5-Stars")
                    self.count5s = 0
                else: print(j)

            elif (98.00 > i >= 75.00):
                self.count5s += 1
                self.count4s += 1
                j = self.gurantee()
                if j is None:
                    print("4-Stars")
                    self.count4s = 0
                else: print(j)
            
            else:
                self.count5s += 1
                self.count4s += 1
                j = self.gurantee()
                if j is None:
                    print("3-Stars")
                else: print(j)
        return store, self.count5s, self.count4s


hey = Gacha(1000).nrolls(); print(hey)


"""
a = random.randrange(0,100,1); print(a)
b = random.uniform(0,100); print(b)
"""
import random
import numpy as np

class Gacha():
    count4s = 0
    count5s = 0

    fivestars = ["Albedo","Diluc","Eula","Ganyu","Hu Tao","Jean","Keqing","Klee"
    ,"Mona","Qiqi","Tartaglia","Venti","Xiao","Zhongli"]
    fourstars = ["Amber","Beidou","Bennet","Chongyun","Diona","Fishcl","Kaeya"
    ,"Lisa","Ningguang","Noelle","Razor","Rosaria","Sucrose","Xiangling","Xingqiu","Xinyan"
    ,"Yanfei"]

    def __init__(self, roll):
        self.roll = roll

    def rng(self, roll):
        for _ in range(roll):
            rollit = random.uniform(0,100)
            yield rollit

    def gurantee(self):
        if self.count4s == 10:
            char = random.choice(self.fourstars)
            res = (f"4-Stars (Pity): {char}")
            self.count42 = 0
            return res
        elif self.count5s == 90:
            char = random.choice(self.fivestars)
            res = (f"5-Stars (Pity): {char}")
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
                    char = random.choice(self.fivestars)
                    print(f"5-Stars: {char}")
                    self.count5s = 0
                else: print(j)

            elif (98.00 > i >= 75.00):
                self.count5s += 1
                self.count4s += 1
                j = self.gurantee()
                if j is None:
                    char = random.choice(self.fourstars)
                    print(f"4-Stars: {char}")
                    self.count4s = 0
                else: print(j)
            
            else:
                self.count5s += 1
                self.count4s += 1
                j = self.gurantee()
                if j is None:
                    print("3-Stars: แตกไปไอสัส")
                else: print(j)
        return store, self.count5s, self.count4s

print("Welcome to this Mock-up Gacha Simulator\nInspired by the one and only:  Genshin Impact")
print("How much money do you wanna lose today?")
print("Enter a number of rolls")
ohho = int(input("> "))
hey = Gacha(ohho).nrolls()


"""
a = random.randrange(0,100,1); print(a)
b = random.uniform(0,100); print(b)
"""
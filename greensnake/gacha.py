import random
import numpy as np

class Gacha():
    count4s = 0
    count5s = 0
    tallyfive = np.array([])
    tallyfour = np.array([])
    tallythree = np.array([])

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
            res = (f"*4-Stars (Pity): {char}")
            self.tallyfour = np.append(self.tallyfour, char)
            self.count42 = 0
            return res
        elif self.count5s == 90:
            char = random.choice(self.fivestars)
            res = (f"**5-Stars (Pity): {char}")
            self.tallyfive = np.append(self.tallyfive, char)
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
                    print(f"**5-Stars: {char}")
                    self.count5s = 0
                    self.tallyfive = np.append(self.tallyfive, char)
                else: 
                    print(j)
                    self.tallyfive = np.append(self.tallyfive, char)

            elif (98.00 > i >= 85.00):
                self.count5s += 1
                self.count4s += 1
                j = self.gurantee()
                if j is None:
                    char = random.choice(self.fourstars)
                    print(f"*4-Stars: {char}")
                    self.count4s = 0
                    self.tallyfour = np.append(self.tallyfour, char)
                else: 
                    print(j)
                    self.tallyfour = np.append(self.tallyfour, char)
            
            else:
                self.count5s += 1
                self.count4s += 1
                j = self.gurantee()
                if j is None:
                    print("3-Stars: แตกไปไอสัส")
                    char = "salt"
                    self.tallythree = np.append(self.tallythree, char)
                else: 
                    print(j)
                    char = "salt"
                    self.tallythree = np.append(self.tallythree, char)
        
        if len(self.tallyfive) > 0:
            print(f"Total **5-Stars: {len(self.tallyfive)}")
            print(f": {self.tallyfive}")
        
        if len(self.tallyfour) > 0:
            print(f"Total *4-Stars: {len(self.tallyfour)}")
            print(f": {self.tallyfour}")

        if len(self.tallythree) > 0:
            #   I mean its never gonna happen, but who knows.
            print(f"Total trash: {len(self.tallythree)}")
            
        return store, self.count5s, self.count4s

print("Welcome to this Mock-up Gacha Simulator\nInspired by the one and only:  Genshin Impact")
print("How much money do you wanna lose today?")
print("Enter a number of rolls")
ohho = int(input("> "))
hey = Gacha(ohho).nrolls()

#   PSA, im never going to probably comment on my code - as long as its not 'explicitly' required.
#   So fuck you.


"""
a = random.randrange(0,100,1); print(a)
b = random.uniform(0,100); print(b)
"""
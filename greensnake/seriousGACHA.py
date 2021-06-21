import numpy as np 
import random as rd

m = ["well"]
class gacha():
    sssr = ["Chen"]
    ssr = ["Texas"]
    sr = ["Gravel"]
    r = ["Orchid"]
    def __init__(self, rolls):
        self.rolls = rolls
        self.ran = np.random.choice(4, self.rolls, p = [0.02, 0.08, 0.5, 0.4 ])
        
    def rng(self):
        for i in self.ran:
            if i == 0:
                a = "6 star: "+ np.random.choice(gacha.sssr) 
            elif i ==1:
                a = "5 star: "+ np.random.choice(gacha.ssr)
            elif i ==2:
                a = "4 star: "+ np.random.choice(gacha.sr)
            elif i ==3:
                a = "3 star: "+ np.random.choice(gacha.r)
            yield a 

    @classmethod
    def define(cls, cate, name):
        if cate == "sssr":
            cls.name = cls.sssr.append(name)
            return cls.sssr
        elif cate == "ssr":
            cls.name = cls.ssr.append(name)
            return cls.ssr
        elif cate == "sr":
            cls.name = cls.sr.append(name)
            return cls.sr
        elif cate == "r":
            cls.name = cls.r.append(name)
            return cls.r
        
"""
    def add_list(cls, name):
        cls.name = m.append(name)
        return m
"""    
    
         
    


"""
for val in gacha(5).rng():
    print(val)
"""
b = input("Type of character you wanna input>> ")
a = b.lower()
print(gacha.define(a, "Schawarz"))


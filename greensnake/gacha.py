import random

class Gacha():
    def __init__(self, roll):
        self.roll = roll

    def rng(self):
        rollit = random.uniform(0,100)
        return rollit
    
    def oneroll(self):
        res = self.rng()


a = random.randrange(0,100,1); print(a)
b = random.uniform(0,100); print(b)
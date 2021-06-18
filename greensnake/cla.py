import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as hentai

class Jean:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    
    def area(size):
        return size.width*size.length

r = Jean(5,10)
print("Area is:", r.area())

# มึงแก้อันนี้ให้กุดิ๊สัส
class Mona:
    def __init__(self, mu, sd):
        self.sd = sd
        self.mu = mu
    
    def normdist(tiger):
        x = np.arange(-2,2,0.01)
        y = hentai.norm.pdf(x, tiger.mu, tiger.sd)      
        return y

    def betadist(tiger):
        y = np.arange(-1,1,0.01)
        return y

print("Hi")
choice = input("> ")

try:
    if choice == 1:
        res = Mona(0,1).normdist()
        x = np.arange(-2,2,0.01)
        plt.plot(x, res)
        plt.show()
    elif choice == 2:
        res = Mona(0,1).betadist()
        x = np.arange(-2,2,0.01)
        plt.plot(x, res)
        plt.show()
except:
    print("kys")


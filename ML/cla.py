import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

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
    
    def normdist(self, mean, std):
        x = np.arange(-2,2,0.01)
        y = norm.pdf(x, mean.mu, std.sd)      
        return y


res = Mona(0,1).normdist(0.0,1.0)
x = np.arange(-2,2,0.01)
plt.plot(x, res)
plt.show()

"""
class Tiger:
    def __init__(self, inhere):
        self.inhere = inhere
    def whateverthisis(hentai):
        return hentai.inhere

print(Tiger(69).whateverthisis())
"""
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

folder = 'F:/whateverthisis/Basic-Image-Processing/images/malaria/'
files = os.listdir(folder)
total = len(files)
pos = 0
neg = 0
m = 0
o = 0
n = 0

imgdb1 = []
imgdb2 = []
imgdb3 = []
imgdb4 = []
imgdb5 = []

for i, file in enumerate(files):
    imageinput = cv2.imread(folder + file)

    height,width,depth = imageinput.shape
    b,g,r = cv2.split(imageinput)
    kernel = np.ones((3,3), np.uint8)
    image_noise_removal = cv2.bitwise_xor(g,r)

    ret, th = cv2.threshold(image_noise_removal, 150,255, cv2.THRESH_BINARY)
    close = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
    open = cv2. morphologyEx(close, cv2.MORPH_OPEN, kernel)
    cont, hie = cv2.findContours(open, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    bord = np.zeros([height, width, 3])
    cv2.drawContours(bord, cont, -1,(255,0,0),-1)
    
    if len(cont) >= 1:
        imgdb1.append(imageinput)
        imgdb2.append(th)
        imgdb3.append(close)
        imgdb4.append(bord)
        imgdb5.append(file)
        plt.subplot(1,4,1)
        plt.imshow(imageinput), plt.title(file)
        plt.subplot(1,4,2)
        plt.imshow(th, cmap='gray'), plt.title('Noisy')
        plt.subplot(1,4,3)
        plt.imshow(open, cmap='gray'), plt.title('Noise Reduction')
        plt.subplot(1,4,4)
        plt.imshow(bord, cmap='gray'), plt.title('Highlighted')
        plt.savefig("Fig"+str(n)+".png", format="PNG", bbox_inches='tight')
        n += 1
        m += 1
    else: neg += 1

for j in range(m):
        pos += 1 
        o+=1
        plt.subplot(m,4,o)
        plt.imshow(imgdb1[j]), plt.title(imgdb5[j])
        o+=1
        plt.subplot(m,4,o)
        plt.imshow(imgdb2[j], cmap ='gray'), plt.title('Noisy')
        o+=1
        plt.subplot(m,4,o)
        plt.imshow(imgdb3[j], cmap ='gray'), plt.title('Noise Reduction')
        o+=1
        plt.subplot(m,4,o)
        plt.imshow(imgdb4[j], cmap='gray'), plt.title('Highlighted')

print(pos); print(neg)
plt.show()
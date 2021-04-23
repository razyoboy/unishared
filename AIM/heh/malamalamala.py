import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

folder = 'F:/whateverthisis/Basic-Image-Processing/images/malaria/'
files = os.listdir(folder)

total = len(files)
Infected = 0
Uninfected = 0
a = []


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
    
    if len(cont) > 0:
        i = 1
        a.append(i)
    o = 0
    m = len(a)
    for j in range(m):
        o+=1
        plt.subplot(m,4,o)
        plt.imshow(imageinput), plt.title(file)
        o+=1
        plt.subplot(m,4,o)
        plt.imshow(th, cmap ='gray'), plt.title('Noisy')
        o+=1
        plt.subplot(m,4,o)
        plt.imshow(open, cmap ='gray'), plt.title('Sharpened')
        o+=1
        plt.subplot(m,4,o)
        plt.imshow(bord, cmap='gray'), plt.title('Color Dyed')

plt.show()
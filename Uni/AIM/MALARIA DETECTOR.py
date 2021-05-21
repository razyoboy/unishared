import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

folder = 'F:/whateverthisis/Basic-Image-Processing/images/malaria/' #subject to changed
files = os.listdir(folder)

total = len(files)
infected = 0
uninfected = 0
n = 0
for i, file in enumerate(files):
    image = cv2.imread(folder + file)
    
    #check directory 
    """
    cv2.imshow('check',image)   
    cv2.waitKey(0) #open all pictures
    """
    height, width, depth = image.shape
    b,g,r = cv2.split(image)
    kernel = np.ones((3,3), np.uint8) #random
    xor = cv2.bitwise_xor(g,r) #for error reducing 
    # if it reaches 165 then >>>= 255
    ret, threshold = cv2.threshold(xor,150,255, cv2.THRESH_BINARY) #random threshold until satisfied
    #closing > dilation following by erosion (remove insider noises)
    closing = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)
    #opening > erosion following by dilation (remove outsider noises)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
    #contours > border for malaria if python detect
    contours, hierachy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    border = np.zeros([height,width, 3])
    cv2.drawContours(border, contours, -1,(255,0,0),-1)

    if len(contours) > 0:
        plt.subplot(1,4,1)
        plt.imshow(image), plt.title(file)
        plt.subplot(1,4,2)
        plt.imshow(threshold, cmap='gray'), plt.title('Noisy')
        plt.subplot(1,4,3)
        plt.imshow(opening, cmap='gray'), plt.title('Noise Reduction')
        plt.subplot(1,4,4)
        plt.imshow(border, cmap='gray'), plt.title('Highlighted')
        plt.savefig("Fig"+str(n)+".png", format="PNG", bbox_inches='tight')
        n += 1
        if file.startswith('parasitized') and len(contours) > 0:
            infected = infected + 1
    elif file.startswith('uninfected') and len(contours) == 0:
        uninfected = uninfected + 1

print('Malaria detected >>',(infected),'Malaria undetected >>',(uninfected))
print('From total parasitized = 20 \nSENSITIVITY =',(int(infected)/20)*100,'%')
print('From total uninfected = 76 \nSPECIFICITY =',(int(uninfected)/76)*100,'%')

#if use xor = cv2.bitwise_xor(g,b) 19 is infected instead of 20
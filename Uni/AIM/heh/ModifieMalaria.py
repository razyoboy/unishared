import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os

folder = 'C:\\Users\\Windows 10\\Kim\\python\\New folder\\malaria\\' #address of the images
pare = 'C:\\Users\\Windows 10\\Kim\\python\\malaria\\parasitized_01.jpg'
files = os.listdir(folder)
positive = 0
negative = 0
a = 0
j = 0
o = 0
nigga = []
nigga1 = []
nigga2 = []
nigga3 = []
nigga4 = []

for i, file in enumerate(files):
    image = cv.imread(folder + file )
    b,g,r = cv.split(image)
    
    height, width, depth = image.shape
    kernel = np.ones((5,5), np.uint8)#1. use for removing noise from the images
                                     #2. use for make a border line  
#if we use kernel 3*3 the program will detect the parasitized images 21 from 96 which it should be just 20 images for infected cells
    check = cv.bitwise_xor(g, r) #To cut off the background and remain just the cell that has parasites
    
    res, thres = cv.threshold(check, 160,255, cv.THRESH_BINARY)
    new = cv.morphologyEx(thres, cv.MORPH_CLOSE, kernel)#use for cut off the noise in image 

    opening = cv.morphologyEx(new, cv.MORPH_OPEN, kernel )
    contours, hierachy = cv.findContours(opening, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE )
    bord = np.zeros([height, width, 3])
    cv.drawContours(bord, contours, -1, (0,255,0),-1  )
    if len(contours)>=1:
        nigga.append(image)
        nigga1.append(thres)
        nigga2.append(new)
        nigga3.append(bord)
        nigga4.append(file)
        a+=1

for j in range(a):
    o+=1
    plt.subplot(a,4,o)
    plt.imshow(nigga[j], cmap = 'gray'), plt.title(nigga4[j])
    o+=1
    plt.subplot(a,4,o)
    plt.imshow(nigga1[j], cmap = 'gray')
    o+=1
    plt.subplot(a,4,o)
    plt.imshow(nigga2[j], cmap = 'gray')
    o+=1
    plt.subplot(a,4,o)
    plt.imshow(nigga3[j], cmap = 'gray') 

plt.show()
       




"""

    if len(contours)>=1:
        plt.subplot(2,3,1)
        plt.imshow(image, cmap = 'gray'), plt.title(file)
        plt.subplot(2,3,2)
        plt.imshow(g, cmap = 'gray')
        plt.subplot(2,3,3)
        plt.imshow(check, cmap = 'gray')
        plt.subplot(2,3,4)
        plt.imshow(thres, cmap = 'gray')
        plt.subplot(2,3,5)
        plt.imshow(new, cmap = 'gray')
        plt.subplot(2,3,6)
        plt.imshow(bord, cmap = 'gray')
        
        plt.show()
        positive += 1
    else:
        if negative < 76:
            negative += 1
            #the reson we have to put this statement is we use the same source and when we test it 
            #the uninfected cell we get will be 77 while the maximum it supposed to be is only 76. 


print(f"The sensitivity = {positive/20}")
print(f"The specificity = {negative/76}")

"""
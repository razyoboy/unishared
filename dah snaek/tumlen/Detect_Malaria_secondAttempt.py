import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os

folder = 'D:\\KIM\\ProgEmer\\Pan\\malaria\\' #warning use the directory of your file only[this is my directory]
files = os.listdir(folder)
"""
a=cv.imread(folder+files[0])
cv.imshow('hi', a)
cv.waitKey(0)
print(folder+files[0])v 
"""#Just check how does syntax work
total = len(files)
positive = 0


for i, file in enumerate(files):
    original_image = cv.imread(folder+file)
    
    #cv.imshow('hi', original_image)
    #cv.waitKey(0)
    #warning Dont use the above syntax if the folder contains many images
    height, width, depth = original_image.shape
    r,g,b = cv.split(original_image)
    new_image = cv.merge([r*5,g,b])
    new_image_gray = cv.cvtColor(new_image, cv.COLOR_BGR2GRAY)
    use = cv.bitwise_xor(new_image_gray, r)
    res, thereshold = cv.threshold(use, 130, 255, cv.THRESH_BINARY)
    kernel = np.ones((1,1), np.uint8)
    opening = cv.morphologyEx(thereshold, cv.MORPH_OPEN, kernel )
    contours, hierachy = cv.findContours(opening, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE )
    bord = np.zeros([height, width, 3])
    cv.drawContours(bord, contours, -1, (0,255,0),-1  )
    
    #plt.subplot(10,10,i+1)
    #plt.imshow(bord, cmap = 'gray'), plt.title(i)
    #plt.show() 
    #still no clue how to plot all "bord" in the same subplot
    if len(contours)>0:
        positive +=1
   
print("the accuracy of the system is >>", positive/total)





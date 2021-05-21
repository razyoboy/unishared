import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os

folder = 'D:\\KIM\\ProgEmer\\Pan\\pills\\'
files = os.listdir(folder)
for i, file in enumerate(files):
    Pills = cv.imread(folder+file)
    height, width, depth = Pills.shape
    """
    hsv = cv.cvtColor(Pills, cv.COLOR_BGR2HSV)
    h,s,v = cv.split(hsv)
    s = s-70
    v = v*10
    hsv = cv.merge([h,s,v])
    new_pill = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
    grey = cv.cvtColor(new_pill, cv.COLOR_BGR2GRAY)
    """ #The result I got is not satisfied. So, I wont use them
    r,g,b = cv.split(Pills)
    Hi = cv.bitwise_or(r,b)# The images I got are brighter than the original ones So I think I can use it 
    
    #B,G,R = cv.split(new_pill)# -------------------Nothing different from b g r respectively
    res, thereshold = cv.threshold(Hi, 170, 255, cv.THRESH_BINARY)
    kernel = np.ones((25,25), np.uint8)
    opening = cv.morphologyEx(thereshold, cv.MORPH_OPEN, kernel)
    contours, hierachy = cv.findContours(opening, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE )
    border = np.zeros([height, width, 3])
    cv.drawContours(border, contours, -1, (0,255,0),3 )
    print(f"image {i+1} >> no. of pills equal >> {len(contours)}")

    plt.subplot(2,2,1)
    plt.imshow(Pills, cmap = 'gray'), plt.title(file)
    plt.subplot(2,2,2)
    plt.imshow(thereshold, cmap = 'gray'), plt.title(file)
    plt.subplot(2,2,3)
    plt.imshow(Hi, cmap = 'gray')
    plt.subplot(2,2,4)
    plt.imshow(border, cmap = 'gray')
    plt.show()
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

folder = 'F:/whateverthisis/Basic-Image-Processing/images/hela/'
files = os.listdir(folder)

total = len(files)
f, axs = plt.subplots(figsize=(15,total*6))
n = 0 #For saving and naming files
imgdb1 = [] #DB for filenames of each images
imgdb2 = [] #DB for processed images
imgdb3 = [] #DB for contoured images
imgdb4 = [] #DB for number of contours (cells)

for i, file in enumerate(files):
    image = cv2.imread(folder + file)
    #Converting BGR to HSV for ease of manipulation
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #Increasing the intensity of the images
    hsv = image * 15
    gray = hsv.copy() #Preparation to be contoured
    opening = hsv.copy() #Preparation to be contoured as well

    #Converting the now seeable images into Grayscale
    grayit = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
    #Data for creating matrix of ones
    height, width = grayit.shape

    #Creating threshold level for cutting and rounding color levels
    ret, thresh = cv2.threshold(grayit, 80, 255, cv2.THRESH_BINARY)

    #To create a color inverted image for ease of reading for the computer
    inverted = cv2.bitwise_not(thresh)
    kernel = np.ones((50,50), np.uint8)
    opening = cv2.morphologyEx(inverted, cv2.MORPH_OPEN, kernel)
    
    #Creating contours
    count, hiera = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    bord = np.zeros([height,width,3])

    cv2.drawContours(bord, count, -1,(0,255,0),3)

    #For appending each corresponding data into an array
    imgdb1.append(file)
    imgdb2.append(gray)
    imgdb3.append(opening)
    imgdb4.append(len(count))


#   The above data and results are stored in an array so that images 
#   can be easily saved and exported without taking to much time and effort

for j in range(len(imgdb1)):
    plt.subplot(121)
    plt.title(imgdb1[j]) #Calling the j element for filenames
    plt.imshow(imgdb2[j], cmap=plt.cm.gray) #Calling the j element for processed images
    plt.subplot(122)
    
    #Calling the j element for the number of contours found
    plt.title('No. of cells = ' + str(imgdb4[j]))
    plt.imshow(imgdb3[j], cmap=plt.cm.gray)
    #n is simply there for saving files with different filenames
    n += 1
    plt.savefig("Cont"+str(n)+".png", format="PNG", bbox_inches='tight')







import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

folder = 'F:/whateverthisis/Basic-Image-Processing/images/malaria/'
files = os.listdir(folder)
total = len(files)

#Initialization for each parameters that we would use
pos = 0 #For positive results
neg = 0 #For negative results
m = 0 #For the m element of subplot(m,n,p)
p = 0 #For the p element of subplot(m,n,p)
n = 0 #For the n element of subplot(m,n,p)

#Databases (arrays) for storing each images after their iterations
imgdb1 = [] #For the original images
imgdb2 = [] #For the noised images
imgdb3 = [] #For the noise-reduced images
imgdb4 = [] #For the highlighted images
imgdb5 = [] #For the filenames of each images

for i, file in enumerate(files):
    imageinput = cv2.imread(folder + file)

    height,width,depth = imageinput.shape
    #spliting BGR channels into their seperate one
    b,g,r = cv2.split(imageinput)
    #The matrix of ones can be changed for an acceptable accuracy
    kernel = np.ones((3,3), np.uint8)
    #Apply noise removal via bitwise operator XOR
    image_noise_removal = cv2.bitwise_xor(g,r) 

    #   Apply thresholding, the threshold value can be changed
    #   for an acceptable accuracy
    ret, th = cv2.threshold(image_noise_removal, 150,255, cv2.THRESH_BINARY)
    #   Apply the Closing technique, dilation is performed
    #   first; then erosion followed 
    close = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)
    #   Apply the Opening technique, 
    #   erosion first; dilation follows
    open = cv2. morphologyEx(close, cv2.MORPH_OPEN, kernel)
    #Creating contours 
    cont, hie = cv2.findContours(open, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    bord = np.zeros([height, width, 3])
    cv2.drawContours(bord, cont, -1,(255,0,0),-1)
    
    #   Apply conditional, 
    #   if the detected contour is greater than one, then mark
    #   that as positive and collect the results
    #   Else, it is classified as a negative

    if len(cont) >= 1:
        pos += 1 

        #Appending each corresponding data into its respective array
        imgdb1.append(imageinput)
        imgdb2.append(th)
        imgdb3.append(close)
        imgdb4.append(bord)
        imgdb5.append(file)
        
        #   Below is for the image saving automation with each 
        #   images processed one at a time
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

#   For plotting and showing the results where the plot would dynamically scale
#   based on the number of detected images (m)

for j in range(m):
        p += 1 #For increasing the p element, so that it can plot properly
        plt.subplot(m,4,p)
        plt.imshow(imgdb1[j]), plt.title(imgdb5[j])
        p += 1
        plt.subplot(m,4,p)
        plt.imshow(imgdb2[j], cmap ='gray'), plt.title('Noisy')
        p += 1
        plt.subplot(m,4,p)
        plt.imshow(imgdb3[j], cmap ='gray'), plt.title('Noise Reduction')
        p += 1
        plt.subplot(m,4,p)
        plt.imshow(imgdb4[j], cmap='gray'), plt.title('Highlighted')

print(f"{pos} are detected"); print(f"{neg} are not detected") #Printing positive results and negative results
plt.show()
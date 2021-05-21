import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import os

folder = 'D:\\KIM\\ProgEmer\\Pan\\malaria\\' #This is my own directory, use your own
file = folder + 'parasitized_01.jpg'

  
original_img = cv.imread(file)
#cv.imshow("hi",original_img) #: To check the image was read or not
#cv.waitKey(0)

height, width, depth = original_img.shape
r,g,b = cv.split(original_img)
blank = np.zeros([height, width], np.uint8)# dont know the reason why we use np.uint8

"""
r_new = cv.merge([r*20, blank, blank])
g_new = cv.merge([blank, g*10, blank])
b_new = cv.merge([blank, blank, b*10])
"""#Just try somethings but the result wouldnt satisfy so I wont use it
new_img = cv.merge([r*5, g, b])
new_img_gray = cv.cvtColor(new_img, cv.COLOR_BGR2GRAY)
#important ----------------------
#-----------------------------------------------------------
ima = cv.bitwise_xor(new_img_gray, r) #interesting"""--------------------------------------
#This one can cut the black border off so Im gonna use this one
re, there = cv.threshold(ima, 130, 255, cv.THRESH_BINARY) #interest"""---------------------
#-----------------------------------------------------------
"""
img_cutoff = cv.bitwise_and(new_img_gray, r)#the reason we cant use cv.bitwise_and(new_img_gray, new_img)
                                            #the first one is in gray scale which the number of array is not the 
                                            #same as the second one so it lead to conflict.
res, thereshold = cv.threshold(img_cutoff, 100, 255, cv.THRESH_BINARY)
#the image is much more clearer. Then, I will find the contour to identify where the parasite is 
inv_img = cv.bitwise_not(thereshold)#for finding border


kernel = np.ones((5,5), np.uint8)
opening = cv.morphologyEx(inv_img, cv.MORPH_OPEN, kernel)
contours, hierarchy = cv.findContours(opening, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
border = np.zeros([height, width, 3])
cv.drawContours(border, contours, -1, (0,255,0), -1)
"""    
kernel = np.ones((1,1), np.uint8) #Kernel size 5*5 is too big So I use 1*1 instead
opening = cv.morphologyEx(there, cv.MORPH_OPEN, kernel )
contour, hier = cv.findContours(opening, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE )
bord = np.zeros([height, width, 3])
cv.drawContours(bord, contour, -1, (0,255,0),-1  )

"""
hsv = cv.cvtColor(original_img, cv.COLOR_BGR2HSV)
#we gonna increase the brightness of the image to make the color more easily to detect

h,s,v = cv.split(hsv)
v = v*10  
hsv = cv.merge([h,s,v])
hsv_back = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
#convert the picture back to BGR channal
new_img_hsv = cv.cvtColor(hsv_back, cv.COLOR_BGR2GRAY)
"""#The image is not as good as I thought so I wont use it
plt.subplot(4,4,1)
plt.imshow(original_img, cmap = 'gray')
plt.subplot(4,4,2)
plt.imshow(r, cmap = 'gray')
plt.subplot(4,4,3)
plt.imshow(new_img_gray, cmap = 'gray') #after comparing r & new_img_gray almost similar but there are some points
                                        #that not the same so I will use bitwisw_and to cut off the diference
plt.subplot(4,4,4)
plt.imshow(new_img, cmap = 'gray')
plt.subplot(4,4,5)
plt.imshow(ima, cmap = 'gray')
"""
plt.imshow(img_cutoff, cmap = 'gray') #the parasite in the cell is more clearer than r and new_img_gray 
plt.subplot(4,4,6)
plt.imshow(thereshold, cmap = 'gray')#see? after I applied cv.thereshold the color remain just black and white 
                                    #and now we can see the parasite much more clearer
plt.subplot(4,4,7)
plt.imshow(border, cmap = 'gray'), plt.title("DONE!!!")
"""

plt.subplot(4,4,6)
plt.imshow(there, cmap= 'gray')
plt.subplot(4,4,7)
plt.imshow(bord, cmap ='gray')
plt.show()





import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

folder = 'F:/whateverthisis/Basic-Image-Processing/images/'
lenna = folder + 'lenna.png'
apple = folder + 'apples.jpg'
chess = folder + 'chess.png'

image = cv2.imread(chess)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#cv2.imshow('Check',image)   
#cv2.waitKey(0) 
image = cv2.resize(image, (800,800))
height, width, depth = image.shape

print(f"This image is {width} x {height} with {depth} channels")

f, axs = plt.subplots(figsize=(15,15))
plt.subplot(221)
plt.imshow(image)

print('I wanted to see the Queen')
queen = image[700:800, 300:400]

plt.subplot(222)
plt.imshow(queen)

new = image.copy()
oho = new[700:800, 400:500]
plt.subplot(223)
plt.imshow(oho); plt.show()

lenn = cv2.imread(lenna)
lenn = cv2.cvtColor(lenn, cv2.COLOR_BGR2RGB)
height, width, depth = lenn.shape

blank = np.zeros([height,width], np.uint8)
red, green, blue = cv2.split(lenn)

redthemselves = cv2.merge([red, blank, blank])
greenlantern = cv2.merge([blank, green, blank])
bluelabel = cv2.merge([blank, blank, blue])

f, axs = plt.subplots(figsize=(15,15))
plt.subplot(231)
plt.imshow(redthemselves)
plt.subplot(232)
plt.imshow(greenlantern)
plt.subplot(233)
plt.imshow(bluelabel)

hsv_lenna = cv2.cvtColor(lenn, cv2.COLOR_RGB2HSV)
hue, sat, val = cv2.split(hsv_lenna)
plt.subplot(234)
plt.imshow(hue, cmap=plt.cm.gray)
plt.subplot(235)
plt.imshow(sat, cmap=plt.cm.gray)
plt.subplot(236)
plt.imshow(val, cmap=plt.cm.gray)
plt.show()
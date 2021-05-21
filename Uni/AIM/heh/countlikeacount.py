import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

folder = 'F:/whateverthisis/Basic-Image-Processing/images/'
clips = folder + 'clips.jpg'


image = cv2.imread(clips)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

grayit = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
height, width = grayit.shape

ret, thresh = cv2.threshold(grayit, 80, 255, cv2.THRESH_BINARY)

inverted = cv2.bitwise_not(thresh)

kernel = np.ones((50,50), np.uint8)
opening = cv2.morphologyEx(inverted, cv2.MORPH_OPEN, kernel)

count, hiera = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
bord = np.zeros([height,width,3])

cv2.drawContours(bord, count, -1,(0,255,0),3)
print('count=', len(count))

f, axs = plt.subplots(figsize=(15,15))
plt.subplot(141)
plt.imshow(image)
plt.subplot(142)
plt.imshow(inverted, cmap=plt.cm.gray)
plt.subplot(143)
plt.imshow(opening, cmap=plt.cm.gray)
plt.subplot(144)
plt.imshow(bord)
plt.show()
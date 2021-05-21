import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

folder = 'F:/whateverthisis/Basic-Image-Processing/images/'
question = folder + 'apples02.jpg'

original = cv2.imread(question)
#Converting BGR to RGB for comparision
original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
image = cv2.imread(question)
#Convert the color mode to HSV for ease of manipulation
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#So that we can compare both images
out = image.copy()
#Spliting the three channels and increasing the hue channel for the green color
h, s, v = cv2.split(out)
h += 55

#Combine them back into a 3-channel image
greenlantern = cv2.merge([h,s,v])
#Converting HSV back into RGB color space
out = cv2.cvtColor(greenlantern, cv2.COLOR_HSV2RGB)

f, axs = plt.subplots(figsize=(15,15))
plt.subplot(121)
plt.imshow(original); plt.title('Original')
plt.subplot(122)
plt.imshow(out); plt.title('Manipulated')
plt.savefig("ApplesGreen"+".png", format="PNG", bbox_inches='tight')
plt.show()

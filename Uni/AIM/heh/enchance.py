import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

folder = 'F:/whateverthisis/Basic-Image-Processing/images/'
question = folder + 'hela/01.png'

image = cv2.imread(question)
out = image.copy()
hsv = cv2.cvtColor(out, cv2.COLOR_BGR2HSV)

out = image * 15
f, axs = plt.subplots(figsize=(15,15))
plt.subplot(211); plt.imshow(image)
plt.subplot(212); plt.imshow(out)
plt.show()


#apple
#mito

#exer 3 and 4
#assign 1

#do not exceed 3 if possible

#explain steps

#email in github

#chunchat02@gmail.com

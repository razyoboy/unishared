import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

path = r'D:\KIM\ProgEmer\Pan\mitosis.jpg'
a = cv.imread(path)
z = cv.imread(path)
kernel = np.ones((5,5),np.uint8)
Morph = cv.morphologyEx(a, cv.MORPH_GRADIENT, kernel)
b = cv.bitwise_not(Morph,  a)
c = cv.cvtColor(b, cv.COLOR_BGR2GRAY)
#cv.imshow("hi.jpg",Morph)
#cv.waitKey(0)
plt.subplot(2,2,1), plt.imshow(z, cmap = 'gray')
plt.title('Original')
plt.subplot(2,2,2), plt.imshow(Morph, cmap = 'gray')
plt.title('Morphology')
plt.subplot(2,2,3), plt.imshow(b, cmap='gray')
plt.title('Not')
plt.subplot(2,2,4), plt.imshow(c, cmap= 'gray')
plt.title('Gray')
plt.show()
import cv2
import matplotlib.pyplot as plt
import numpy as np

folder = 'C:/Users/wendy/Desktop/'
pills = folder + 'noisypill.jpg'

#   Read the input images
img = cv2.imread(pills)
#   Contours only support Grayscaled images,
#   so conversion is needed.
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#   120, 255 are from trial and errors, which
#   proves to be the most accurate one.
res, th = cv2.threshold(imggray, 120, 255, cv2.THRESH_BINARY_INV)

#   Invert the image through bitwise operator.
inv = cv2.bitwise_not(th)
kernel = np.ones((5,5), np.uint8)
#   Perform erosion and dilation
#   Again, the kernel are from trial and errors,
#   which using this is the most accurate.
ero = cv2.erode(inv, kernel)
kernel = np.ones((20,20), np.uint8)
dilate = cv2.dilate(ero, kernel)

#   Then find the contours, this is extremely delicate
#   Hence why all of the above must be done first
#   In order to get a valid result.

count, hiera = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
height, width, depth = img.shape
bord = np.zeros([height,width,3])
cv2.drawContours(bord, count, -1,(0,255,0),-1)

#   Then print the counted number of pills
#   which is stored in an array.
length = len(count)
print(f"Counted pills = {length}")
plt.imshow(bord, cmap='gray')
plt.savefig("outpills"+".png", format="PNG", bbox_inches='tight')
plt.show()

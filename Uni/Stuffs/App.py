import numpy as np
import cv2 as cv
"""
from matplotlib import pyplot as plt
path = r'D:\KIM\ProgEmer\Pan\apple.jpg'
a = cv.imread(path)
window_name = 'image'
cv.imshow(window_name,a)
cv.waitKey(0)
"""
path = r'D:\KIM\ProgEmer\Pan\apple.jpg'
image = cv.imread(path)
hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)
low_red = np.array([161, 155, 84])
high_red = np.array([179, 255, 255])
mask=cv.inRange(hsv,low_red,high_red) 
image[mask>0]=(0,255,0)
cv.imwrite("result.png",image)
cv.imshow("Hi", image)
cv.waitKey(0)

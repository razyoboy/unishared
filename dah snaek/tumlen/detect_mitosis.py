import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

path = r'C:\Users\Windows 10\OneDrive\เอกสาร\GitHub\gittest\gittest\tumlen\hela\01.png'
#file = path + '\01.png'
image = cv.imread(path)
cv.imshow("i", image)
cv.waitKey(0)
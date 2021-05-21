
import cv2
import matplotlib.pyplot as plt
import numpy as np
folder = 'C:/Users/wendy/Desktop/ohshit/'
c1 = folder + 'circle1.jpg'
c2 = folder + 'circle2.jpg'
c3 = folder + 'circle3.jpg'
rec = folder + 'rectangle.jpg'
'''
img1 = cv2.imread(c1)
img2 = cv2.imread(c2)
img3 = cv2.imread(c3)

img4 = cv2.bitwise_xor(img1, img2)
out = cv2.bitwise_and(img3, img4)

plt.imshow(out)
plt.savefig("out1"+".png", format="PNG", bbox_inches='tight')
plt.show()
'''

img = cv2.imread(rec)                    
erode = cv2.erode(img, np.ones((5,5), np.uint8))
dilate = cv2.dilate(erode, np.ones((5,5), np.uint8))

plt.imshow(dilate)
plt.savefig("out2"+".png", format="PNG", bbox_inches='tight')
plt.show()

















'''
a = len([c for c in 'Python' if c in 'Programming'])
print(a)
'''
'''
n = 8
f = []
for i in range(8):
  if len(f) < 2: f += [1]
  else: f += [f[-1] + f[-2]]
print(f)
'''
'''
labelled = [0, 0, 0, 1, 1]
detected = [0, 0, 0, 0, 1]
tp, tn, fp, fn = 0, 0, 0, 0
for i in range(5):
  if labelled[i] and detected[i]:
    tp += 1
  elif not labelled[i] and detected[i]:
    fp += 1
  elif labelled[i] and not detected[i]:
    fn += 1
  elif not labelled[i] and not detected[i]:
    tn += 1
print('sensitivity', tp/(tp+fn))
print('specificity', tn/(tn+fp))
print('accuracy', (tp+tn)/(tp+fp+tn+fn))
'''
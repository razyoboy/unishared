import os
import cv2
import numpy as np

def operate(image1, image2):
	global bw_and, bw_or, bw_not, bw_xor
	bw_not = cv2.bitwise_not(image2)
	bw_and = cv2.bitwise_and(image1, image2)
	bw_or = cv2.bitwise_or(image1, image2)
	bw_xor = cv2.bitwise_xor(image1, image2)

def concat(img1, img2, img3, img4, img5, img6):
	top = cv2.hconcat([img1, img2, img3])
	down = cv2.hconcat([img4, img5, img6])
	out = cv2.vconcat([top, down])
	out = cv2.line(out, (0, h), (w*3, h), 127, 1)
	out = cv2.line(out, (w, 0), (w, h*2), 127, 1)
	out = cv2.line(out, (w*2, 0), (w*2, h*2), 127, 1)
	return out

def display(image):
	image = cv2.resize(image, (0, 0), fx=scale, fy=scale, interpolation = cv2.INTER_AREA)
	cv2.imshow('display', image)

def mouse_event(event, x, y, flags, param):
	global mouse

	# update cursor position
	if event == cv2.EVENT_MOUSEMOVE:
		x = x // scale
		y = y // scale
		if y < h and x < w:

			# mouse movement
			image1 = np.zeros([h, w], np.uint8)
			cv2.circle(image1, (x, y), radius, (255, 255, 255), -1)

			# bitwise operations
			operate(image1, image2)
	
			# display
			display(concat(image1, image2, bw_not, bw_and, bw_or, bw_xor))

if __name__ == '__main__':

	# root directory
	root = os.path.dirname(os.path.abspath(__file__))
	files = ['circle.png', 'window.png', 'sky.png', 'butterfly.png', 'board.png', 'deathlyhallows.png',  'text.png']
	total = len(files)

	# parameter
	h, w = 200, 200,
	scale = 2
	radius = 30
	mouse = (0, 0)
	index, view = 0, 0

	# images
	image1 = np.zeros([h, w], np.uint8)
	image2 = np.zeros([h, w], np.uint8)
	bw_and = np.zeros([h, w], np.uint8)
	bw_or  = np.zeros([h, w], np.uint8)
	bw_not = np.zeros([h, w], np.uint8)
	bw_xor = np.zeros([h, w], np.uint8)

	while True:

		# load image + info
		image_path = os.path.join(root, 'images', files[index])
		image2 = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
		image2 = cv2.resize(image2, (h, w))

		# bitwise operations
		operate(image1, image2)
	
		# display
		display(concat(image1, image2, bw_not, bw_and, bw_or, bw_xor))

		# user feedback
		cv2.setMouseCallback('display', mouse_event)
		key = cv2.waitKeyEx(0)
		if key in [ord('q'), 27]:
			break
		elif key in [ord('a'), 2424832]:
			index = max(index - 1, 0)
		elif key in [ord('d'), 2555904]:
			index = min(index + 1, total - 1)
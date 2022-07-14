import cv2 
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../photos/grey1.jpeg', 0)
ret, img_aft = cv2.threshold(img, 140, 220, cv2.THRESH_BINARY)
	
def grey_hist(image):
	# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	#compute histogram
	hist = cv2.calcHist([image], [0], None, [256], [0, 256])

	# matplotlib expects RGB images so convert and then display the image
	# with matplotlib
	plt.figure()
	plt.axis("off")
	plt.imshow(cv2.cvtColor(image, cv2.COLOR_GRAY2RGB))
	# plot the histogram
	plt.figure()
	plt.title("Grayscale Histogram")
	plt.plot(hist)
	plt.xlim([0, 256])

	plt.show()

	# normalize the histogram
	# hist /= hist.sum()
	# # plot the normalized histogram
	# plt.figure()
	# plt.title("Grayscale Histogram (Normalized)")
	# plt.xlabel("Bins")
	# plt.ylabel("% of Pixels")
	# plt.plot(hist)
	# plt.xlim([0, 256])
	# plt.show()

# grey_hist(img)
grey_hist(img_aft)

# cv2.imshow('Thress
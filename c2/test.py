# import Opencv
import cv2
  
# import Numpy
import numpy as np
import imutils
from matplotlib import pyplot as plt


a = cv2.imread('../photos/dragon.jpeg')
img = cv2.cvtColor(a, cv2.COLOR_BGR2YCR_CB)

#spliting channel
y, cb, cr = cv2.split(img)

y = cv2.equalizeHist(y)

#merging channel
image_merge = cv2.merge([y, cb, cr])
b = cv2.cvtColor(image_merge, cv2.COLOR_YCrCb2BGR)
# res = np.hstack((a, b))
# cv2.imshow('B-A', res)

# cv2.waitKey(0)

def d2_bgr(image):
	# split the image into its respective channels, then initialize the
	# tuple of channel names along with our figure for plotting
	chans = cv2.split(image)
	colors = ("b", "g", "r")
	plt.figure()
	plt.title("'Flattened' Color Histogram")
	plt.xlabel("Bins")
	plt.ylabel("# of Pixels")

	# loop over the image channels
	for (chan, color) in zip(chans, colors):
		# create a histogram for the current channel and plot it
		hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
		plt.plot(hist, color=color)
		plt.xlim([0, 256])
		plt.ylim([0, 5000])
		# create a new figure and then plot a 2D color histogram for the
	

	# display the original input image
	plt.figure()
	plt.axis("off")
	plt.imshow(imutils.opencv2matplotlib(image))
	# show our plots
	plt.show()

d2_bgr(a)
d2_bgr(b)
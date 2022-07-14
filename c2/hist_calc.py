#https://pyimagesearch.com/2021/04/28/opencv-image-histograms-cv2-calchist/
#https://prateekvjoshi.com/2013/11/22/histogram-equalization-of-rgb-images/#:~:text=Histogram%20equalization%20is%20applicable%20to,it%20wouldn't%20make%20sense.
#https://pyimagesearch.com/2021/02/08/histogram-matching-with-opencv-scikit-image-and-python/
from matplotlib import pyplot as plt
import cv2
import imutils
import numpy as np
from skimage import exposure

g_img = cv2.imread('../photos/grey1.jpeg', 0)
rgb_img = cv2.imread('../photos/italy.jpg')
ref_pic = cv2.imread('../photos/red_hist.jpg')

def grey_hist(image):
	image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
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
	plt.xlabel("Bins")
	plt.ylabel("# of Pixels")
	plt.plot(hist)
	plt.xlim([0, 256])

	# normalize the histogram
	hist /= hist.sum()
	# plot the normalized histogram
	plt.figure()
	plt.title("Grayscale Histogram (Normalized)")
	plt.xlabel("Bins")
	plt.ylabel("% of Pixels")
	plt.plot(hist)
	plt.xlim([0, 256])
	plt.show()



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
		# plt.ylim([0, 50000])
		# create a new figure and then plot a 2D color histogram for the
	

	# display the original input image
	plt.figure()
	plt.axis("off")
	plt.imshow(imutils.opencv2matplotlib(image))
	# show our plots
	plt.show()

def grey_balancing(img):
	# creating a Histograms Equalization
	# of a image using cv2.equalizeHist()
	equ = cv2.equalizeHist(img)
	  
	# stacking images side-by-side
	res = np.hstack((img, equ))
	  
	# show image input vs output
	cv2.imshow('Before-After', res)
	  
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def rgb_balancing(img):
	#converting to ycrcb color space
	a = img
	img = cv2.cvtColor(a, cv2.COLOR_BGR2YCR_CB)

	#spliting channel
	y, cb, cr = cv2.split(img)

	y = cv2.equalizeHist(y)
	# g = cv2.equalizeHist(g)
	# r = cv2.equalizeHist(r)
	#merging channel
	image_merge = cv2.merge([y, cb, cr])
	#convert back to rgb
	b = cv2.cvtColor(image_merge, cv2.COLOR_YCrCb2BGR)

	res = np.hstack((a, b))
	cv2.imshow('B-A', res)

	cv2.waitKey(0)

def hist_matching(src, ref):
	# load the source and reference images
	print("[INFO] loading source and reference images...")

	# determine if we are performing multichannel histogram matching
	# and then perform histogram matching itself
	print("[INFO] performing histogram matching...")
	# multi = True if src.shape[-1] > 1 else False
	matched = exposure.match_histograms(src, ref, multichannel=True)
	# show the output images
	cv2.imshow("Source", src)
	cv2.imshow("Reference", ref)
	cv2.imshow("Matched", matched)
	cv2.waitKey(0)

# grey_hist(g_img)
d2_bgr(rgb_img)
# grey_balancing(g_img)
# rgb_balancing(rgb_img)
# hist_matching(rgb_img, ref_pic)
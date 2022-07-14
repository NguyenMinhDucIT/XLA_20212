# import the necessary packages
from skimage import exposure
import matplotlib.pyplot as plt
import cv2


# load the source and reference images
print("[INFO] loading source and reference images...")
src = cv2.imread('../photos/dragon.jpeg')
ref = cv2.imread('../photos/red_hist.jpg')
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
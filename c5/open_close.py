import cv2 as cv
import numpy as np


img = cv.imread('../photos/color_noise.jpeg')
kernel = np.ones((5,5),np.uint8)

# that's it for now
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
res = np.hstack((img, opening, closing))
cv.imshow('Before-Open-Close', res)
cv.waitKey(0)


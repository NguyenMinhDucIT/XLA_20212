#3. Lập trình ứng dụng cải thiện độ tương phản ảnh dùng các hàm phép toán điểm ảnh
#(hàm tuyến tính, hàm ngưỡng, hàm phi tuyến) 

import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('../photos/grey1.jpeg', 0)
ret, img_aft = cv2.threshold(img, 140, 220, cv2.THRESH_BINARY)

def compute_hist(img):
    hist = np.zeros((256,), np.uint8)
    h, w = img.shape[:2]
    for i in range(h):
        for j in range(w):
            hist[img[i][j]] += 1
    return hist




hist = compute_hist(img_aft).ravel()
       
fig1 = plt.figure()
ax = plt.subplot(121)
plt.imshow(img_aft, cmap='gray')

plt.subplot(122)
plt.plot(hist)
plt.show()



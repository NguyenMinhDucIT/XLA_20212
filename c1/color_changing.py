import cv2 

img = cv2.imread('../photos/dragon.jpeg')
cv2.imshow('Before', img)
size = img.shape
width = size[0]
height = size[1]
print(width, height)

# for i in range(0,width):# process all pixels
#     for j in range(0,height):
#         data = img[i,j]
#         #print(data) #(255, 255, 255)
#         # if (data[0]==255 and data[1]==255 and data[2]==255):
#         img[i, j][0] += 50
#         img[i, j][1] += 50
#         img[i, j][2] += 50
# cv2.imshow('After', img)
# cv2.waitKey(0)	

# Convert to GRAYSCALE
gr_pic = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gr_pic)
cv2.waitKey(0)	
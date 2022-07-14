import cv2



#reading the image
img = cv2.imread('../photos/cat1.jpeg', cv2.IMREAD_UNCHANGED)
cv2.imshow('Original', img)
print('Original Dimensions : ',img.shape)

#change size
def resizing(samp): 
    scale_percent = 60 # percent of original size
    width = int(samp.shape[1] * scale_percent / 100)
    height = int(samp.shape[0] * scale_percent / 100)
    dim = (width, height)
      
    # resize image
    resized = cv2.resize(samp, dim, interpolation = cv2.INTER_AREA)
     
    print('Resized Dimensions : ',resized.shape)
     
    cv2.imshow("Resized image", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#change res?
def changing_res(samp):
    cap = cv2.imread('../photos/cat1.jpeg', cv2.IMREAD_UNCHANGED)

    def make_1080p():
        cap.set(3, 1920)
        cap.set(4, 1080)

    def make_720p():
        cap.set(3, 1280)
        cap.set(4, 720)
        cv2.imshow("Resized image", cap)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def make_480p():
        cap.set(3, 640)
        cap.set(4, 480)

    def change_res(width, height):
        cap.set(3, width)
        cap.set(4, height)

    # make_720p()
    # change_res(1280, 720)

#change color
def to_gray(samp):
    size = samp.shape
    width = size[0]
    height = size[1]
    print('After: ', img.shape)

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

# resizing(img)
to_gray(img)

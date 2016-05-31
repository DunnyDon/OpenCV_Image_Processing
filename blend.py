import cv2
import numpy as np
# Load two images
img1 = cv2.imread('Colour.jpg')
img2 = cv2.imread('test.jpg')

# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
edgerow, edgecol, edgechan = img1.shape
roi = img1[0:rows, 0:cols ]
print img1.shape, img2.shape
# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
resized_image = cv2.resize(img1, (1000, 400))
cv2.imshow('res',resized_image )
cv2.waitKey(0)
cv2.destroyAllWindows()
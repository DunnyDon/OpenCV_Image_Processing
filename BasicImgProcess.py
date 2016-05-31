import numpy as np
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('Colour.jpg')

b,g,r = cv2.split(img)
img[:,:,2] = 0
replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
resized_image = cv2.resize(img, (1000, 500)) 
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.show()
cv2.imshow('image',resized_image)
cv2.waitKey(0)
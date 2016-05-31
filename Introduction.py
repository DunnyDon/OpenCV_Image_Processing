import numpy as np
import cv2

img = cv2.imread('test.jpg',0)
# passing in 0 changes the image to black and white
cv2.imshow('image',img)
cv2.waitKey(0)
#Argument passed is measured in milliseconds 
# If 0 is passed then function waits indefinitely
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('test.png',img)
    cv2.destroyAllWindows()
cv2.destroyAllWindows()
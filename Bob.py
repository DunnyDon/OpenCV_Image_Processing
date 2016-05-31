import cv2

vc = cv2.VideoCapture('test.mp4')
c=1

if vc.isOpened():
	rval , frame = vc.read()
	print vc.isOpened()
else:
	rval = False
	print vc.isOpened()

while rval:
    rval, frame = vc.read()
    cv2.imwrite(str(c) + '.jpg',frame)
    c = c + 1
    cv2.waitKey(1)
vc.release()
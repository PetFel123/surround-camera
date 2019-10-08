import cv2
import numpy as np

def readImage(vc):
    if vc.isOpened():
        return vc.read()
    else:
        return False, False

cv2.namedWindow("preview")
vc1 = cv2.VideoCapture(0)
vc2 = cv2.VideoCapture(2)

rval1, frame1 = readImage(vc1)
rval2, frame2 = readImage(vc2)

while rval1 and rval2:
    cv2.imshow("preview", np.concatenate((frame1, frame2), axis = 1))
    
    rval1, frame1 = readImage(vc1)
    rval2, frame2 = readImage(vc2)
    
    key = cv2.waitKey(20)
    if key == 27:
        break
cv2.destroyWindow("preview")
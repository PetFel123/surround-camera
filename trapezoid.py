import cv2
import numpy as np

def warpImage(frame):
    rows, cols, _ = frame.shape

    black = np.zeros((rows + 300, cols + 300, 3), np.uint8)

    br, bc, _ = black.shape

    src = np.array([[0.0, 0.0],[float(cols), 0.0],[float(cols), float(rows)], [0.0, float(rows)]])

    dst = np.array([[0.0, 0.0], [float(bc), 0.0], [bc * 0.6, float(br)], [bc * 0.4, float(br)]])

    h, _ = cv2.findHomography(src, dst)

    print("rows = ", br, ", cols = ", bc)

    return cv2.warpPerspective(frame, h, (bc, br))


cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened():
    rval, frame = vc.read()
else:
    rval = False

out = warpImage(frame)

while rval:
    cv2.imshow("preview", out)
    
    rval, frame = vc.read()

    out = warpImage(frame)

    key = cv2.waitKey(20)
    if key == 27:
        break
cv2.destroyWindow("preview")
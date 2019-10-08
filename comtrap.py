import cv2
import numpy as np

def warpImage(frame, frac, addr, addc, rot):
    rows, cols, _ = frame.shape

    black = np.zeros((rows + addr, cols + addc, 3), np.uint8)

    br, bc, _ = black.shape

    src = np.array([[0.0, 0.0],[float(cols), 0.0],[float(cols), float(rows)], [0.0, float(rows)]])

    dst = np.array([[0.0, 0.0], [float(bc), 0.0], [bc * (1-frac), float(br)], [bc * frac, float(br)]])

    h, _ = cv2.findHomography(src, dst)

    if rot:
        return cv2.warpPerspective(frame, h, (1253, 940))
    else:
        return cv2.warpPerspective(frame, h, (940, 1253))


cv2.namedWindow("preview")
vc1 = cv2.VideoCapture(0)
vc = cv2.VideoCapture(2)

if vc.isOpened():
    rval, frame = vc.read()
    rval1, frame1 = vc1.read()
else:
    rval = False

out = warpImage(frame, 0.4, 300, 300, False)
out1 = cv2.rotate(warpImage(frame1, 0.4, -120, 613, True), cv2.ROTATE_90_CLOCKWISE)

while rval:
    cv2.imshow("preview", out1 + out)

    rval, frame = vc.read()
    rval1, frame1 = vc1.read()

    out = warpImage(frame, 0.4, 300, 300, False)
    out1 = cv2.rotate(warpImage(frame1, 0.45, -120, 613, True), cv2.ROTATE_90_CLOCKWISE)

    key = cv2.waitKey(20)
    if key == 27:
        break
cv2.destroyWindow("preview")
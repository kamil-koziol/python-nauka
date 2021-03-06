from cv2 import cv2
import numpy as np

cap = cv2.VideoCapture(0)

window = cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars", 512,512)
cv2.createTrackbar("Hue Min", "Trackbars", 0, 179, lambda x:x)
cv2.createTrackbar("Hue Max", "Trackbars", 24, 179, lambda x:x)
cv2.createTrackbar("Sat Min", "Trackbars", 88, 255, lambda x:x)
cv2.createTrackbar("Sat Max", "Trackbars", 255, 255, lambda x:x)
cv2.createTrackbar("Val Min", "Trackbars", 137, 255, lambda x:x)
cv2.createTrackbar("Val Max", "Trackbars", 255, 255, lambda x:x)

while True:
    s, frame = cap.read()

    mins = np.array([
        cv2.getTrackbarPos("Hue Min", "Trackbars"),
        cv2.getTrackbarPos("Sat Min", "Trackbars"),
        cv2.getTrackbarPos("Val Min", "Trackbars")
    ], dtype=np.uint8)

    maxes = np.array([
        cv2.getTrackbarPos("Hue Max", "Trackbars"),
        cv2.getTrackbarPos("Sat Max", "Trackbars"),
        cv2.getTrackbarPos("Val Max", "Trackbars")
    ], dtype=np.uint8)

    mask = cv2.inRange(frame, mins, maxes)
    # result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("Mask", mask)
    cv2.waitKey(1)
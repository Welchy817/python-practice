from pyimagesearch.shape_detector import ShapeDetector
import argparse
import imutils
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

gray    = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh  = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]

cv2.imshow("Thresh", thresh)
cv2.waitKey(0)

contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
sd = ShapeDetector

for c in contours:
    M = cv2.moments(c)
    try:
        cX = int((M["m10"] / M["m00"]))
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    try:
        cY = int((M["m01"] / M["m00"]))
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    shape = sd.detect(c)

    c = c.astype(int)
    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
    cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    cv2.imshow("Image", image)
    cv2.waitKey(0)
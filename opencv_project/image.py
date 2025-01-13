import cv2 as cv

image = cv.imread("./cappy.png")

cv.imshow("Display Window", image)
assert image is not None, "file could not be read, check with os.path.exists()"
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(image, contours, -1, (0,255,0), 3)
k = cv.waitKey(0)
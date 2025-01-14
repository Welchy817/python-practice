import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])

cv2.imshow("Display Window", image)
print("Printing base image...")
assert image is not None, "file could not be read, check with os.path.exists()"
k = cv2.waitKey(0)

grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print("Printing image in grayscale...")
cv2.imshow("Display Window", grayscale)
k = cv2.waitKey(0)
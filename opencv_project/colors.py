import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Games", image)
cv2.waitKey(0)
boundaries = [
    ([86, 31, 4], [220, 131, 100]),     # Blue
    ([42, 56, 36], [88, 191, 81]),      # Green
    ([24, 26, 101], [84, 94, 218]),     # Red
    ([27, 153, 164], [102, 198, 221])   # Yellow

]

for (lower, upper) in boundaries:
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")

    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    cv2.imshow("images", np.hstack([image, output]))
    cv2.waitKey(0)
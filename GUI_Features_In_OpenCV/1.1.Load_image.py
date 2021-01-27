import cv2 as cv
import sys

# Read image
Image_folder = "./Image/"
img = cv.imread(cv.samples.findFile(Image_folder + "Night.jpg"))

# Show image
cv.imshow("Display image", img)
k = cv.waitKey(0)

# Press "S" to save image
if k == ord("S"):
    cv.imwrite(Image_folder + "Saved_Image.png", img)
import cv2 as cv
import numpy as np

img = np.zeros((512,512,3))

# Draw a line
cv.line(img, (0, 0), (511,511), (255,255,255), 5)

# Draw a rectangle
cv.rectangle(img, (0,511), (100,100), (255,0,0), 5)

# Draw a circle
cv.circle(img, (int(512/2),int(512/2)), 100, (0,255,0),5)

cv.imshow("Draw", img)
k = cv.waitKey(0)
if k == ord("q"):
    cv.destroyAllWindows()
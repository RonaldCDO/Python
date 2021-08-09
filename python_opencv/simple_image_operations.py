import cv2 as cv
import sys
from matplotlib import pyplot as plt

img = cv.imread("teste1.png", 0)
# plt.hist(img.ravel(),256, [0,256])
# plt.show()

if img is None:
    sys.exit('Could not read the image.')

cv.imshow('Display Window', img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("teste1.png", img)

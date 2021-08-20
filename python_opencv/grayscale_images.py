import cv2 as cv
import numpy as np

im = cv.imread('car.png', 0)

kernel = np.ones((5, 5), np.int16) * 1 / 25

out = cv.filter2D(im, -1, kernel)
print(out)
for i in range(len(out)):
    for j in range(len(out[0])):
        if out[i][j] < 128:
            out[i][j] = 255
        else:
            out[i][j] = 0

cv.imshow('output', out)

cv.waitKey(0)
cv.destroyAllWindows()

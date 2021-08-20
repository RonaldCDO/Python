import numpy as np
import cv2 as cv


im = cv.imread('car1.png')

m1 = np.ones((5, 5), np.int16)


print('im', type(im))
print('m1', type(m1))
print(m1)

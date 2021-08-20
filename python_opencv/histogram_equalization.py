import cv2
import numpy as np

img = cv2.imread('teste1.png', 0)

equ = cv2.equalizeHist(img)

res = np.hstack(img)

cv2.imshow('teste', res)

cv2.waitKey(0)
cv2.destroyAllWindows()

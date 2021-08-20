import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

im = cv.imread('test80.jpg')


def is_gray(input_img):
    if len(input_img.shape) < 3:
        return True


def dec_int(input_im):
    if not is_gray(input_im):
        r, g, b = cv.split(input_im)
        r = resize_im(r)
        g = resize_im(g)
        b = resize_im(b)
        new_im = np.dstack((r, g, b))
    else:
        new_im = resize_im(input_im)
    return new_im


def resize_im(channel):
    res_ch = []
    for i in range(len(channel)):
        for j in range(len(channel[0])):
            if i % 2 == 0 and j % 2 == 0:
                aux = channel[i][j]
                res_ch.append(aux)
    res_ch = np.array(res_ch)
    res_ch = np.reshape(res_ch, (int(len(channel) / 2), int(len(channel[0]) / 2)))
    return res_ch


def edge_improv(input_im):
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    if not is_gray(input_im):
        r, g, b = cv.split(input_im)
        r_filtered = cv.filter2D(r, -1, kernel)
        g_filtered = cv.filter2D(g, -1, kernel)
        b_filtered = cv.filter2D(b, -1, kernel)
        out_im = np.dstack((r_filtered, g_filtered, b_filtered))
    else:
        out_im = cv.filter2D(input_im, -1, kernel)
    return out_im


def filter_average(input_im):
    kernel = np.ones((5, 5), np.int16) * 1 / 25
    if not is_gray(input_im):
        r, g, b = cv.split(input_im)
        filtered_r = cv.filter2D(r, -1, kernel)
        filtered_g = cv.filter2D(g, -1, kernel)
        filtered_b = cv.filter2D(b, -1, kernel)
        filtered_im = np.dstack((filtered_r, filtered_g, filtered_b))
    else:
        filtered_im = cv.filter2D(input_im, -1, kernel)
    return filtered_im


# cv.imshow('Output', output)
# cv.imshow('R_Filtered', out_resized_ft)

# cv.imshow('R_sharp', output_sharp)
# cv.imshow('R_unsharp', unsharp_out)

moon_orig = dec_int(im)
moon_edges = edge_improv(moon_orig)
moon_out = moon_orig - moon_edges

moon_orig2 = dec_int(im)
moon_unsharp2 = filter_average(moon_orig2)
moon_edges2 = moon_orig2 - moon_unsharp2
moon_out2 = moon_orig2 + moon_edges2

cv.imshow('moon_orig', moon_orig)
cv.imshow('moon_edges', moon_edges)
cv.imshow('moon_out', moon_out)

cv.imshow('moon_orig2', moon_orig2)
cv.imshow('moon_unsharp2', moon_unsharp2)
cv.imshow('moon_edges2', moon_edges2)
cv.imshow('moon_out2', moon_out2)
# cv.imshow('unsharp', out_unsharp)

# cv.imshow('binary', binary_unsharp)

cv.waitKey(0)
cv.destroyAllWindows()
#
# cv.imshow('Input', im)
# cv.imshow('Output', output_im)
# oute = edge_improv(im)
# cv.imshow('Filtered', oute)
# cv.waitKey(0)
# cv.destroyAllWindows()

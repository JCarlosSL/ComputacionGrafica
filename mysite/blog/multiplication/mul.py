import cv2
import numpy as np


def mult(imgA, c):
    imgA = imgA.astype(int)
    rows = imgA.shape[0]
    cols = imgA.shape[1]
    for i in range(rows):
        for j in range(cols):
            b, r, g = imgA[i, j]
            b = b * c
            r = r * c
            g = g * c
            imgA[i, j] = b, r, g
    imgA[np.where(imgA > 255)] = 255
    return imgA.astype(np.uint8)


imgA = cv2.imread('mul_4.jpg')


imgOutput = mult(imgA, 3)

cv2.imwrite('imgout.png',imgOutput)
#cv2.imshow('', imgOutput)
#cv2.waitKey(0)



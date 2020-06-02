import numpy as np
import cv2

IMG_1 = cv2.imread('add_10.jpg')
IMG_2 = cv2.imread('add_11.jpg')

SIZE_1 = IMG_1.shape[0] + IMG_1.shape[1]
SIZE_2 = IMG_2.shape[0] + IMG_2.shape[1]

if (SIZE_1 > SIZE_2):
    IMG_1 = cv2.resize(IMG_1, IMG_2.shape[1::-1])
else:
    IMG_2 = cv2.resize(IMG_2, IMG_1.shape[1::-1])

alpha_img = np.floor_divide(IMG_1, 2)
beta_img = np.floor_divide(IMG_2, 2)

np_add = np.add(alpha_img, beta_img)
np_add.astype(np.int8)
cv2.imshow('', np_add)
cv2.waitKey(0)

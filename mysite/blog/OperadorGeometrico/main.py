import numpy as np
import cv2 as cv
from  affineTref import affine as AT 
from getaffineTransform import getaffineTransform
import matplotlib.pyplot as plt

img = cv.imread('mul_4.jpg')
rows,cols=img.shape[0],img.shape[1]

g = AT()

#pts1 = np.float32([[50,50],[200,50],[50,200]])
#pts2 = np.float32([[10,100],[200,50],[100,250]])

pts1 = np.float32([[3,2],[20,15],[50,200]])
pts2 = np.float32([[10,100],[20,50],[400,250]])
M = getaffineTransform(pts1,pts2)
dst = cv.warpAffine(img,M,(cols,rows))
plt.subplot(121),plt.imshow(img),plt.title('input')
plt.subplot(122),plt.imshow(dst),plt.title('output')
plt.show()


"""
px = cols/2
py = rows/2
M = g.Mrotate(127,px,py)
ro,co = g.rotacion(px,py,M,rows,cols)
newimg = g.warpAffine(img,M,ro,co)
cv.imwrite('news_127.png',newimg)
"""

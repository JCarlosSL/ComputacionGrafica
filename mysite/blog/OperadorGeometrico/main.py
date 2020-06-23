import numpy as np
import cv2 as cv
from  affineTransformation import affine as AT 


img = cv.imread('mul_4.jpg')
rows,cols=img.shape[0],img.shape[1]

g = AT()

#M = g.rotate(270,[c/2,r/2])
M = g.Mtranslate([120,100])
#M = g.shear([0.2,0.1])
#M = g.scale([1,2])
newimg = g.warpAffine(img,M,rows,cols)


cv.imwrite('news1.png',newimg)


"""
M=np.float32([[1,0,180],[0,1,150]])
img_trans=cv.warpAffine(img,M,(cols,rows))
cv.imwrite('new.png',img_trans)
"""
"""
M=np.float32([[2,0,0],[0,3,0]])
img_trans=cv.warpAffine(img,M,(cols*2,rows*3))
cv.imwrite('new.png',img_trans)
"""
"""
t = 90
p=[(cols*2)/2,(rows*2)/2]
M=np.float32([[np.cos(t),np.sin(t),(1-np.cos(t))*p[0] - np.sin(t)*p[1]],
    [-np.sin(t),np.cos(t),np.sin(t)*p[0]+(1-np.sin(t))*p[1]]])
img_trans=cv.warpAffine(img,M,(cols*2,rows*2))
cv.imwrite('new.png',img_trans)
"""

"""
M=np.float32([[1,0.3,0],[0.5,1,0]])
img_trans=cv.warpAffine(img,M,(cols,rows))
cv.imwrite('new.png',img_trans)
"""



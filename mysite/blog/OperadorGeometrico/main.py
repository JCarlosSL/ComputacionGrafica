import numpy as np
import cv2 as cv
from  affineTransformation import affine as AT 
import math
img = cv.imread('mul_4.jpg')
rows,cols=img.shape[0],img.shape[1]

g = AT()

"""
M = g.Mtranslate([120,100])
newimg = g.warpAffine(img,M,rows+120,cols+100)
cv.imwrite('news1.png',newimg)
"""

"""
M = g.Mscale([0.9,1.1])
newimg = g.warpAffine(img,M,int(rows*0.9),int(cols*1.1))
cv.imwrite('news1.png',newimg)
"""

r = 2*np.pi

s = (r/360)*30
s1 = (r/360)*60
b = np.sin(s)*cols
c = np.cos(s)*cols
b1 = np.sin(s1)*rows
c1 = np.cos(s1)*rows

ro = int(b+b1)
co = int(c+c1)
M = g.Mrotate(30,[cols/2,rows/2])
newimg = g.warpAffine(img,M,ro,co)
cv.imwrite('news1.png',newimg)


"""
M = g.Mshear([0.2,0.1])
newimg = g.warpAffine(img,M,rows,cols)
cv.imwrite('news1.png',newimg)
"""


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


